import legacy
import machine_parts_patch
import search_patch
import extruder_location_label_patch
import control_split_patch
import drawing_number_patch
import warehouse_back_button_patch
import sticky_sidebar_patch
import search_layout_patch
import drawings_patch
import extruder4_drawing_structure_patch
import extruder4_equipment_details_patch
import extruder4_installation_split_patch
import extruder4_main_drives_force_patch
import extruder4_station_category_patch
import extruder5_drawing_data_patch
import extruder5_station_category_patch
import extruder5_calender_isolation_patch
import extruder5_extruder_b_patch
import extruder5_extruder_a_patch

PATCH = r'''<style>
.qty-control{display:flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap}.qty-control button{width:36px;height:36px;border:1px solid #aebfc1;border-radius:8px;background:#eef5f3;color:#34454b;font-size:22px;font-weight:700;cursor:pointer}.qty-control .qnum{min-width:42px;text-align:center;font-size:17px;font-weight:700}.warehouse-main-add{display:inline-block;margin:0 0 12px;padding:11px 16px;border:0;border-radius:9px;background:#527d83;color:#fff;font-size:15px;font-weight:700;cursor:pointer}.category-add{display:inline-block;margin:0 0 14px}.warehouse-grid .custom-cat{position:relative}.warehouse-grid .custom-cat .cat-delete{position:absolute;top:3px;right:3px;width:24px;height:24px;border:0;border-radius:50%;background:#fff;color:#777;cursor:pointer;display:none}.owner-mode .warehouse-grid .custom-cat .cat-delete{display:block}#addItemBtn{display:none!important}.item-actions button{cursor:pointer}.internal-code{font-weight:700;white-space:nowrap}
</style>
<script>
(function(){
  document.documentElement.setAttribute('translate','no');document.body.classList.add('notranslate');
  const CACHE_KEY='warehouse_translation_cache_clean_v2';let trCache={};try{trCache=JSON.parse(localStorage.getItem(CACHE_KEY)||'{}')}catch(e){}let renderToken=0;
  function saveCache(){try{localStorage.setItem(CACHE_KEY,JSON.stringify(trCache))}catch(e){}}
  function looksLikePartNumber(s){if(!s)return true;return /\d/.test(s)&&/[A-Za-zА-Яа-яא-ת]/.test(s)&&!(/\s/.test(s))}
  async function tr(text,target){text=(text||'').trim();if(!text||looksLikePartNumber(text))return text;let key=target+'|'+text;if(trCache[key])return trCache[key];try{let u='https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl='+target+'&dt=t&q='+encodeURIComponent(text),r=await fetch(u);if(!r.ok)return text;let j=await r.json(),out=(j[0]||[]).map(x=>x[0]).join('').trim()||text;trCache[key]=out;saveCache();return out}catch(e){return text}}
  function staticTerm(text,target){const d={'בסיס לממסרים':{ru:'Колодка реле',he:'בסיס לממסרים',en:'Relay socket'},'בסיס ממסר':{ru:'Колодка реле',he:'בסיס ממסר',en:'Relay socket'},'ממסר צעד':{ru:'Импульсное реле',he:'ממסר צעד',en:'Impulse relay'},'פחת':{ru:'УЗО',he:'פחת',en:'RCD'},'מאמ׳׳ת':{ru:'Автоматический выключатель',he:'מאמ״ת',en:'Circuit breaker'},'מאמ״ת':{ru:'Автоматический выключатель',he:'מאמ״ת',en:'Circuit breaker'},'למנוע':{ru:'для двигателя',he:'למנוע',en:'for motor'}};let out=text||'';Object.keys(d).forEach(k=>out=out.split(k).join(d[k][target]||k));return out}
  async function displayText(text,target,kind){let s=staticTerm(text,target);if(!s||looksLikePartNumber(s))return s;if(kind==='name'){let chunks=s.split(/(\b[A-Z0-9][A-Z0-9._+\/-]*\d[A-Z0-9._+\/-]*\b)/gi),out=[];for(const c of chunks){if(!c||(/\d/.test(c)&&!/\s/.test(c)))out.push(c);else out.push(await tr(c,target))}return out.join('')}return await tr(s,target)}
  inventory.forEach(x=>{if(x.qty===''||x.qty===null||typeof x.qty==='undefined')x.qty=0;else{x.qty=Number(x.qty);if(!Number.isFinite(x.qty)||x.qty<0)x.qty=0}if(typeof x.internalCode==='undefined')x.internalCode=''});try{localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory))}catch(e){}
  const modal=document.querySelector('#warehouseEditModal .modal-card');if(modal&&!document.getElementById('wiInternalCode')){let modelLabel=document.getElementById('wlModel'),lab=document.createElement('label'),inp=document.createElement('input');lab.id='wlInternalCode';inp.id='wiInternalCode';inp.autocomplete='off';modal.insertBefore(lab,modelLabel);modal.insertBefore(inp,modelLabel)}
  const headRow=document.querySelector('#warehouseCategory thead tr');if(headRow&&!document.getElementById('thInternalCode')){let th=document.createElement('th');th.id='thInternalCode';headRow.insertBefore(th,headRow.firstChild)}
  function syncExtraTexts(){const c=document.getElementById('addCategoryBtn'),a=document.getElementById('warehouseMainAdd'),lc=document.getElementById('wlInternalCode'),hc=document.getElementById('thInternalCode');if(c)c.textContent=lang==='he'?'+ טבלה חדשה':lang==='en'?'+ New table':'+ Новая таблица';if(a)a.textContent=lang==='he'?'+ הוסף פריט חדש':lang==='en'?'+ Add new item':'+ Добавить новую позицию';if(lc)lc.textContent=lang==='he'?'קוד מחסן / קוד פנימי':lang==='en'?'Warehouse / internal code':'Код склада / внутренний код';if(hc)hc.textContent=lang==='he'?'קוד מחסן':lang==='en'?'Warehouse code':'Код склада'}
  window.changeWarehouseQty=function(i,delta){let x=inventory[i];if(!x)return;x.qty=Math.max(0,(Number(x.qty)||0)+delta);localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory));renderWarehouseItems()}
  window.openWarehouseEdit=function(i){currentWarehouseEditIndex=i;let x=i>=0?inventory[i]:{cat:currentWarehouseCat,internalCode:'',name:'',manufacturer:'',specs:'',qty:0,machine:'',price:'',notes:''};warehouseEditTitle.textContent=T[lang].editItem;document.getElementById('wiInternalCode').value=x.internalCode||'';wiModel.value=x.name||'';wiManufacturer.value=x.manufacturer||'';wiSpecs.value=x.specs||'';wiQty.value=x.qty??0;wiMachine.value=x.machine||'';wiPrice.value=x.price||'';wiNotes.value=x.notes||'';syncExtraTexts();warehouseEditModal.classList.add('open')}
  window.saveWarehouseItem=function(){let obj={cat:currentWarehouseCat,internalCode:document.getElementById('wiInternalCode').value.trim(),name:wiModel.value.trim(),manufacturer:wiManufacturer.value.trim(),specs:wiSpecs.value.trim(),qty:wiQty.value===''?0:Math.max(0,Number(wiQty.value)||0),machine:wiMachine.value.trim(),price:wiPrice.value===''?'':Number(wiPrice.value),notes:wiNotes.value.trim(),source:'manual'};if(!obj.name)return;if(currentWarehouseEditIndex>=0)inventory[currentWarehouseEditIndex]=obj;else inventory.push(obj);localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory));warehouseEditModal.classList.remove('open');populateManufacturers();renderWarehouseItems()}
  const customKey='warehouse_custom_categories_v1';function loadCats(){try{return JSON.parse(localStorage.getItem(customKey)||'[]')}catch(e){return[]}}function saveCats(a){localStorage.setItem(customKey,JSON.stringify(a))}function catName(c){return c[lang]||c.ru||c.he||c.en||''}
  window.addWarehouseCategory=async function(){let base=prompt(lang==='he'?'שם הקטגוריה החדשה:':lang==='en'?'New table/category name:':'Название новой таблицы / категории:');if(!base||!base.trim())return;base=base.trim();let ru=base,he=base,en=base;try{if(lang!=='ru')ru=await tr(base,'ru');if(lang!=='he')he=await tr(base,'he');if(lang!=='en')en=await tr(base,'en')}catch(e){}let a=loadCats(),id='custom_'+Date.now();a.push({id,ru,he,en});saveCats(a);makeWarehouse()}
  window.deleteWarehouseCategory=function(id){if(!ownerUnlocked)return;let msg=lang==='he'?'למחוק את הקטגוריה? הפריטים שבתוכה יימחקו.':lang==='en'?'Delete this category? Its items will also be deleted.':'Удалить эту таблицу? Позиции внутри неё тоже удалятся.';if(!confirm(msg))return;saveCats(loadCats().filter(c=>c.id!==id));inventory=inventory.filter(x=>x.cat!==id);localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory));makeWarehouse();showPage('stock')}
  const originalMakeWarehouse=window.makeWarehouse;window.makeWarehouse=function(){originalMakeWarehouse();loadCats().forEach(c=>{categoryLabels[c.id]={ru:c.ru,he:c.he,en:c.en};warehouseGrid.insertAdjacentHTML('beforeend',`<div class="custom-cat"><button class="warehouse-tile" onclick="openWarehouseCategory('${c.id}')">${esc(catName(c))}</button><button class="cat-delete" onclick="event.stopPropagation();deleteWarehouseCategory('${c.id}')">×</button></div>`)});syncExtraTexts()}
  let stock=document.getElementById('stock');if(stock&&!document.getElementById('addCategoryBtn')){let b=document.createElement('button');b.id='addCategoryBtn';b.className='small-btn category-add';b.onclick=addWarehouseCategory;stock.insertBefore(b,document.getElementById('warehouseGrid'))}let catPage=document.getElementById('warehouseCategory');if(catPage&&!document.getElementById('warehouseMainAdd')){let b=document.createElement('button');b.id='warehouseMainAdd';b.className='warehouse-main-add';b.onclick=()=>openWarehouseEdit(-1);let controls=catPage.querySelector('.warehouse-controls');catPage.insertBefore(b,controls)}
  window.renderWarehouseItems=function(){if(!currentWarehouseCat)return;const token=++renderToken,target=lang;const q=(warehouseSearch.value||'').toLowerCase(),mf=manufacturerFilter.value||'';const rows=inventory.map((x,i)=>({x,i})).filter(o=>o.x.cat===currentWarehouseCat).filter(o=>!mf||o.x.manufacturer===mf).filter(o=>!q||[o.x.internalCode,o.x.name,o.x.manufacturer,o.x.specs,o.x.machine,o.x.notes].join(' ').toLowerCase().includes(q));warehouseItemsBody.innerHTML=rows.map(o=>`<tr data-widx="${o.i}"><td class="internal-code">${esc(o.x.internalCode||'')}</td><td><b class="tr-name">${esc(o.x.name)}</b></td><td>${esc(o.x.manufacturer)}</td><td class="tr-specs">${esc(o.x.specs)}</td><td class="qty"><div class="qty-control"><button title="−1" onclick="changeWarehouseQty(${o.i},-1)">−</button><span class="qnum">${esc(String(o.x.qty??0))}</span><button title="+1" onclick="changeWarehouseQty(${o.i},1)">+</button></div></td><td class="tr-machine">${esc(o.x.machine||'')}</td><td>${o.x.price?esc(String(o.x.price)):''}</td><td class="item-actions"><button onclick="openWarehouseEdit(${o.i})">✎</button><button class="owner-only" onclick="deleteWarehouseItem(${o.i})">×</button></td></tr>`).join('');syncExtraTexts();rows.forEach(async o=>{const row=warehouseItemsBody.querySelector(`tr[data-widx="${o.i}"]`);if(!row)return;const[n,s,m]=await Promise.all([displayText(o.x.name,target,'name'),displayText(o.x.specs,target,'specs'),displayText(o.x.machine||'',target,'machine')]);if(token!==renderToken||target!==lang||!row.isConnected)return;const ne=row.querySelector('.tr-name'),se=row.querySelector('.tr-specs'),me=row.querySelector('.tr-machine');if(ne)ne.textContent=n;if(se)se.textContent=s;if(me)me.textContent=m})};
  document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(()=>{renderToken++;syncExtraTexts();if(document.getElementById('warehouseCategory').classList.contains('active'))renderWarehouseItems()},0)));syncExtraTexts();makeWarehouse();
})();
</script>'''
NO_TRANSLATE = r'''<meta name="google" content="notranslate"><meta name="robots" content="notranslate">'''
legacy.HTML = legacy.HTML.replace('</head>', NO_TRANSLATE + '</head>')
legacy.HTML = legacy.HTML.replace('</body>', PATCH + '</body>')
extruder_location_label_patch.apply(legacy)
control_split_patch.apply(legacy)
machine_parts_patch.apply(legacy)
drawing_number_patch.apply(legacy)
warehouse_back_button_patch.apply(legacy)
sticky_sidebar_patch.apply(legacy)
search_patch.apply(legacy)
search_layout_patch.apply(legacy)
drawings_patch.apply(legacy)
extruder4_drawing_structure_patch.apply(legacy)
extruder4_equipment_details_patch.apply(legacy)
extruder4_installation_split_patch.apply(legacy)
extruder4_main_drives_force_patch.apply(legacy)
extruder4_station_category_patch.apply(legacy)
extruder5_drawing_data_patch.apply(legacy)
extruder5_station_category_patch.apply(legacy)
extruder5_calender_isolation_patch.apply(legacy)
extruder5_extruder_b_patch.apply(legacy)
extruder5_extruder_a_patch.apply(legacy)
app = legacy.app
if __name__ == '__main__': app.run(debug=True)
