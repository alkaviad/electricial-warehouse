def apply(legacy):
    patch = r'''<style>
/* A8 — private mini-program for Extruder 5 / Extruder B only. */
#extruderSectionPage.e5-exb-private > #e4StationCatalog,
#extruderSectionPage.e5-exb-private > #e5StationCatalog,
#extruderSectionPage.e5-exb-private > .detail-grid{display:none!important}
#e5ExBCatalog{display:block!important;margin:10px 0 20px;padding:15px;border:2px solid #9fb8ba;border-radius:14px;background:#fff}
.e5xb-grid{display:grid;grid-template-columns:repeat(3,minmax(150px,1fr));gap:12px}.e5xb-tile{min-height:82px;border:1px solid #cbd8d9;border-radius:11px;background:#f4f8f7;color:#34454b;font-size:14px;font-weight:700;padding:12px;cursor:pointer}.e5xb-head{display:flex;justify-content:space-between;align-items:center;gap:10px}.e5xb-back{padding:8px 12px;border:1px solid #cbd8d9;border-radius:8px;background:#f4f8f7;cursor:pointer;font-weight:700}.e5xb-sub{font-size:12px;color:#687b80;margin:5px 0 12px}.e5xb-wrap{overflow:auto;max-height:650px}.e5xb-table{width:100%;border-collapse:collapse;min-width:900px}.e5xb-table th,.e5xb-table td{padding:8px;border-bottom:1px solid #e3eaea;text-align:left;font-size:12px;vertical-align:top}.e5xb-table th{position:sticky;top:0;background:#e8f1ef}@media(max-width:850px){.e5xb-grid{grid-template-columns:repeat(2,minmax(130px,1fr))}}
</style><script>
(function(){
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function esc(s){return String(s==null?'':s).replace(/[&<>\"']/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[m]})}
 function target(si){
   try{var mi=Number(currentMachineIndex),s=si==null?Number(currentExtruderSection):Number(si);if(mi===16&&s===2)return true;
   var mn=((machines[lang]||[])[mi]||'').toLowerCase(),sn=((extruderSections[lang]||[])[s]||'').toLowerCase();
   return mn.indexOf('5')>=0&&(mn.indexOf('экструдер')>=0||mn.indexOf('אקסטרודר')>=0||mn.indexOf('extruder')>=0)&&(sn.indexOf('b')>=0||sn.indexOf('б')>=0||sn.indexOf('ראשי')>=0||sn.indexOf('main')>=0);
   }catch(e){return false}
 }
 var cats=[
  ['cb1heat',['CB1 — нагрев цилиндра','CB1 — חימום צילינדר','CB1 — barrel heating']],
  ['cb1aux',['CB1 — насос смазки / термостатирование','CB1 — משאבת סיכה / תרמוסטט','CB1 — lubrication / thermostatic unit']],
  ['cb1io',['CB1 — PLC / I/O / Safety','CB1 — PLC / I/O / Safety','CB1 — PLC / I/O / Safety']],
  ['cb3screen',['CB3 — сменщик фильтра','CB3 — מחליף מסנן','CB3 — screenchanger']],
  ['cb3pump',['CB3 — melt pump / трубы','CB3 — משאבת התך / צנרת','CB3 — melt pump / pipes']],
  ['cb3heat',['CB3 — нагреватели / термопары','CB3 — גופי חימום / תרמוקפלים','CB3 — heaters / thermocouples']],
  ['cb4vac',['CB4 — вакуумные насосы','CB4 — משאבות ואקום','CB4 — vacuum pumps']],
  ['cb4valves',['CB4 — электроклапаны / охлаждение','CB4 — שסתומים חשמליים / קירור','CB4 — solenoid valves / cooling']],
  ['motors',['Моторы и полевое оборудование','מנועים וציוד שטח','Motors and field equipment']]
 ];
 function row(n,d,m,p,data){return[n,d,m,p,data]}
 var D={
  cb1heat:[
   row('Зона нагрева цилиндра 1','401','','','CB1 · thermoregulation zone'),row('Зона нагрева цилиндра 2','402','','','CB1'),row('Зона нагрева цилиндра 3','403','','','CB1'),row('Зона нагрева цилиндра 4','404','','','CB1'),row('Зона нагрева цилиндра 5','405','','','CB1'),row('Зона нагрева цилиндра 6','406','','','CB1'),row('Зона нагрева цилиндра 7','407','','','CB1'),row('Зона нагрева цилиндра 8','408','','','CB1'),row('Зона нагрева цилиндра 9','409','','','CB1'),row('Зона нагрева цилиндра 10','410','','','CB1'),row('Зона нагрева цилиндра 11','411','','','CB1'),row('Зона нагрева цилиндра 12','412','','','CB1'),row('Зона дегазации 1','413','','','CB1'),row('Зона дегазации 2','414','','','CB1'),
   row('SSR зоны адаптера сменщика фильтра','-415KP2','Carlo Gavazzi','RGS1A60D50KKE','50A · 24Vdc'),row('Нагреватели зоны адаптера','-415R2 / -415R2.1 / -415R2.2 / -415R2.3','','','4 kW total group; individual elements shown on drawing'),row('Предохранитель нагрева','-415FU2','','5017906.25','25A gR')
  ],
  cb1aux:[row('Пускатель насоса смазки','-85Q1','Siemens','3RA6120-2CB32','1–4 A · Class 10'),row('Мотор насоса смазки','+EB-85M1','','','Extruder lubrication pump'),row('Датчик MIN давления смазки','+EB-85SP5','','','Lubrication MIN pressure'),row('Датчик MAX давления смазки','+EB-85SP6','','','Lubrication MAX pressure'),row('Термостатическая установка цилиндра','+TU / +EB-L1,L2,L3','','','Cylinder thermostatic unit · page 86'),row('Термопара термостатической установки','+TU-X1','','','CB1 · IW1094')],
  cb1io:[row('DI 8x24VDC ST','-952A0','Siemens','6ES7131-6BF00-0BA0','ET200SP · lubrication/cooling inputs'),row('F-DQ 4x24VDC/2A PM HF','-962A0','Siemens','6ES7136-6DB00-0CA0','ET200SP · lubrication/heating safety outputs'),row('AI Energy Meter ST','-907A0','Siemens','6ES7134-6PA00-0BD0','Extruder B heating supply measurement'),row('Main heating contactor','-400KM7','Siemens','3RT1456-6AB36','275A · 24Vdc · S6')],
  cb3screen:[row('Screenchanger hydraulic/unit control','91 / 92','','','CB3 · screenchanger unit'),row('Температура расплава сменщика фильтра','-93ST3','','','Melt thermocouple · CB3'),row('AI RTD/TC module','-925A0','Siemens','6ES7134-6JF00-0CA1','AI 8xRTD/TC 2-wire HF ET200SP'),row('Контроль давления сменщика фильтра','94','','','CB3 · pressure control')],
  cb3pump:[row('Контроль температуры труб','95','','','CB3 · pipe temperature control'),row('Контроль давления входа melt pump','96','','','CB3 · pump input pressure'),row('Pipe zone 2','410','','','CB3'),row('Pipe zone 3','411','','','CB3'),row('Pipe zone 4','412','','','CB3'),row('Pipe zone 5','413','','','CB3'),row('Pipe zone 6','414','','','CB3'),row('Pipe zone 7','415','','','CB3'),row('Pipe zone 8','416','','','CB3'),row('Pipe zone 9','417','','','CB3')],
  cb3heat:[row('AI RTD/TC module','-924A0','Siemens','6ES7134-6JF00-0CA1','Pipe thermocouples · ET200SP'),row('Термопара pipe zone 4','+PB-412ST5','','','IW1576'),row('Термопара pipe zone 5','+PB-413ST5','','','IW1578'),row('Термопара pipe zone 6','+PB-414ST5','','','IW1580'),row('Термопара pipe zone 7','+PB-415ST5','','','IW1582'),row('Термопара pipe zone 8','+PB-416ST5','','','IW1584'),row('Термопара pipe zone 9','+PB-417ST5','','','IW1586')],
  cb4vac:[row('Вакуумные насосы','105 / 106','','','CB4 · Extruder B degassing vacuum pumps'),row('Остаточный вакуум дегазации','110','','','CB4 · residual vacuum'),row('Температура воды дегазации','109','','','CB4'),row('Температура воздуха / chimney','110a','','','CB4'),row('Команды старт/стоп вакуумных насосов','110b','','','CB4')],
  cb4valves:[row('Электроклапаны заполнения','107','','','CB4 · refilling solenoid valves'),row('Электроклапаны срыва вакуума','108','','','CB4 · vacuum break solenoid valves'),row('Bypass уровней дегазации','110c','','','CB4 · degassing level bypass')],
  motors:[row('Главный узел Extruder B','+EB','Bandera','2C85','Twin-screw Extruder B; main motor/drive belongs to line power system'),row('Melt / volumetric pump B','+PB','','','Melt gear/volumetric pump B; pressure-stabilizing process unit'),row('Охлаждение цилиндра','','','','Cylinder cooling fans are monitored by CB1 PLC input'),row('Охлаждение шкафа CB1','10','','','Cabinet cooling'),row('Охлаждение шкафа CB3','10','','','Cabinet cooling')]
 };
 var selected=null;
 function label(c){return c[1][lang==='he'?1:lang==='en'?2:0]}
 function remove(){var x=document.getElementById('e5ExBCatalog');if(x)x.remove();var p=document.getElementById('extruderSectionPage');if(p)p.classList.remove('e5-exb-private')}
 function render(){
   var p=document.getElementById('extruderSectionPage');if(!p||!p.classList.contains('active')||!target()){remove();return}p.classList.add('e5-exb-private');
   var old=document.getElementById('e5ExBCatalog');if(old)old.remove();var d=document.createElement('div');d.id='e5ExBCatalog';
   if(selected){var c=cats.find(function(x){return x[0]===selected}),rows=D[selected]||[];d.innerHTML='<div class="e5xb-head"><h2>'+esc(label(c))+'</h2><button class="e5xb-back" id="e5xbCatBack">'+tx('← Назад','← חזרה','← Back')+'</button></div><div class="e5xb-sub">S.3909 · OR16/268 · Extruder B: CB1 / CB3 / CB4</div><div class="e5xb-wrap"><table class="e5xb-table"><thead><tr><th>'+tx('Название','שם','Name')+'</th><th>'+tx('Номер на чертеже','מספר בשרטוט','Drawing designation')+'</th><th>'+tx('Производитель','יצרן','Manufacturer')+'</th><th>Part No.</th><th>'+tx('Данные','נתונים','Data')+'</th></tr></thead><tbody>'+rows.map(function(r){return '<tr>'+r.map(function(v){return '<td>'+esc(v)+'</td>'}).join('')+'</tr>'}).join('')+'</tbody></table></div>'}
   else d.innerHTML='<button class="e5xb-back" id="e5xbMainBack">'+tx('← Назад','← חזרה','← Back')+'</button><h2>'+tx('Экструдер B — электрическое оборудование','אקסטרודר B — ציוד חשמלי','Extruder B — electrical equipment')+'</h2><div class="e5xb-sub">'+tx('Отдельно по физическим шкафам CB1, CB3, CB4 и полевому оборудованию.','מחולק לפי הארונות הפיזיים CB1, CB3, CB4 וציוד השטח.','Separated by physical cabinets CB1, CB3, CB4 and field equipment.')+'</div><div class="e5xb-grid">'+cats.map(function(c){return '<button type="button" class="e5xb-tile" data-e5xb="'+c[0]+'">'+esc(label(c))+'</button>'}).join('')+'</div>';
   var title=document.getElementById('sectionTitle');if(title&&title.parentNode===p)title.insertAdjacentElement('afterend',d);else p.insertBefore(d,p.firstChild);
   d.querySelectorAll('[data-e5xb]').forEach(function(b){b.onclick=function(e){e.stopPropagation();selected=this.dataset.e5xb;render()}});var cb=document.getElementById('e5xbCatBack');if(cb)cb.onclick=function(e){e.stopPropagation();selected=null;render()};var mb=document.getElementById('e5xbMainBack');if(mb)mb.onclick=function(e){e.stopPropagation();remove();if(typeof openExtruder==='function')openExtruder(currentMachineIndex)};
 }
 var prev=window.openExtruderSection;if(typeof prev==='function'&&!prev.__e5xbA8){window.openExtruderSection=function(i){selected=null;var r=prev.apply(this,arguments);if(target(i)){setTimeout(render,20);setTimeout(render,120)}else remove();return r};window.openExtruderSection.__e5xbA8=true}
 document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){if(target())setTimeout(render,50)})});
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
