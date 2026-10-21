(function(){
var r=document.documentElement,t=document.getElementById('tt');
function store(v){try{localStorage.setItem('theme',v)}catch(e){}}
var s=null;try{s=localStorage.getItem('theme')}catch(e){}
function dark(){return r.getAttribute('data-theme')==='dark'||(!r.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme: dark)').matches)}
function icon(){t.textContent=dark()?'\u2600':'\u263D'}
if(s)r.setAttribute('data-theme',s);icon();
t.onclick=function(){var v=dark()?'light':'dark';r.setAttribute('data-theme',v);store(v);icon()};
// hide a figure whose image file is not uploaded yet, and any figure section left empty
document.querySelectorAll('figure img,figure video').forEach(function(m){m.addEventListener('error',function(){m.closest('figure').remove();clean()},true)});
function clean(){document.querySelectorAll('.figs').forEach(function(f){if(!f.querySelector('figure'))f.closest('section').remove()})}
})();
