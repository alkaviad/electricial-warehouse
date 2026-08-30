def apply(legacy):
    patch = r'''<style>
.main-cabinet-tile{background:#e8f1ef!important;border:2px solid #8ca9ad!important}.main-cabinet-page .machine-parts-wrap{margin-top:12px}.main-cabinet-note{color:#718087;margin:4px 0 12px}
</style>
<div class="page main-cabinet-page" id="extruderMainCabinetPage"><button class="back" id="emcBack"></button><h2 id="emcTitle"></h2><p class="main-cabinet-note" id="emcNote"></p><button class="machine-parts-add" id="emcAdd"></button><div id="emcTable"></div></div>
<script>
(function(){
 const KEY='machine_parts_v1';
 let activeMachine=null;
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function e(s){return esc(String(s??''))}
 function load(){try{return JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){return{}}}
 function k(){return 'maincab:'+activeMachine}
 function machineName(i){return (machines[lang]&&machines[lang][i])||''}
 function items(){let d=load();return d[k()]||[]}
 function table(){let a=items();return `<div class="machine-parts-wrap"><table><thead><tr><th>${tx('Код','קוד','Code')}</th><th>${tx('Модель / артикул','דגם / מק״ט','Model / part no.')}</th><th>${tx('Фирма','יצרן','Manufacturer')}</th><th>${tx('Параметры','נתונים','Specifications')}</th><th>${tx('Количество','כמות','Quantity')}</th><th>${tx('Цена','מחיר','Price')}</th><th>${tx('Примечание','הערה','Notes')}</th><th>${tx('Изменение','עריכה','Edit')}</th></tr></thead><tbody>${a.length?a.map((x,i)=>`<tr><td><b>${e(x.code)}</b></td><td>${e(x.model)}</td><td>${e(x.mfr)}</td><td>${e(x.specs)}</td><td class="qty">${e(x.qty)}</td><td>${x.price!==''?e(x.price):''}</td><td>${e(x.notes)}</td><td class="machine-parts-actions"><button onclick="openMainCabinetEdit(${i})">✎</button></td></tr>`).join(''):`<tr><td colspan="8" class="machine-parts-empty">${tx('Пока ничего не добавлено','עדיין לא נוסף דבר','Nothing added yet')}</td></tr>`}</tbody></table></div>`}
 window.renderExtruderMainCabinet=function(){if(activeMachine===null)return;emcTitle.textContent=machineName(activeMachine)+' — '+tx('Лех раши','לוח חשמל ראשי','Main electrical cabinet');emcNote.textContent=tx('Центральный электрощит всего экструдера — управляет всеми его узлами.','לוח החשמל המרכזי של כל האקסטרודר — שולט בכל היחידות שלו.','Central electrical cabinet for the whole extruder — controls all sections.');emcBack.textContent=tx('← Назад','← חזרה','← Back');emcAdd.textContent=tx('+ Новая позиция','+ פריט חדש','+ New item');emcTable.innerHTML=table()}
 window.openExtruderMainCabinet=function(){activeMachine=currentMachineIndex;emcBack.onclick=()=>openExtruder(activeMachine);emcAdd.onclick=()=>openMachinePartEditInline('maincab',activeMachine,null,-1);renderExtruderMainCabinet();showPage('extruderMainCabinetPage')}
 window.openMainCabinetEdit=function(i){openMachinePartEditInline('maincab',activeMachine,null,i)}
 function addTile(){let g=document.getElementById('extruderGrid');if(!g||currentMachineIndex===null)return;if(document.getElementById('extruderMainCabinetTile'))return;let w=document.createElement('div');w.className='tile-wrap';w.id='extruderMainCabinetTile';w.innerHTML=`<button class="section-tile main-cabinet-tile" onclick="openExtruderMainCabinet()">${tx('Лех раши','לוח חשמל ראשי','Main electrical cabinet')}</button>`;g.insertBefore(w,g.firstChild)}
 const oldOpenExtruder=window.openExtruder;window.openExtruder=function(i){oldOpenExtruder(i);setTimeout(addTile,0)};
 document.addEventListener('click',function(ev){if(ev.target&&ev.target.id==='mpSave')setTimeout(()=>{let p=document.getElementById('extruderMainCabinetPage');if(p&&p.classList.contains('active'))renderExtruderMainCabinet()},20)});
 document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(()=>{if(document.getElementById('extruderPage').classList.contains('active')){let old=document.getElementById('extruderMainCabinetTile');if(old)old.remove();addTile()}if(document.getElementById('extruderMainCabinetPage').classList.contains('active'))renderExtruderMainCabinet()},0)));
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
