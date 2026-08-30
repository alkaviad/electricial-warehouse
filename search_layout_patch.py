def apply(legacy):
    patch = r'''<style>
/* Compact search layout and permanent navigation. */
#searchPage{padding-top:0!important;margin-top:0!important}
#searchPage>h2{margin:0 0 4px!important}
#searchPage>.subtitle{margin:0 0 10px!important}
#searchPage .search-center{gap:9px!important}
#searchPage .search-card{padding:11px 12px!important}
#searchPage .search-card h3{margin:0 0 6px!important;font-size:16px!important}
#searchPage .search-results{margin-top:7px!important}
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
  function normalizePages(){
    const content=document.querySelector('.content');
    if(!content)return;
    /* Several feature patches append their pages after </main>.
       Move every application page into the real content panel so the
       large empty panel can never remain above the active page. */
    document.querySelectorAll('.page').forEach(p=>{
      if(p.parentElement!==content)content.appendChild(p);
    });
  }

  normalizePages();
  document.addEventListener('DOMContentLoaded',normalizePages);

  const oldShow=window.showPage;
  if(oldShow){
    window.showPage=function(id){
      normalizePages();
      return oldShow(id);
    };
  }

  const oldSearch=window.openSearchCenter;
  if(oldSearch){
    window.openSearchCenter=function(){
      normalizePages();
      return oldSearch();
    };
  }
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
