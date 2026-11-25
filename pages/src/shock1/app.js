var K='shock1.';
function get(n,d){try{var v=localStorage.getItem(K+n);return v?JSON.parse(v):d}catch(e){return d}}
function put(n,v){try{localStorage.setItem(K+n,JSON.stringify(v))}catch(e){}}
function show(id){
  var el=document.getElementById(id);if(!el)return;
  document.querySelectorAll('.view').forEach(function(v){v.hidden=v.id!==id});
  window.scrollTo(0,0);setTimeout(function(){window.scrollTo(0,0)},0);
  if(id!=='HOME'){var s=get('seen',{});s[id]=1;put('seen',s);}
  paint();
}
function route(){var h=location.hash.slice(1);show(document.getElementById(h)?h:'HOME');}
window.addEventListener('hashchange',route);
document.addEventListener('click',function(ev){
  var b=ev.target.closest('button');if(!b)return;
  if(b.dataset.go){location.hash=b.dataset.go;return}
  if(b.classList.contains('home')){location.hash='HOME';return}
  if(b.classList.contains('rv')){
    var a=b.nextElementSibling;
    if(a&&a.classList.contains('ans')){
      if(!b.dataset.l)b.dataset.l=b.textContent;
      a.hidden=!a.hidden;b.textContent=a.hidden?b.dataset.l:'Hide';
    }
  }
});
function paint(){
  var s=get('seen',{});
  document.querySelectorAll('.tile[data-go]').forEach(function(t){t.classList.toggle('done',!!s[t.dataset.go])});
}
route();
