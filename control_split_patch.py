def apply(legacy):
    patch = r'''<script>
(function(){
const labels={
 encoders:{ru:'Энкодеры',he:'אנקודרים',en:'Encoders'},
 control_cpu:{ru:'Бакара — CPU / контроллеры',he:'בקרה — CPU / בקרים',en:'Control — CPU / controllers'},
 control_io:{ru:'Бакара — входы / выходы I/O',he:'בקרה — כניסות / יציאות I/O',en:'Control — I/O modules'}
};
Object.assign(categoryLabels,labels);
const obsolete=['control_comm','control_expansion','control_safety','control_power','plc_modules'];
function text(x){return [x.name,x.specs,x.manufacturer,x.notes].join(' ').toLowerCase()}
function classify(x){
 let s=text(x), p=String(x.name||'').toUpperCase(), all=(p+' '+s).toUpperCase();
 if(x.cat==='control_power')return 'power_supplies';
 if(x.cat==='control_comm'||x.cat==='control_expansion'||x.cat==='control_safety')return 'control_io';
 if(x.cat!=='plc_modules'&&x.cat!=='drives_control'&&x.cat!=='control_cpu'&&x.cat!=='control_io'&&x.cat!=='encoders')return x.cat;
 if(/ACS\d|SINAMICS|MICROMASTER|BSD0200|SERVO|מתנעה תדר|ווסת תדר|FREQUENCY|DRIVE/.test(all))return 'drives_control';
 if(/ENCODER|אנקוד|absolute incoder|absolute encoder/.test(s))return 'encoders';
 if(/ספק כוח|power supply|6ep|ndr-/.test(s))return 'power_supplies';
 if(/\bcpu\b|בקר ראשי|בקר מתו|בקר מתוכ|programmable|controller|x20 cp|313-|317-/.test(s))return 'control_cpu';
 return 'control_io';
}
let changed=false;
inventory.forEach(x=>{let c=classify(x);if(c!==x.cat){x.cat=c;changed=true}});
if(changed)try{localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory))}catch(e){}
const oldMake=window.makeWarehouse;
window.makeWarehouse=function(){
 oldMake();
 const g=document.getElementById('warehouseGrid');if(!g)return;

 // Remove categories the user no longer wants and all old split-control tiles.
 const removeText=[
  'מגעים','контакты','contacts',
  'כבלים וחוטים','кабели и провода','cables and wires',
  'כניסות כבל','кабельные вводы','cable glands',
  'פנאומטיקה / שסתומים','פנאומטיקה','שסתומים','пневматика','клапаны','pneumatics','valves'
 ];
 Array.from(g.querySelectorAll('.warehouse-tile')).forEach(b=>{
   let t=(b.textContent||'').trim().toLowerCase();
   if(removeText.some(x=>t.includes(x.toLowerCase()))){(b.closest('.tile-wrap')||b).remove();return;}
   // Remove every legacy duplicate of CPU, I/O and encoders. Canonical tiles are added below.
   if(t.includes('cpu')||t.includes('i/o')||t.includes('אנקוד')||t.includes('энкод')||t.includes('encoder')||t==='בקרה'||t.includes('plc')){
     (b.closest('.tile-wrap')||b).remove();
   }
 });
 obsolete.forEach(id=>g.querySelectorAll('[data-split-cat="'+id+'"]').forEach(e=>e.remove()));
 // Ensure only one canonical tile for each retained control category.
 Object.keys(labels).forEach(id=>{
   g.querySelectorAll('[data-split-cat="'+id+'"]').forEach(e=>e.remove());
   let w=document.createElement('div');w.className='tile-wrap';w.setAttribute('data-split-cat',id);
   let b=document.createElement('button');b.className='warehouse-tile';b.onclick=()=>openWarehouseCategory(id);
   let l=labels[id];b.textContent=l[lang]||l.ru;w.appendChild(b);g.appendChild(w);
 });
};
setTimeout(()=>{try{makeWarehouse()}catch(e){}},0);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
