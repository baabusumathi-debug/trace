// Tiny IndexedDB wrapper. Everything the app needs offline lives here.
const STORES = {
  kv: null,                       // key -> value
  decks: 'deck',                  // { deck, version, cards[], verified, downloadedAt }
  events: 'id',                   // card views (the source of truth for "times seen")
  logrows: 'id',                  // War Map Log rows waiting to be appended
  edits: 'key',                   // card edits: key = deck|code
  visuals: 'deck',                // accepted visual-deck package per deck (from ChatGPT, validated)
  vimg: 'key'                     // visual images: key = deck|file, value { blob }
};

let dbp = null;
let DBNAME = 'trace';
export function useDemoDb() { DBNAME = 'trace-demo'; dbp = null; }
export function useDbName(n) { DBNAME = n; dbp = null; }

function open() {
  if (dbp) return dbp;
  dbp = new Promise((resolve, reject) => {
    const req = indexedDB.open(DBNAME, 2);
    req.onupgradeneeded = () => {
      const db = req.result;
      for (const [name, key] of Object.entries(STORES)) {
        if (!db.objectStoreNames.contains(name)) {
          const st = key ? db.createObjectStore(name, { keyPath: key }) : db.createObjectStore(name);
          if (name === 'events') { st.createIndex('synced', 'synced'); st.createIndex('deck', 'deck'); }
        }
      }
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
  return dbp;
}

function tx(store, mode, fn) {
  return open().then(db => new Promise((resolve, reject) => {
    const t = db.transaction(store, mode);
    const st = t.objectStore(store);
    let result;
    Promise.resolve(fn(st)).then(r => { result = r; });
    t.oncomplete = () => resolve(result);
    t.onerror = () => reject(t.error);
    t.onabort = () => reject(t.error);
  }));
}
const wrap = req => new Promise((res, rej) => { req.onsuccess = () => res(req.result); req.onerror = () => rej(req.error); });

export const db = {
  get: (store, key) => tx(store, 'readonly', st => wrap(st.get(key))),
  all: (store) => tx(store, 'readonly', st => wrap(st.getAll())),
  put: (store, val, key) => tx(store, 'readwrite', st => { key === undefined ? st.put(val) : st.put(val, key); }),
  putMany: (store, vals) => tx(store, 'readwrite', st => { vals.forEach(v => st.put(v)); }),
  del: (store, key) => tx(store, 'readwrite', st => { st.delete(key); }),
  delMany: (store, keys) => tx(store, 'readwrite', st => { keys.forEach(k => st.delete(k)); }),
  kv: {
    get: key => tx('kv', 'readonly', st => wrap(st.get(key))),
    set: (key, val) => tx('kv', 'readwrite', st => { st.put(val, key); })
  }
};

// Read one value from another Trace database on this device without ever creating or changing it.
export async function peekDb(name, store, key) {
  try {
    if (indexedDB.databases) { const all = await indexedDB.databases(); if (!all.some(d => d.name === name)) return null; }
    return await new Promise(resolve => {
      const req = indexedDB.open(name);
      req.onupgradeneeded = () => { req.transaction.abort(); };     // it did not exist: leave no trace
      req.onerror = () => resolve(null);
      req.onsuccess = () => {
        const d = req.result;
        try { const g = d.transaction(store, 'readonly').objectStore(store).get(key); g.onsuccess = () => { resolve(g.result || null); d.close(); }; g.onerror = () => { resolve(null); d.close(); }; }
        catch (e) { resolve(null); d.close(); }
      };
    });
  } catch (e) { return null; }
}
