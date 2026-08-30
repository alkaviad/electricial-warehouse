import legacy

WAREHOUSE_FIX = r'''<style>
.qty-control{display:flex;align-items:center;justify-content:center;gap:5px;white-space:nowrap}.qty-control button{width:30px;height:30px;border:1px solid #bcc9ca;border-radius:7px;background:#eef5f3;font-size:18px;font-weight:700;cursor:pointer}.qty-control .qnum{min-width:34px;text-align:center;font-size:15px}.category-add{margin:0 0 14px;display:none}.owner-mode .category-add{display:inline-block}.warehouse-grid .custom-cat{position:relative}.warehouse-grid .custom-cat .cat-delete{position:absolute;top:3px;right:3px;width:24px;height:24px;border:0;border-radius:50%;background:#fff;color:#777;cursor:pointer;display:none}.owner-mode .warehouse-grid .custom-cat .cat-delete{display:block}
</style>
<script>
(function(){
 const CACHE_KEY='warehouse_translation_cache_v2';
 let trCache={};try{trCache=JSON.parse(localStorage.getItem(CACHE_KEY)||'{}')}catch(e){}
 function saveCache(){try{localStorage.setItem(CACHE_KEY,JSON.stringify(trCache))}catch(e){}}
 function looksLikePartNumber(s){if(!s)return true;return /\d/.test(s)&&/[A-Za-zА-Яа-яא-ת]/.test(s)&&!(/\s/.test(s))}
 async function tr(text,target){text=(text||'').trim();if(!text||looksLikePartNumber(text))return text;let key=target+'|'+text;if(trCache[key])return trCache[key];try{let u='https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl='+target+'&dt=t&q='+encodeURIComponent(text),r=await fetch(u);if(!r.ok)return text,j=await r.json(),out=(j[0]||[]).map(x=>x[0]).join('').trim()||text;trCache[key]=out;saveCache();return out}catch(e){return text}}
 function staticTerm(text,target){const d={'בסיס לממסרים':{ru:'Колодка реле',he:'בסיס לממסרים',en:'Relay socket'},'בסיס ממסר':{ru:'Колодка реле',he:'בסיס ממסר',en:'Relay socket'},'ממסר צעד':{ru:'Импульсное реле',he:'ממסר צעד',en:'Impulse relay'},'פחת':{ru:'УЗО',he:'פחת',en:'RCD'},'מאמ׳׳ת':{ru:'Автоматический выключатель',he:'מאמ״ת',en:'Circuit breaker'},'מאמ״ת':{ru:'Автоматический выключатель',he:'מאמ״ת',en:'Circuit breaker'},'למנוע':{ru:'для двигателя',he:'למנוע',en:'for motor'}};let out=text||'';Object.keys(d).forEach(k=>out=out.split(k).join(d[k][target]||k));return out}
 async function displayText(text,target,kind){let s=staticTerm(text,target);if(!s||looksLikePartNumber(s))return s;if(kind==='name'){let chunks=s.split(/(\b[A-Z0-9][A-Z0-9._+\/-]*\d[A-Z0-9._+\/-]*\b)/gi),out=[];for(const c of chunks){if(!c||(/\d/.test(c)&&!/\s/.test(c)))out.push(c);else out.push(await tr(c,target))}return out.join('')}return await tr(s,target)}

 // Keep quantities as real stock numbers. Blank imported quantities become 0 until counted.
 inventory.forEach(x=>{if(x.qty===''||x.qty===null||typeof x.qty==='undefined')x.qty=0;else{x.qty=Number(x.qty);if(!Number.isFinite(x.qty)||x.qty<0)x.qty=0}});
 try{localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory))}catch(e){}

 window.changeWarehouseQty=function(i,delta){if(!ownerUnlocked)return;let x=inventory[i];if(!x)return;let n=Number(x.qty)||0;n=Math.max(0,n+delta);x.qty=n;localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory));renderWarehouseItems()}

 const customKey='warehouse_custom_categories_v1';
 function loadCats(){try{return JSON.parse(localStorage.getItem(customKey)||'[]')}catch(e){return[]}}
 function saveCats(a){localStorage.setItem(customKey,JSON.stringify(a))}
 function catName(c){return c[lang]||c.ru||c.he||c.en||''}
 window.addWarehouseCategory=async function(){if(!ownerUnlocked)return;let base=prompt(lang==='he'?'שם הקטגוריה החדשה:':lang==='en'?'New table/category name:':'Название новой таблицы / категории:');if(!base||!base.trim())return;base=base.trim();let sourceLang=lang,ru=base,he=base,en=base;try{if(sourceLang!=='ru')ru=await tr(base,'ru');if(sourceLang!=='he')he=await tr(base,'he');if(sourceLang!=='en')en=await tr(base,'en')}catch(e){}let a=loadCats(),id='custom_'+Date.now();a.push({id,ru,he,en});saveCats(a);makeWarehouse()}
 window.deleteWarehouseCategory=function(id){if(!ownerUnlocked)return;let msg=lang==='he'?'למחוק את הקטגוריה? הפריטים שבתוכה יימחקו.':lang==='en'?'Delete this category? Its items will also be deleted.':'Удалить эту таблицу? Позиции внутри неё тоже удалятся.';if(!confirm(msg))return;saveCats(loadCats().filter(c=>c.id!==id));inventory=inventory.filter(x=>x.cat!==id);localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory));makeWarehouse();showPage('stock')}
 const oldMakeWarehouse=window.makeWarehouse;
 window.makeWarehouse=function(){oldMakeWarehouse();let a=loadCats();a.forEach(c=>{categoryLabels[c.id]={ru:c.ru,he:c.he,en:c.en};warehouseGrid.insertAdjacentHTML('beforeend',`<div class="custom-cat"><button class="warehouse-tile" onclick="openWarehouseCategory('${c.id}')">${esc(catName(c))}</button><button class="cat-delete" onclick="event.stopPropagation();deleteWarehouseCategory('${c.id}')">×</button></div>`)})}

 let stock=document.getElementById('stock');if(stock&&!document.getElementById('addCategoryBtn')){let b=document.createElement('button');b.id='addCategoryBtn';b.className='small-btn category-add';b.onclick=addWarehouseCategory;stock.insertBefore(b,document.getElementById('warehouseGrid'))}
 function setAddCatText(){let b=document.getElementById('addCategoryBtn');if(b)b.textContent=lang==='he'?'+ טבלה חדשה':lang==='en'?'+ New table':'+ Новая таблица'}

 window.renderWarehouseItems=function(){if(!currentWarehouseCat)return;let q=(warehouseSearch.value||'').toLowerCase(),mf=manufacturerFilter.value||'';let rows=inventory.map((x,i)=>({x,i})).filter(o=>o.x.cat===currentWarehouseCat).filter(o=>!mf||o.x.manufacturer===mf).filter(o=>!q||[o.x.name,o.x.manufacturer,o.x.specs,o.x.machine,o.x.notes].join(' ').toLowerCase().includes(q));warehouseItemsBody.innerHTML=rows.map(o=>`<tr data-widx="${o.i}"><td><b class="tr-name">${esc(o.x.name)}</b></td><td>${esc(o.x.manufacturer)}</td><td class="tr-specs">${esc(o.x.specs)}</td><td class="qty"><div class="qty-control"><button class="owner-only" onclick="changeWarehouseQty(${o.i},-1)">−</button><span class="qnum">${esc(String(o.x.qty??0))}</span><button class="owner-only" onclick="changeWarehouseQty(${o.i},1)">+</button></div></td><td class="tr-machine">${esc(o.x.machine||'')}</td><td>${o.x.price?esc(String(o.x.price)):''}</td><td class="item-actions owner-only"><button onclick="openWarehouseEdit(${o.i})">✎</button><button onclick="deleteWarehouseItem(${o.i})">×</button></td></tr>`).join('');let target=lang;rows.forEach(async o=>{let row=warehouseItemsBody.querySelector(`tr[data-widx="${o.i}"]`);if(!row)return;let[n,s,m]=await Promise.all([displayText(o.x.name,target,'name'),displayText(o.x.specs,target,'specs'),displayText(o.x.machine||'',target,'machine')]);if(!row.isConnected)return;let ne=row.querySelector('.tr-name'),se=row.querySelector('.tr-specs'),me=row.querySelector('.tr-machine');if(ne)ne.textContent=n;if(se)se.textContent=s;if(me)me.textContent=m})}

 // Existing manual item form already stores model, manufacturer, specs, quantity, machine, price and notes.
 // Translate its labels and newly entered human-readable values through the same display translator.
 const oldSetLang=window.setLang;
 window.setLang=function(l){oldSetLang(l);setAddCatText();makeWarehouse()}
 setAddCatText();makeWarehouse();
})();
</script>'''

legacy.HTML = legacy.HTML.replace('</body>', WAREHOUSE_FIX + '</body>')
app = legacy.app

if __name__ == '__main__':
    app.run(debug=True)
