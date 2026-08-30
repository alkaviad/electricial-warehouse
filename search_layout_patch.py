def apply(legacy):
    patch = r'''<style>
/* Search page: remove the large empty area and put all useful search controls immediately in view. */
#searchPage{padding-top:0!important}
#searchPage>h2{margin:0 0 4px!important}
#searchPage>.subtitle{margin:0 0 10px!important}
#searchPage .search-center{gap:9px!important}
#searchPage .search-card{padding:11px 12px!important}
#searchPage .search-card h3{margin:0 0 6px!important;font-size:16px!important}
#searchPage .search-results{margin-top:7px!important}

/* Permanent right navigation stays fixed while search/results scroll. */
.side{position:sticky!important;top:12px!important;align-self:start!important;height:max-content!important;z-index:10!important}

@media(min-width:721px){
  .workspace{grid-template-columns:118px minmax(0,1fr)!important;gap:12px!important}
  .diamond-button{width:96px!important;height:96px!important}
  .diamond{width:68px!important;height:68px!important;margin:14px auto!important}
  .diamond-inner{width:88px!important;font-size:12px!important}
}
</style>
<script>
(function(){
  function compactSearch(){
    const p=document.getElementById('searchPage');
    if(!p)return;
    /* A stray empty block from older layout/patches must not reserve screen space. */
    Array.from(p.children).forEach(el=>{
      if(el.matches('h2,.subtitle,.search-center'))return;
      const txt=(el.textContent||'').trim();
      if(!txt && el.children.length===0)el.style.display='none';
    });
  }
  compactSearch();
  document.addEventListener('click',()=>setTimeout(compactSearch,0));
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
