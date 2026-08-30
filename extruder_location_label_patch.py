def apply(legacy):
    patch = r'''<script>
(function(){
function fixExtruderLabels(){
  let changed=false;
  inventory.forEach(x=>{
    if(x.cat!=='plc_modules' && x.cat!=='drives_control') return;
    let m=String(x.machine||'').trim();
    if(/^(Line|שורה)\s*4$/i.test(m)){x.machine='Экструдер 4';changed=true}
    if(/^(Line|שורה)\s*5$/i.test(m)){x.machine='Экструдер 5';changed=true}
  });
  if(changed) try{localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory))}catch(e){}
}
fixExtruderLabels();
})();
</script>'''
    legacy.HTML=legacy.HTML.replace('</body>',patch+'</body>')
