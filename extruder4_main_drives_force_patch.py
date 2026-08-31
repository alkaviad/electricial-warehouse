import extruder4_main_cabinet_inventory_patch
import extruder4_main_cabinet_full_data_patch

def apply(legacy):
    extruder4_main_cabinet_inventory_patch.apply(legacy)
    extruder4_main_cabinet_full_data_patch.apply(legacy)

    patch = r'''<script>
(function(){
  function stopCabinetBubble(ev){
    var t=ev.target;
    if(t && t.closest && t.closest('#e4MainCabinetInventory')){
      ev.stopPropagation();
    }
  }
  function install(){
    if(document.body && !document.body.__e4CabinetClickFix){
      document.body.__e4CabinetClickFix=true;
      document.body.addEventListener('click', stopCabinetBubble, false);
    }
  }
  install();
  document.addEventListener('DOMContentLoaded', install);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
