"""Ensure changed website content came through a merged, independently approved PR."""
import json
import os
import subprocess
import sys
from pathlib import Path

from website_library import read_snapshot, require


def api(path):
    args = ["gh", "api", "--paginate", "--slurp", f"repos/{os.environ['GITHUB_REPOSITORY']}/{path}"]
    pages = json.loads(subprocess.check_output(args, text=True))
    return [item for page in pages for item in page]


def authorize(candidate, previous):
    if previous is None and not any(candidate["sections"].values()):
        return
    revision = candidate["revision"]
    for pr in api(f"commits/{revision}/pulls"):
        if not (pr["merged_at"] and pr["base"]["ref"] == "main" and pr["merge_commit_sha"] == revision):
            continue
        head = pr["head"]["sha"]
        number = pr["number"]
        tree = lambda commit: subprocess.check_output(["git", "rev-parse", f"{commit}^{{tree}}"]).strip()
        # Compare the reviewed tree to the exact merge result, including the build code.
        subprocess.run(["git", "fetch", "origin", f"refs/pull/{number}/head"], check=True)
        if tree(head) != tree(revision):
            continue
        changed = {f["filename"] for f in api(f"pulls/{number}/files?per_page=100")}
        dependencies = set(candidate["changedFiles"]) - changed
        def unchanged_dependency(file):
            if previous is None or file in previous["files"] or not file.startswith(("data/master/", "volkswagen/")):
                return False
            check = subprocess.run(["git", "diff", "--quiet", previous["revision"], revision, "--", file])
            return check.returncode == 0
        if not all(unchanged_dependency(file) for file in dependencies):
            continue
        reviews = {}
        for review in api(f"pulls/{number}/reviews?per_page=100"):
            if review["state"] != "COMMENTED":
                reviews[review["user"]["login"]] = review
        for login, r in reviews.items():
            if (login != pr["user"]["login"] and r["state"] == "APPROVED" and r["commit_id"] == head
                    and r["author_association"] in {"MEMBER", "OWNER", "COLLABORATOR"}):
                permission = subprocess.check_output(["gh", "api",
                    f"repos/{os.environ['GITHUB_REPOSITORY']}/collaborators/{login}/permission",
                    "--jq", ".permission"], text=True).strip()
                if permission in {"admin", "write", "maintain"}:
                    print(f"PR #{number}, reviewer {login}, exact reviewed tree {head}")
                    return
    require(False, "publication requires independent write-authorized approval of the exact merged content")


if __name__ == "__main__":
    previous_file = Path(sys.argv[2])
    authorize(read_snapshot(Path(sys.argv[1])), read_snapshot(previous_file) if previous_file.exists() else None)
