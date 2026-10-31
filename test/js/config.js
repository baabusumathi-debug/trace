// Fixed facts about Naven's Drive. The backend URL and key are NOT stored here (the code is public);
// each device receives them once through the private setup link and keeps them in IndexedDB.
// The test build lives at /trace/test/: its own storage, and it never writes to the Sheet or Drive.
export const CHANNEL = /\/test\//.test(location.pathname) ? 'test' : 'live';
export const CONFIG = {
  readOnly: CHANNEL === 'test',
  appVersion: '1.3.1',
  traceFolderId: '1e_lx6kl_MhG4aOracgTr_HG3NUp7OsYs',
  libraryId: '1b3tMq38gqAE_m7eb5PeeJ53LjKqdggHI',   // fallback; the app looks library.json up by name
  exam: { name: 'NEET-SS', date: '2026-12-11' },
  who: 'Trace',                 // Log "who" for Naven, as the War Map expects
  syncEveryMs: 120000,
  logIdleMs: 20 * 60000,        // a flow left open this long is written to the Log anyway
  avgWindow: 200                // rolling average over the last N cards
};
