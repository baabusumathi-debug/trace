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
  // Test build carries only the deck being piloted, so sync and deck download stay fast (T-070: TOX01 Explain v2)
  onlyDecks: CHANNEL === 'test' ? ['TOX01', 'TOX02', 'TOX03A', 'TOX03B', 'TOX04', 'TOX05', 'TOX06', 'RESP01A', 'BS01A', 'BS01B', 'CCM01', 'CCM03', 'CCM06', 'CCM10', 'CCM11', 'CVS03', 'CVS05B', 'CVS07A', 'CVS07B', 'D05B', 'D05C', 'ECMO01', 'EPI01A', 'EPI01C', 'HEMO05A', 'HEMO05B', 'HY1', 'HY2', 'HY6', 'HY7', 'MISC05B', 'MV04B', 'NEURO01', 'NEURO02', 'NEURO03', 'RESP03', 'SC-A', 'SC-B', 'SEP01A', 'SEP02', 'SPECIAL04A', 'SPECIAL05B', 'ECMO02A', 'MV01', 'MV02', 'MV03', 'MV04A', 'MV05', 'NEURO06A', 'NEURO06B', 'RESP01B', 'RESP01C', 'RESP02A', 'RESP02B', 'RESP04', 'RESP07A', 'RESP07B', 'ABG01', 'CVS01', 'CVS04', 'CVS06A', 'CVS06B', 'CVS09', 'GI05', 'HEMO01B', 'HEMO02', 'HEMO03B', 'HEMO04', 'HY5', 'MISC05A', 'OBS01', 'OBS02B', 'RESP05', 'SEP01B', 'SEP01C', 'SEP01E', 'SOD01A', 'SPECIAL05A', 'TRIALS01B', 'ABG02', 'ABG03', 'CCM08', 'ELEC01A', 'ELEC01B', 'ELEC02', 'ELEC03A', 'ELEC03B', 'ELEC04', 'ENDO01B', 'ENDO02A', 'ENDO02B', 'GI01A', 'GI01B', 'GI01C', 'GI02A', 'GI02B', 'GI03', 'GI06', 'GI07A', 'GI07B', 'HY4', 'HY8', 'NEURO05', 'NMD01', 'NMD02', 'NMD03', 'OBS02A', 'RENAL01', 'RENAL02', 'RENAL03', 'RENAL04', 'SC-E', 'SOD01B', 'SPECIAL01', 'SPECIAL03', 'RESP06A', 'RESP06B'] : null,   // + the decks with T-093 text corrections and the viva P4 decks (T-095) and P1 decks (T-122) and P3, P6, P7 decks (T-123) and RESP06A/B (T-126)
  appVersion: '1.3.115',
  traceFolderId: '1e_lx6kl_MhG4aOracgTr_HG3NUp7OsYs',
  doctFolderId: '1wqRbRG-nqldfafFL-AughcBEBfo6atQo',   // Trace › doct: finished DocT attempts sent by the recorder (v2.0+)
  libraryId: '1b3tMq38gqAE_m7eb5PeeJ53LjKqdggHI',   // fallback; the app looks library.json up by name
  exam: { name: 'NEET-SS', date: '2026-12-11' },
  who: IS_HT ? 'HT' : 'Trace',  // Log "who": Trace for Naven, HT for HT, as the War Map expects
  syncEveryMs: 120000,
  logIdleMs: 20 * 60000,        // a flow left open this long is written to the Log anyway
  avgWindow: 200                // rolling average over the last N cards
};
