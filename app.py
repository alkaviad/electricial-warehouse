from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Электрический склад</title>
<style>
*{box-sizing:border-box}
:root{--bg:#eef2f3;--panel:#f8faf9;--ink:#34454b;--muted:#718087;--line:#ccd7d8;--accent:#527d83;--soft:#e0ebea}
body{margin:0;font-family:Arial,Helvetica,sans-serif;background:var(--bg);color:var(--ink)}
header{background:#536a70;color:#f8fbfb;padding:14px 20px}
.top{max-width:1250px;margin:auto;display:flex;justify-content:space-between;align-items:center;gap:15px}
h1{margin:0;font-size:25px}
.lang button,.back,.save{border:1px solid var(--line);border-radius:8px;padding:8px 12px;cursor:pointer}
.workspace{max-width:1250px;margin:auto;padding:18px 14px;display:grid;grid-template-columns:145px 1fr;gap:18px}
.side{display:flex;flex-direction:column;align-items:center;gap:12px}
.diamond-button{width:112px;height:112px;border:0;background:transparent;cursor:pointer}
.diamond{width:80px;height:80px;margin:16px auto;background:#f7faf9;border:2px solid var(--line);border-radius:13px;transform:rotate(45deg);display:flex;align-items:center;justify-content:center}
.diamond-inner{width:102px;transform:rotate(-45deg);text-align:center;font-weight:700;font-size:13px}
.icon{display:block;font-size:20px}
.content{background:var(--panel);border:1px solid var(--line);border-radius:15px;padding:22px;min-width:0}
.page{display:none}.page.active{display:block}
.subtitle{color:var(--muted)}
.box{border:1px solid var(--line);border-radius:12px;padding:20px;background:#fff;min-height:350px}
.machine-grid,.section-grid{display:grid;grid-template-columns:repeat(4,minmax(105px,1fr));gap:12px}
.machine,.section-tile,.detail-tile,.fault-main{min-height:76px;border:1px solid var(--line);border-radius:10px;background:#f2f6f5;color:var(--ink);font-weight:700;cursor:pointer;padding:10px}
.machine:hover,.section-tile:hover,.detail-tile:hover,.fault-main:hover{background:var(--soft);border-color:var(--accent)}
.fault-main{width:220px;min-height:82px;margin:4px 0 20px;background:#e8f1ef;font-size:16px}
.detail-grid{display:grid;grid-template-columns:repeat(2,minmax(180px,1fr));gap:16px;max-width:620px}
.detail-tile{min-height:110px}
.section-info{margin-top:18px;padding:16px;border:1px solid var(--line);border-radius:12px;background:#fff}
.fault-form{margin-top:18px;padding:16px;border:1px solid var(--line);border-radius:12px;background:#fff}
.fault-form label{display:block;font-weight:700;margin:12px 0 5px}
.fault-form input,.fault-form textarea,.fault-form select{width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;background:#fbfdfc}
.fault-form textarea{min-height:70px}
.save{margin-top:14px;background:var(--accent);color:white;font-weight:700}
.records{margin-top:18px;display:grid;gap:10px}
.record{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px}
.record img{max-width:180px;max-height:130px;border-radius:8px;margin-top:8px}
.record-date{font-weight:700}
.stats{margin:15px 0;padding:10px;background:var(--soft);border-radius:8px;font-weight:700}
@media(max-width:720px){
.workspace{grid-template-columns:105px 1fr;gap:8px;padding:10px 6px}.diamond-button{width:92px;height:92px}.diamond{width:64px;height:64px}.diamond-inner{width:86px;font-size:11px}.content{padding:14px 10px}.machine-grid,.section-grid{grid-template-columns:repeat(2,1fr);gap:8px}.detail-grid{grid-template-columns:1fr}.fault-main{width:100%}h1{font-size:20px}
}
</style>
</head>
<body>
<header><div class="top"><h1>⚡ <span id="appTitle"></span></h1><div class="lang"><button onclick="setLang('ru')">RU</button><button onclick="setLang('he')">עברית</button><button onclick="setLang('en')">EN</button></div></div></header>
<main class="workspace">
<nav class="side">
<button class="diamond-button" id="stockBtn" onclick="showPage('stock')"><div class="diamond"><div class="diamond-inner"><span class="icon">📦</span><span id="stockNav"></span></div></div></button>
<button class="diamond-button" id="machinesBtn" onclick="showPage('machines')"><div class="diamond"><div class="diamond-inner"><span class="icon">🏭</span><span id="machinesNav"></span></div></div></button>
</nav>
<section class="content">
<div id="stock" class="page active"><h2 id="stockTitle"></h2><div class="box" id="stockBox"></div></div>
<div id="machines" class="page"><h2 id="machinesTitle"></h2><p class="subtitle" id="machinesSub"></p><div class="machine-grid" id="machineGrid"></div></div>

<div id="thermoPage" class="page">
<button class="back" onclick="showPage('machines')" id="thermoBack"></button>
<h2 id="thermoTitle"></h2><p class="subtitle" id="thermoSub"></p>
<button class="fault-main" id="thermoFaults" onclick="openThermoFaults()"></button>
<div class="section-grid" id="thermoGrid"></div>
</div>

<div id="thermoSectionPage" class="page">
<button class="back" onclick="openThermo(currentMachineIndex)" id="thermoSectionBack"></button>
<h2 id="thermoSectionTitle"></h2>
<div class="section-info"><b id="thermoPartsTitle"></b><p id="thermoPartsText"></p></div>
</div>

<div id="machineDetail" class="page">
<button class="back" onclick="showPage('machines')" id="backBtn"></button><h2 id="machineDetailTitle"></h2>
<div class="detail-grid"><button class="detail-tile" id="faultsTile" onclick="openGenericFaults()"></button><button class="detail-tile" id="partsTile"></button></div>
</div>

<div id="extruderPage" class="page"><button class="back" onclick="showPage('machines')" id="extruderBack"></button><h2 id="extruderTitle"></h2><p class="subtitle" id="extruderSub"></p><div class="section-grid" id="extruderGrid"></div></div>
<div id="extruderSectionPage" class="page"><button class="back" onclick="openExtruder(currentMachineIndex)" id="sectionBack"></button><h2 id="sectionTitle"></h2><div class="detail-grid"><button class="detail-tile" id="sectionFaults" onclick="openExtruderFaults()"></button><button class="detail-tile" id="sectionParts"></button></div></div>

<div id="faultPage" class="page">
<button class="back" onclick="backFromFaults()" id="faultBack"></button><h2 id="faultTitle"></h2><div class="stats" id="stats"></div>
<div class="fault-form">
<label id="dateLabel"></label><input type="date" id="faultDate">
<label id="areaLabel"></label><select id="faultAreaSelect"></select><input id="faultAreaInput" style="display:none">
<label id="faultLabel"></label><textarea id="faultText"></textarea>
<label id="repairLabel"></label><textarea id="repairText"></textarea>
<label id="replaceLabel"></label><input id="replaceText">
<label id="photoLabel"></label><input type="file" accept="image/*" capture="environment" id="faultPhoto">
<button class="save" onclick="saveFault()" id="saveBtn"></button>
</div><div class="records" id="records"></div>
</div>
</section></main>
<script>
let lang=localStorage.getItem('elektrikaLang')||'ru';
let currentMachineIndex=null,currentExtruderSection=null,currentThermoSection=null,faultMode='generic';

const machines={
ru:['Кефель 5','Кефель 6','Кефель 7','Кефель 8','Кефель 9','Кефель 10','Кефель 11','Кефель 12','Кефель 13','C1','C2','C3','RDM','Машина печати','Машина формовки стаканов','Экструдер 4','Экструдер 5','Экструдер 6'],
he:['כפל 5','כפל 6','כפל 7','כפל 8','כפל 9','כפל 10','כפל 11','כפל 12','כפל 13','C1','C2','C3','RDM','מכונת דפוס','מכונת כוסות','אקסטרודר 4','אקסטרודר 5','אקסטרודר 6'],
en:['Kefel 5','Kefel 6','Kefel 7','Kefel 8','Kefel 9','Kefel 10','Kefel 11','Kefel 12','Kefel 13','C1','C2','C3','RDM','Printing Machine','Cup Forming Machine','Extruder 4','Extruder 5','Extruder 6']};

const thermoSections={
ru:['Размотка','Цепной транспорт / подача пластика','Нагрев','Формовка','Нож / резка','Робот и выгрузка','Электрошкаф A','Электрошкаф B'],
he:['פריסה','שרשרת והזנת פלסטיק','חימום','תרמופורמינג','סכין / חיתוך','רובוט ופריקה','לוח חשמל A','לוח חשמל B'],
en:['Unwinding','Chain transport / plastic feed','Heating','Thermoforming','Knife / cutting','Robot and unloading','Electrical Cabinet A','Electrical Cabinet B']};

const extruderSections={
ru:['Станция дозирования','Экструдер A — главный','Экструдер B — вспомогательный','Каландр','Станция силикона','Ресивер','Узел намотки'],
he:['תחנת מינון','אקסטרודר A — ראשי','אקסטרודר B — משני','קלנדר','תחנת סיליקון','רסיבר','גלילן'],
en:['Dosing Station','Extruder A — Main','Extruder B — Secondary','Calender','Silicone Station','Receiver','Winding Unit']};

const T={
ru:{title:'Электрический склад',stock:'Общий склад',machines:'Машины',choose:'Выберите машину',back:'← Назад к машинам',faults:'Поломки',parts:'Электрические части',faultBack:'← Назад',date:'Дата поломки',area:'Часть машины',fault:'Какая поломка',repair:'Что сделал / ремонт',replace:'Замена электрической детали',photo:'Фотография поломки',save:'Сохранить поломку',stats:'Всего сохранённых поломок',extruderSub:'Выберите часть экструзионной линии',sectionBack:'← Назад к экструдеру',thermoSub:'Выберите станцию машины',thermoBack:'← Назад к машинам',thermoSectionBack:'← Назад к машине',partsTitle:'Электрические части этой станции',partsText:'Здесь будем хранить моторы, датчики, нагреватели, приводы, модели и другие электрические компоненты этой станции.',stockText:'Здесь будем отдельно строить общий склад.'},
he:{title:'מחסן חשמל',stock:'מחסן כללי',machines:'מכונות',choose:'בחר מכונה',back:'← חזרה למכונות',faults:'תקלות',parts:'חלקי חשמל',faultBack:'← חזרה',date:'תאריך התקלה',area:'חלק במכונה',fault:'מה התקלקל',repair:'מה עשיתי / תיקון',replace:'החלפת חלק חשמלי',photo:'תמונה של התקלה',save:'שמור תקלה',stats:'סה״כ תקלות שמורות',extruderSub:'בחר חלק מקו האקסטרוזיה',sectionBack:'← חזרה לאקסטרודר',thermoSub:'בחר תחנה במכונה',thermoBack:'← חזרה למכונות',thermoSectionBack:'← חזרה למכונה',partsTitle:'חלקי החשמל של התחנה',partsText:'כאן נשמור מנועים, חיישנים, גופי חימום, דרייבים, דגמים ורכיבים חשמליים של התחנה.',stockText:'כאן נבנה את המחסן הכללי.'},
en:{title:'Electrical Warehouse',stock:'General Warehouse',machines:'Machines',choose:'Select a machine',back:'← Back to machines',faults:'Faults',parts:'Electrical Parts',faultBack:'← Back',date:'Fault date',area:'Machine section',fault:'Fault description',repair:'What was done / repair',replace:'Electrical part replaced',photo:'Fault photo',save:'Save fault',stats:'Saved faults',extruderSub:'Select a section of the extrusion line',sectionBack:'← Back to extruder',thermoSub:'Select a machine station',thermoBack:'← Back to machines',thermoSectionBack:'← Back to machine',partsTitle:'Electrical parts for this station',partsText:'Here we will store motors, sensors, heaters, drives, models and other electrical components for this station.',stockText:'We will build the general warehouse here.'}}

function showPage(p){document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));document.getElementById(p).classList.add('active')}
function makeMachines(){let g=document.getElementById('machineGrid');g.innerHTML='';machines[lang].forEach((n,i)=>{let b=document.createElement('button');b.className='machine';b.textContent=n;b.onclick=()=>openMachine(i);g.appendChild(b)})}
function openMachine(i){currentMachineIndex=i;currentExtruderSection=null;currentThermoSection=null;if(i<=11){openThermo(i);return}if(i>=15){openExtruder(i);return}document.getElementById('machineDetailTitle').textContent=machines[lang][i];showPage('machineDetail')}

function openThermo(i){currentMachineIndex=i;currentThermoSection=null;thermoTitle.textContent=machines[lang][i];thermoSub.textContent=T[lang].thermoSub;thermoFaults.textContent='⚠ '+T[lang].faults;let g=thermoGrid;g.innerHTML='';thermoSections[lang].forEach((n,idx)=>{let b=document.createElement('button');b.className='section-tile';b.textContent=n;b.onclick=()=>openThermoSection(idx);g.appendChild(b)});showPage('thermoPage')}
function openThermoSection(idx){currentThermoSection=idx;thermoSectionTitle.textContent=machines[lang][currentMachineIndex]+' — '+thermoSections[lang][idx];thermoPartsTitle.textContent=T[lang].partsTitle;thermoPartsText.textContent=T[lang].partsText;showPage('thermoSectionPage')}

function openExtruder(i){currentMachineIndex=i;currentExtruderSection=null;extruderTitle.textContent=machines[lang][i];extruderSub.textContent=T[lang].extruderSub;let g=extruderGrid;g.innerHTML='';extruderSections[lang].forEach((n,idx)=>{let b=document.createElement('button');b.className='section-tile';b.textContent=n;b.onclick=()=>openExtruderSection(idx);g.appendChild(b)});showPage('extruderPage')}
function openExtruderSection(idx){currentExtruderSection=idx;sectionTitle.textContent=machines[lang][currentMachineIndex]+' — '+extruderSections[lang][idx];showPage('extruderSectionPage')}

function todayLocal(){let d=new Date(),m=String(d.getMonth()+1).padStart(2,'0'),day=String(d.getDate()).padStart(2,'0');return d.getFullYear()+'-'+m+'-'+day}
function prepareFaultForm(){faultDate.value=todayLocal();faultText.value='';repairText.value='';replaceText.value='';faultPhoto.value=''}
function openThermoFaults(){faultMode='thermo';currentThermoSection=null;faultTitle.textContent=machines[lang][currentMachineIndex]+' — '+T[lang].faults;faultAreaInput.style.display='none';faultAreaSelect.style.display='block';faultAreaSelect.innerHTML='';thermoSections[lang].forEach(n=>{let o=document.createElement('option');o.value=n;o.textContent=n;faultAreaSelect.appendChild(o)});prepareFaultForm();renderRecords();showPage('faultPage')}
function openGenericFaults(){faultMode='generic';faultTitle.textContent=machines[lang][currentMachineIndex]+' — '+T[lang].faults;faultAreaSelect.style.display='none';faultAreaInput.style.display='block';faultAreaInput.value='';prepareFaultForm();renderRecords();showPage('faultPage')}
function openExtruderFaults(){faultMode='extruder';faultTitle.textContent=machines[lang][currentMachineIndex]+' — '+extruderSections[lang][currentExtruderSection]+' — '+T[lang].faults;faultAreaSelect.style.display='none';faultAreaInput.style.display='block';faultAreaInput.value=extruderSections[lang][currentExtruderSection];prepareFaultForm();faultAreaInput.value=extruderSections[lang][currentExtruderSection];renderRecords();showPage('faultPage')}
function backFromFaults(){if(faultMode==='thermo')showPage('thermoPage');else if(faultMode==='extruder')showPage('extruderSectionPage');else showPage('machineDetail')}
function faultKey(){if(faultMode==='thermo')return 'faults_machine_'+currentMachineIndex+'_thermo';if(faultMode==='extruder')return 'faults_machine_'+currentMachineIndex+'_section_'+currentExtruderSection;return 'faults_machine_'+currentMachineIndex}
function selectedArea(){return faultMode==='thermo'?faultAreaSelect.value:faultAreaInput.value}
function saveFault(){let file=faultPhoto.files[0];let finish=(photo)=>{let a=JSON.parse(localStorage.getItem(faultKey())||'[]');a.unshift({date:faultDate.value,area:selectedArea(),fault:faultText.value,repair:repairText.value,replace:replaceText.value,photo:photo||''});try{localStorage.setItem(faultKey(),JSON.stringify(a))}catch(e){alert('Фотография слишком большая. Попробуйте фото меньшего размера.');return}faultText.value='';repairText.value='';replaceText.value='';faultPhoto.value='';renderRecords()};if(file){let r=new FileReader();r.onload=e=>finish(e.target.result);r.readAsDataURL(file)}else finish('')}
function renderRecords(){let a=JSON.parse(localStorage.getItem(faultKey())||'[]');stats.textContent=T[lang].stats+': '+a.length;records.innerHTML='';a.forEach(x=>{let d=document.createElement('div');d.className='record';d.innerHTML='<div class="record-date">'+esc(x.date)+'</div><div><b>'+T[lang].area+':</b> '+esc(x.area)+'</div><div><b>'+T[lang].fault+':</b> '+esc(x.fault)+'</div><div><b>'+T[lang].repair+':</b> '+esc(x.repair)+'</div><div><b>'+T[lang].replace+':</b> '+esc(x.replace)+'</div>'+(x.photo?'<img src="'+x.photo+'">':'');records.appendChild(d)})}
function esc(s){let d=document.createElement('div');d.textContent=s||'';return d.innerHTML}

function setLang(l){lang=l;localStorage.setItem('elektrikaLang',l);let t=T[l];document.documentElement.dir=l==='he'?'rtl':'ltr';appTitle.textContent=t.title;stockNav.textContent=t.stock;machinesNav.textContent=t.machines;stockTitle.textContent=t.stock;stockBox.textContent=t.stockText;machinesTitle.textContent=t.machines;machinesSub.textContent=t.choose;backBtn.textContent=t.back;faultsTile.textContent=t.faults;partsTile.textContent=t.parts;extruderBack.textContent=t.back;sectionBack.textContent=t.sectionBack;sectionFaults.textContent=t.faults;sectionParts.textContent=t.parts;thermoBack.textContent=t.thermoBack;thermoSectionBack.textContent=t.thermoSectionBack;faultBack.textContent=t.faultBack;dateLabel.textContent=t.date;areaLabel.textContent=t.area;faultLabel.textContent=t.fault;repairLabel.textContent=t.repair;replaceLabel.textContent=t.replace;photoLabel.textContent=t.photo;saveBtn.textContent=t.save;makeMachines();if(currentMachineIndex!==null){if(currentMachineIndex<=11&&thermoPage.classList.contains('active'))openThermo(currentMachineIndex);if(currentMachineIndex>=15&&extruderPage.classList.contains('active'))openExtruder(currentMachineIndex)}}
setLang(lang);
</script></body></html>'''

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
