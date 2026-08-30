def apply(legacy):
    patch = r'''<style>
.machine-parts-add{display:inline-block;margin:12px 0;padding:10px 15px;border:0;border-radius:9px;background:#527d83;color:#fff;font-weight:700;cursor:pointer}.machine-parts-wrap{overflow:auto;border:1px solid #ccd7d8;border-radius:10px;background:#fff;margin-top:10px}.machine-parts-wrap table{min-width:860px}.machine-parts-actions button{padding:4px 7px;cursor:pointer}.machine-parts-empty{padding:18px;color:#718087}.machine-parts-link{margin-top:14px;min-height:68px}.machine-parts-modal label{display:block;font-weight:700;margin:10px 0 4px}.machine-parts-modal input,.machine-parts-modal textarea{width:100%;padding:10px;border:1px solid #ccd7d8;border-radius:8px;background:#fbfdfc}.machine-parts-modal textarea{min-height:70px}
</style>
<div class="page" id="machinePartsPage"><button class="back" id="machinePartsBack"></button><h2 id="machinePartsTitle"></h2><button class="machine-parts-add" id="machinePartsAdd" onclick="openMachinePartEdit(-1)"></button><div class="machine-parts-wrap"><table><thead><tr><th id="mpThCode"></th><th id="mpThModel"></th><th id="mpThMfr"></th><th id="mpThSpecs"></th><th id="mpThQty"></th><th id="mpThPrice"></th><th id="mpThNotes"></th><th id="mpThEdit"></th></tr></thead><tbody id="machinePartsBody"></tbody></table></div></div>
<div class="modal" id="machinePartModal"><div class="modal-card machine-parts-modal"><h3 id="machinePartModalTitle"></h3><label id="mpLCode"></label><input id="mpCode"><label id="mpLModel"></label><input id="mpModel"><label id="mpLMfr"></label><input id="mpMfr"><label id="mpLSpecs"></label><textarea id="mpSpecs"></textarea><label id="mpLQty"></label><input id="mpQty" type="number" min="0" step="1"><label id="mpLPrice"></label><input id="mpPrice" type="number" step="0.01"><label id="mpLNotes"></label><textarea id="mpNotes"></textarea><div class="modal-actions"><button class="modal-btn" id="mpCancel" onclick="closeMachinePartEdit()"></button><button class="modal-btn primary" id="mpSave" onclick="saveMachinePart()"></button></div></div></div>
<script>
(function(){
 const KEY='machine_parts_v1';
 let ctx=null, editIndex=-1;
 function load(){try{return JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){return{}}}
 function save(v){localStorage.setItem(KEY,JSON.stringify(v))}
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function e(s){return esc(String(s??''))}
 function machineName(){return (machines[lang]&&machines[lang][currentMachineIndex])||''}
 function ctxTitle(){
   if(!ctx)return'';
   if(ctx.type==='thermo')return machineName()+' — '+thermoSections[lang][ctx.section];
   if(ctx.type==='extruder')return machineName()+' — '+extruderSections[lang][ctx.section];
   return machineName();
 }
 function keyFor(c){return c.type+':'+c.machine+(c.section===null?'':':'+c.section)}
 function items(){let d=load();return d[keyFor(ctx)]||[]}
 function store(a){let d=load();d[keyFor(ctx)]=a;save(d)}
 function syncText(){
   if(!ctx)return;
   machinePartsTitle.textContent=ctxTitle()+' — '+tx('Электрические части','חלקי חשמל','Electrical parts');
   machinePartsAdd.textContent=tx('+ Добавить новую позицию','+ הוסף פריט חדש','+ Add new item');
   machinePartsBack.textContent=tx('← Назад','← חזרה','← Back');
   mpThCode.textContent=tx('Код','קוד','Code'); mpThModel.textContent=tx('Модель / артикул','דגם / מק״ט','Model / part no.'); mpThMfr.textContent=tx('Фирма','יצרן','Manufacturer'); mpThSpecs.textContent=tx('Параметры','נתונים','Specifications'); mpThQty.textContent=tx('Количество','כמות','Quantity'); mpThPrice.textContent=tx('Цена','מחיר','Price'); mpThNotes.textContent=tx('Примечание','הערה','Notes'); mpThEdit.textContent=tx('Изменение','עריכה','Edit');
   mpLCode.textContent=tx('Код склада / внутренний код','קוד מחסן / קוד פנימי','Warehouse / internal code'); mpLModel.textContent=tx('Модель / артикул','דגם / מק״ט','Model / part no.'); mpLMfr.textContent=tx('Фирма','יצרן','Manufacturer'); mpLSpecs.textContent=tx('Параметры','נתונים','Specifications'); mpLQty.textContent=tx('Количество на этом узле','כמות ביחידה הזאת','Quantity on this section'); mpLPrice.textContent=tx('Цена','מחיר','Price'); mpLNotes.textContent=tx('Примечание','הערה','Notes'); mpCancel.textContent=tx('Отмена','ביטול','Cancel'); mpSave.textContent=tx('Сохранить','שמור','Save');
 }
 window.renderMachineParts=function(){if(!ctx)return;syncText();let a=items();machinePartsBody.innerHTML=a.length?a.map((x,i)=>`<tr><td><b>${e(x.code)}</b></td><td>${e(x.model)}</td><td>${e(x.mfr)}</td><td>${e(x.specs)}</td><td class="qty">${e(x.qty)}</td><td>${x.price!==''?e(x.price):''}</td><td>${e(x.notes)}</td><td class="machine-parts-actions"><button onclick="openMachinePartEdit(${i})">✎</button></td></tr>`).join(''):`<tr><td colspan="8" class="machine-parts-empty">${tx('Пока ничего не добавлено','עדיין לא נוסף דבר','Nothing added yet')}</td></tr>`}
 window.openMachineParts=function(type){
   if(type==='thermo')ctx={type:'thermo',machine:currentMachineIndex,section:currentThermoSection};
   else if(type==='extruder')ctx={type:'extruder',machine:currentMachineIndex,section:currentExtruderSection};
   else ctx={type:'machine',machine:currentMachineIndex,section:null};
   machinePartsBack.onclick=function(){if(ctx.type==='thermo')openThermoSection(ctx.section);else if(ctx.type==='extruder')openExtruderSection(ctx.section);else showPage('machineDetail')};
   renderMachineParts();showPage('machinePartsPage');
 }
 window.openMachinePartEdit=function(i){editIndex=i;let a=items(),x=i>=0?a[i]:{code:'',model:'',mfr:'',specs:'',qty:1,price:'',notes:''};machinePartModalTitle.textContent=tx('Позиция оборудования','פריט ציוד','Equipment item');mpCode.value=x.code||'';mpModel.value=x.model||'';mpMfr.value=x.mfr||'';mpSpecs.value=x.specs||'';mpQty.value=x.qty??1;mpPrice.value=x.price??'';mpNotes.value=x.notes||'';syncText();machinePartModal.classList.add('open')}
 window.closeMachinePartEdit=function(){machinePartModal.classList.remove('open')}
 window.saveMachinePart=function(){let model=mpModel.value.trim();if(!model)return;let x={code:mpCode.value.trim(),model,mfr:mpMfr.value.trim(),specs:mpSpecs.value.trim(),qty:Math.max(0,Number(mpQty.value)||0),price:mpPrice.value===''?'':Number(mpPrice.value),notes:mpNotes.value.trim()};let a=items();if(editIndex>=0)a[editIndex]=x;else a.push(x);store(a);closeMachinePartEdit();renderMachineParts()}

 // Thermoforming machines: every station gets the same editable component table.
 let thermoPage=document.getElementById('thermoSectionPage');
 if(thermoPage&&!document.getElementById('thermoPartsOpen')){let b=document.createElement('button');b.id='thermoPartsOpen';b.className='detail-tile machine-parts-link';b.onclick=()=>openMachineParts('thermo');thermoPage.appendChild(b)}
 // Extruders and standalone machines already have "Electrical parts" tiles; connect them.
 if(document.getElementById('sectionParts'))sectionParts.onclick=()=>openMachineParts('extruder');
 if(document.getElementById('partsTile'))partsTile.onclick=()=>openMachineParts('machine');
 function syncEntryButtons(){let b=document.getElementById('thermoPartsOpen');if(b)b.textContent=tx('Электрические части / создать таблицу','חלקי חשמל / צור טבלה','Electrical parts / create table');if(document.getElementById('sectionParts'))sectionParts.textContent=tx('Электрические части','חלקי חשמל','Electrical parts');if(document.getElementById('partsTile'))partsTile.textContent=tx('Электрические части','חלקי חשמל','Electrical parts');if(document.getElementById('machinePartsPage').classList.contains('active'))renderMachineParts()}
 document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(syncEntryButtons,0)));
 syncEntryButtons();
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
