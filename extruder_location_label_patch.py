def apply(legacy):
    patch = r'''<script>
(function(){
function extruderLocationText(m){
  m=String(m||'').trim();
  if(/^(Line|שורה|Шура|Строка|Экструдер|Extruder)\s*4$/i.test(m)) return lang==='he'?'אקסטרודר 4':lang==='en'?'Extruder 4':'Экструдер 4';
  if(/^(Line|שורה|Шура|Строка|Экструдер|Extruder)\s*5$/i.test(m)) return lang==='he'?'אקסטרודר 5':lang==='en'?'Extruder 5':'Экструдер 5';
  return null;
}
function fixExtruderLabels(){
  let changed=false;
  inventory.forEach(x=>{
    if(x.cat!=='plc_modules' && x.cat!=='drives_control') return;
    let fixed=extruderLocationText(x.machine);
    if(fixed && x.machine!==fixed){x.machine=fixed;changed=true}
  });
  if(changed) try{localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory))}catch(e){}
}
window.fixExtruderLabels=fixExtruderLabels;
window.extruderLocationText=extruderLocationText;
fixExtruderLabels();
const oldRender=window.renderWarehouseItems;
window.renderWarehouseItems=function(){fixExtruderLabels();oldRender();setTimeout(()=>{document.querySelectorAll('#warehouseItemsBody tr').forEach(row=>{let cell=row.querySelector('.tr-machine');if(!cell)return;let fixed=extruderLocationText(cell.textContent);if(fixed)cell.textContent=fixed})},0)};
document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(()=>{fixExtruderLabels();if(document.getElementById('warehouseCategory')?.classList.contains('active'))window.renderWarehouseItems()},50)));
})();
</script>'''
    legacy.HTML=legacy.HTML.replace('</body>',patch+'</body>')
