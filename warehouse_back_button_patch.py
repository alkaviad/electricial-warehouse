def apply(legacy):
    # The redundant button has the fixed id warehouseBack in legacy.py.
    # Hide it directly instead of depending on its translated text or class name.
    patch = r'''<style>
#warehouseBack{display:none!important}
</style>
<script>
(function(){
  function hideWarehouseBack(){
    const b=document.getElementById('warehouseBack');
    if(b){b.style.setProperty('display','none','important');b.hidden=true;}
  }
  hideWarehouseBack();
  document.addEventListener('DOMContentLoaded',hideWarehouseBack);
  document.addEventListener('click',()=>setTimeout(hideWarehouseBack,0));
  setTimeout(hideWarehouseBack,100);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
