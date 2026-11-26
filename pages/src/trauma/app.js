function hh(){var h=document.querySelector('header');if(h)document.documentElement.style.setProperty('--hh',h.offsetHeight+'px')}window.addEventListener('resize',hh);hh();
var K='trauma.';
function get(n,d){try{var v=localStorage.getItem(K+n);return v?JSON.parse(v):d}catch(e){return d}}
function put(n,v){try{localStorage.setItem(K+n,JSON.stringify(v))}catch(e){}}
function recallOn(){return document.body.classList.contains('recall')}
// with recall on, no tab opens by itself: the cards and traps below would give the blanks away
function show(id,tab){document.querySelectorAll('.view').forEach(function(v){v.hidden=v.id!==id});
 if(id!=='HOME'){var v=document.getElementById(id);var ps=v.querySelectorAll('.pane');if(ps.length){var t=tab||(recallOn()?null:ps[0].id);ps.forEach(function(p){p.hidden=p.id!==t});v.querySelectorAll('.tab').forEach(function(b){b.classList.toggle('on',b.dataset.p===t)});}}
 paint();}
function route(){var h=location.hash.slice(1);var el=h&&document.getElementById(h);if(!el){show('HOME');window.scrollTo(0,0);return}
 if(el.classList.contains('view')){show(h);window.scrollTo(0,0);setTimeout(function(){window.scrollTo(0,0)},0)}else{var v=el.closest('.view'),p=el.closest('.pane');show(v.id,p?p.id:null);el.scrollIntoView({block:'center'});}}
window.addEventListener('hashchange',route);
function setRecall(on){document.body.classList.toggle('recall',on);var b=document.getElementById('rcbtn');b.classList.toggle('on',on);b.textContent='Recall: '+(on?'on':'off');put('recall',on);
 document.querySelectorAll('.cz.sh').forEach(function(x){x.classList.remove('sh')});
 var cur=[].find.call(document.querySelectorAll('.view'),function(v){return !v.hidden});if(cur)show(cur.id);}
document.addEventListener('click',function(ev){
 var cz=ev.target.closest('.cz');
 if(cz&&recallOn()){cz.classList.toggle('sh');return;}
 var b=ev.target.closest('button,a');if(!b)return;
 if(b.dataset.go){location.hash=b.dataset.go;}
 if(b.classList.contains('home')){location.hash='HOME';}
 if(b.id==='rcbtn'){setRecall(!recallOn());}
 if(b.classList.contains('rall')){b.closest('.view').querySelectorAll('.cz').forEach(function(x){x.classList.add('sh')});}
 if(b.classList.contains('rcov')){b.closest('.view').querySelectorAll('.cz').forEach(function(x){x.classList.remove('sh')});}
 if(b.classList.contains('tab')){var v2=b.closest('.view');show(v2.id,b.dataset.p);}
 if(b.classList.contains('rv')){var a=b.nextElementSibling;while(a&&!a.classList.contains('ans'))a=a.nextElementSibling;if(a){if(!b.dataset.l)b.dataset.l=b.textContent;a.hidden=!a.hidden;b.textContent=a.hidden?b.dataset.l:'Hide';}}
 if(b.classList.contains('tg')){var t=document.getElementById(b.dataset.t);t.hidden=!t.hidden;b.textContent=t.hidden?'Show the decision tree':'Hide the decision tree';}
 if(b.classList.contains('mk')){var k=b.dataset.k,m=get('miss',{});if(m[k])delete m[k];else m[k]=(b.closest('[id]')||{}).id||'';put('miss',m);paint();}
 if(b.classList.contains('done')){var d=get('done',{}),s=b.dataset.s;if(d[s])delete d[s];else d[s]=1;put('done',d);if(d[s])location.hash='HOME';else paint();}
 if(b.id==='mclr'){var w=document.getElementById('mclrq');if(w)w.hidden=!w.hidden;}
 if(b.id==='mclry'){put('miss',{});document.getElementById('mclrq').hidden=true;paint();}
});
function paint(){var m=get('miss',{}),ks=Object.keys(m),d=get('done',{});
 document.querySelectorAll('button.mk').forEach(function(b){b.classList.toggle('on',!!m[b.dataset.k]);b.textContent=m[b.dataset.k]?'Missed ✓':'Missed'});
 document.querySelectorAll('.tile[data-go]').forEach(function(t){t.classList.toggle('ok',!!d[t.dataset.go])});
 document.querySelectorAll('button.done').forEach(function(b){b.classList.toggle('on',!!d[b.dataset.s]);b.textContent=d[b.dataset.s]?'Done ✓ (tap to undo)':'Mark concept done ✓'});
 var n=document.querySelectorAll('.tiles .tile.ok').length,T=document.querySelectorAll('.tiles .tile').length;
 document.getElementById('pc').textContent=n+' of '+T+' concepts done';document.getElementById('pb').style.width=(T?100*n/T:0)+'%';
 document.getElementById('ml').innerHTML=ks.length?ks.map(function(k){return '<li><a href="#'+m[k]+'">'+k+'</a></li>'}).join(''):'<li>Nothing marked yet.</li>';document.getElementById('mc').textContent=ks.length;}
setRecall(get('recall',false));route();
