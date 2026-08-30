def apply(legacy):
    patch = r'''<style>
/* Search page must start immediately next to the permanent navigation. */
#searchPage{padding-top:0!important;margin-top:0!important}
#searchPage>h2{margin:0 0 4px!important}
#searchPage>.subtitle{margin:0 0 10px!important}
#searchPage .search-center{gap:9px!important}
#searchPage .search-card{padding:11px 12px!important}
#searchPage .search-card h3{margin:0 0 6px!important;font-size:16px!important}
#searchPage .search-results{margin-top:7px!important}
.side{position:sticky!important;top:12px!important;align-self:start!important;height:max-content!important;z-index:10!important}
@media(min-width:721px){.workspace{grid-template-columns:118px minmax(0,1fr)!important;gap:12px!important}.diamond-button{width:96px!important;height:96px!important}.diamond{width:68px!important;height:68px!important;margin:14px auto!important}.diamond-inner{width:88px!important;font-size:12px!important}}
</style>
<script>
(function(){
  function fixSearchLayout(){
    const p=document.getElementById('searchPage');
    const content=document.querySelector('.content');
    if(!p||!content)return;
    /* search_patch is appended after legacy's </main>; move it into the real content panel. */
    if(p.parentElement!==content) content.appendChild(p);
    /* Hide any legacy empty box that was occupying the large white rectangle. */
    Array.from(content.children).forEach(el=>{
      if(el===p)return;
      if(el.classList.contains('page') && el.classList.contains('active') && el.id!=='searchPage')el.classList.remove('active');
    });
  }
  const oldOpen=window.openSearchCenter;
  window.openSearchCenter=function(){
    if(oldOpen)oldOpen();
    fixSearchLayout();
    document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));
    const p=document.getElementById('searchPage');if(p)p.classList.add('active');
    window.scrollTo({top:0,left:0,behavior:'auto'});
  };
  fixSearchLayout();
  document.addEventListener('click',()=>setTimeout(fixSearchLayout,0));
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
