const languages = ['ar', 'en', 'sv'];
const identity = ['make', 'model', 'year', 'engineName', 'engineCode'];
const optionalScope = ['ecu', 'market'];
const idPattern = /^[a-z][a-z0-9-]{0,79}$/;
const filled = value => typeof value === 'string' && Boolean(value.trim());
const translated = value => languages.every(lang => filled(value?.[lang]));
const normalized = value => String(value ?? '').trim().normalize('NFC').toLowerCase();
const https = value => {
  try {
    const url = new URL(value);
    return url.protocol === 'https:' && !url.username && !url.password;
  } catch { return false; }
};

export function validateSensorCatalog(data) {
  if (data?.schema !== 1 || !Array.isArray(data.sensors) || !data.sensors.length ||
      !Array.isArray(data.specifications)) throw Error('Invalid sensor catalogue');
  const ids = new Set();
  for (const row of data.sensors) {
    if (!row || !idPattern.test(row.id ?? '') || ids.has(row.id) ||
        row.scope !== 'general' || row.status !== 'documented-general' || !https(row.source) ||
        !['name', 'operation', 'measurement', 'interpretation'].every(key => translated(row[key]))) {
      throw Error('Invalid or duplicate sensor guide');
    }
    ids.add(row.id);
    if (row.references !== undefined && (!Array.isArray(row.references) ||
        row.references.some(ref => !https(ref?.url) || !translated(ref.title)))) {
      throw Error('Invalid sensor reference');
    }
  }
  const records = new Set();
  const groups = new Map();
  for (const row of data.specifications) {
    if (!row || !idPattern.test(row.id ?? '') || records.has(row.id) || !ids.has(row.sensorId) ||
        row.status !== 'approved' || !filled(row.reviewedBy) || !https(row.source) || !filled(row.locator) ||
        !['location','terminals','conditions','procedure','expected','interpretation'].every(key => translated(row[key])) ||
        !row.scope || !identity.every(key => filled(row.scope[key]) && !['*','unknown','any'].includes(normalized(row.scope[key]))) ||
        !/^\d{4}$/.test(row.scope.year) || Object.keys(row.scope).some(key => ![...identity,...optionalScope].includes(key) || !filled(row.scope[key]))) {
      throw Error('Unreviewed or incomplete vehicle specification');
    }
    const key = JSON.stringify([row.sensorId, ...identity.map(k => normalized(row.scope[k]))]);
    const scopes = groups.get(key) || [];
    if (scopes.some(s => optionalScope.every(k => !s[k] || !row.scope[k] || normalized(s[k]) === normalized(row.scope[k])))) {
      throw Error('Overlapping sensor specifications require review');
    }
    scopes.push(row.scope);
    groups.set(key, scopes);
    records.add(row.id);
  }
  return data;
}

export function matchingSensorSpec(catalog, id, vehicle) {
  return catalog.specifications.find(row => row.sensorId === id &&
    Object.entries(row.scope).every(([key, value]) => normalized(vehicle[key]) === normalized(value)));
}
