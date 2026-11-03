// Fixed facts about Naven's Drive. The backend URL and key are NOT stored here (the code is public);
// each device receives them once through the private setup link and keeps them in IndexedDB.
// The test build lives at /trace/test/: its own storage, and it never writes to the Sheet or Drive.
export const CHANNEL = /\/test\//.test(location.pathname) ? 'test' : 'live';
// Who studies on this device: 'trace' (Naven) or 'ht' (HT). Chosen once per device; each profile has its own storage.
const PKEY = (CHANNEL === 'test' ? 'trace-test.' : 'trace.') + 'profile';
export const PROFILE = (() => { try { const v = JSON.parse(localStorage.getItem(PKEY)); return v === 'ht' || v === 'trace' ? v : null; } catch (e) { return null; } })();
export function setProfile(p) { try { localStorage.setItem(PKEY, JSON.stringify(p)); return localStorage.getItem(PKEY) === JSON.stringify(p); } catch (e) { return false; } }
export const IS_HT = PROFILE === 'ht';
export const CONFIG = {
  readOnly: CHANNEL === 'test',
  appVersion: '1.3.26',
  traceFolderId: '1e_lx6kl_MhG4aOracgTr_HG3NUp7OsYs',
  doctFolderId: '1wqRbRG-nqldfafFL-AughcBEBfo6atQo',   // Trace › doct: finished DocT attempts sent by the recorder (v2.0+)
  libraryId: '1b3tMq38gqAE_m7eb5PeeJ53LjKqdggHI',   // fallback; the app looks library.json up by name
  exam: { name: 'NEET-SS', date: '2026-12-11' },
  who: IS_HT ? 'HT' : 'Trace',  // Log "who": Trace for Naven, HT for HT, as the War Map expects
  syncEveryMs: 120000,
  logIdleMs: 20 * 60000,        // a flow left open this long is written to the Log anyway
  avgWindow: 200                // rolling average over the last N cards
};
