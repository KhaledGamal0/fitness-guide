export const load = (key, def) => {
  try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : def }
  catch { return def }
}
export const save = (key, val) => {
  try { localStorage.setItem(key, JSON.stringify(val)) } catch {}
}
