def apply(legacy):
    patch = r'''<script>
(function(){
const labels={
 encoders:{ru:'Энкодеры',he:'אנקודרים',en:'Encoders'},
 control_cpu:{ru:'Бакара — CPU / контроллеры',he:'בקרה — CPU / בקרים',en:'Control — CPU / controllers'},
 control_io:{ru:'Бакара — входы / выходы I/O',he:'בקרה — כניסות / יציאות I/O',en:'Control — I/O modules'},
 control_comm:{ru:'Бакара — связь / коммуникация',he:'בקרה — תקשורת',en:'Control — communication'},
 control_expansion:{ru:'Бакара — расширение / интерфейсные модули',he:'בקרה — הרחבה / ממשקים',en:'Control — expansion / interface modules'},
 control_safety:{ru:'Бакара — безопасность',he:'בקרה — בטיחות',en:'Control — safety'},
 control_power:{ru:'Бакара — блоки питания',he:'בקרה — ספקי כוח',en:'Control — power supplies'}
};
Object.assign(categoryLabels,labels);
function text(x){return [x.name,x.specs,x.manufacturer,x.notes].join(' ').toLowerCase()}
function classify(x){
 if(x.cat!=='plc_modules'&&x.cat!=='drives_control')return x.cat;
 let s=text(x), p=String(x.name||'').toUpperCase();
 // Real drives stay only in Drives.
 if(/ACS\d|SINAMICS|MICROMASTER|BSD0200|SERVO|מתנעה תדר|ווסת תדר|FREQUENCY|DRIVE/.test((p+' '+s).toUpperCase()))return 'drives_control';
 // Encoders and encoder/sensor modules are separate.
 if(/ENCODER|אנקוד|absolute incoder|absolute encoder|ssi/.test(s))return 'encoders';
 // Communication networks/interfaces.
 if(/תקשורת|תיקשורת|communication|profinet|profibus|ethernet|anybus|simatic net|6gk|x20 if/.test(s))return 'control_comm';
 // Safety control modules.
 if(/בטיחות|safety|profisafe|xps-ac|cs fs/.test(s))return 'control_safety';
 // Power supplies used by control system.
 if(/ספק כוח|power supply|power$|6ep|ndr-/.test(s))return 'control_power';
 // CPU / PLC / programmable controllers.
 if(/\bcpu\b|בקר ראשי|בקר מתו|בקר מתוכ|programmable|controller|x20 cp|313-|317-/.test(s))return 'control_cpu';
 // Digital/analog I/O modules.
 if(/כניסה|יציאה|input|output|analog|digital|כרטיס אנלוגי|כרטיס דיגיטלי|\bdi\b|\bdo\b|\bai\b|\bao\b/.test(s))return 'control_io';
 // ET200 heads, bases, expansion and other control slots/interfaces.
 if(/et200|הרחבה|ראש בקר|baseunit|base unit|interface|slot|כרטיס/.test(s))return 'control_expansion';
 return x.cat==='drives_control'?'plc_modules':x.cat;
}
let changed=false;
inventory.forEach(x=>{let c=classify(x);if(c!==x.cat){x.cat=c;changed=true}});
if(changed)try{localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory))}catch(e){}
// Ensure new categories are visible as normal warehouse tiles.
const oldMake=window.makeWarehouse;
window.makeWarehouse=function(){
 oldMake();
 const g=document.getElementById('warehouseGrid');if(!g)return;
 Object.keys(labels).forEach(id=>{
   if(g.querySelector('[data-split-cat="'+id+'"]'))return;
   let w=document.createElement('div');w.className='tile-wrap';w.setAttribute('data-split-cat',id);
   let b=document.createElement('button');b.className='warehouse-tile';b.onclick=()=>openWarehouseCategory(id);
   let l=labels[id];b.textContent=l[lang]||l.ru;w.appendChild(b);g.appendChild(w);
 });
};
setTimeout(()=>{try{makeWarehouse()}catch(e){}},0);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
