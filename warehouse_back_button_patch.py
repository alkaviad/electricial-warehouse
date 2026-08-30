def apply(legacy):
    patch = r'''<style>
/* Main warehouse is already available in the permanent navigation. */
#warehouseCategory .back-btn{display:none!important}
</style>
<script>
(function(){
  function removeRedundantWarehouseBack(){
    const page=document.getElementById('warehouseCategory');
    if(!page)return;
    page.querySelectorAll('button').forEach(b=>{
      const t=(b.textContent||'').trim().toLowerCase();
      if(t.includes('מחסן ראשי')||t.includes('главный склад')||t.includes('main warehouse')){
        b.style.display='none';
      }
    });
  }
  removeRedundantWarehouseBack();
  document.addEventListener('click',()=>setTimeout(removeRedundantWarehouseBack,0));
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
