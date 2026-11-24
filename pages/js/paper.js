// Paper styles for the note pages. Each returns the CSS background for one page.
export const PAPERS = [
  ['plain',    'Plain'],
  ['lines-n',  'Lines · narrow'],
  ['lines-w',  'Lines · wide'],
  ['grid-n',   'Grid · narrow'],
  ['grid-w',   'Grid · wide'],
  ['dots-n',   'Dots · narrow'],
  ['dots-w',   'Dots · wide']
];
export const COLOURS = [
  ['white',  'White',  '#ffffff', '#c9ced8'],
  ['cream',  'Cream',  '#fdf6e3', '#d8cdaa'],
  ['grey',   'Grey',   '#f0f2f5', '#c3c9d4'],
  ['yellow', 'Yellow', '#fdf8d0', '#d9d08a'],
  ['blue',   'Blue',   '#eef4fb', '#b9ccE4'],
  ['green',  'Green',  '#eef7ee', '#b9d6ba'],
  ['pink',   'Pink',   '#fdeff2', '#e3bcc6']
];
export const LAYOUTS = [['fixed', 'Separate pages (A4)'], ['flow', 'One long page per card']];
const col = id => COLOURS.find(c => c[0] === id) || COLOURS[0];

// u = page units per CSS pixel at 100%: the rulings are drawn in page units so they zoom with the ink
export function paperCss(paper, colour) {
  const c = col(colour), bg = c[2], ln = c[3];
  const line = (n) => `repeating-linear-gradient(to bottom, transparent 0 ${n - 1}px, ${ln} ${n - 1}px ${n}px)`;
  const vert = (n) => `repeating-linear-gradient(to right, transparent 0 ${n - 1}px, ${ln} ${n - 1}px ${n}px)`;
  const dot = (n) => `radial-gradient(${ln} 1.4px, transparent 1.5px)`;
  switch (paper) {
    case 'lines-n': return { 'background-image': line(26), 'background-color': bg, 'background-size': 'auto' };
    case 'lines-w': return { 'background-image': line(40), 'background-color': bg, 'background-size': 'auto' };
    case 'grid-n':  return { 'background-image': `${line(24)}, ${vert(24)}`, 'background-color': bg, 'background-size': 'auto' };
    case 'grid-w':  return { 'background-image': `${line(40)}, ${vert(40)}`, 'background-color': bg, 'background-size': 'auto' };
    case 'dots-n':  return { 'background-image': dot(24), 'background-color': bg, 'background-size': '24px 24px' };
    case 'dots-w':  return { 'background-image': dot(40), 'background-color': bg, 'background-size': '40px 40px' };
    default:        return { 'background-image': 'none', 'background-color': bg };
  }
}
export function applyPaper(el, paper, colour) {
  const css = paperCss(paper, colour);
  el.style.backgroundImage = css['background-image'];
  el.style.backgroundColor = css['background-color'];
  el.style.backgroundSize = css['background-size'] || 'auto';
  el.dataset.paper = paper; el.dataset.colour = colour;
}
export const paperName = id => (PAPERS.find(p => p[0] === id) || PAPERS[0])[1];
export const colourName = id => col(id)[1];
