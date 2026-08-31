def apply(legacy):
    patch = r'''<script>
(function(){
const labels={
 encoders:{ru:'Энкодеры',he:'אנקודרים',en:'Encoders'},
 control_cpu:{ru:'Бакара — CPU / контроллеры',he:'בקרה — CPU / בקרים',en:'Control — CPU / controllers'},
 control_io:{ru:'Бакара — входы / выходы I/O',he:'בקרה — כניסות / יציאות I/O',en:'Control — I/O modules'}
};
Object.assign(categoryLabels,labels);
const obsolete=['control_comm','control_expansion','control_safety','control_power'];
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
 // Remove old duplicate control tiles created by earlier versions.
 obsolete.concat(['plc_modules']).forEach(id=>{
   g.querySelectorAll('[data-split-cat="'+id+'"]').forEach(e=>e.remove());
 });
 Object.keys(labels).forEach(id=>{
   if(g.querySelector('[data-split-cat="'+id+'"]'))return;
   let w=document.createElement('div');w.className='tile-wrap';w.setAttribute('data-split-cat',id);
   let b=document.createElement('button');b.className='warehouse-tile';b.onclick=()=>openWarehouseCategory(id);
   let l=labels[id];b.textContent=l[lang]||l.ru;w.appendChild(b);g.appendChild(w);
 });
 // Hide legacy PLC/control tile when it still exists in the original grid.
 Array.from(g.querySelectorAll('.warehouse-tile')).forEach(b=>{
   let t=(b.textContent||'').toLowerCase();
   if((t.includes('plc')&&t.includes('i/o'))||t==='בקרה' || t==='контроллеры / plc'){
     let w=b.closest('.tile-wrap')||b;w.style.display='none';
   }
 });
};
setTimeout(()=>{try{makeWarehouse()}catch(e){}},0);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
