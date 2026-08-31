def apply(legacy):
    patch = r'''<style>
#e4MainGroups,#e4MainPhysicalDrives,#e4ForcedMainDrives{display:none!important}
#e4MainCabinetInventory{margin:14px 0 20px;padding:15px;border:1px solid #d3ddde;border-radius:14px;background:#fff}
#e4MainCabinetInventory h2{margin:0 0 14px;font-size:20px}
.e4mc-grid{display:grid;grid-template-columns:repeat(4,minmax(150px,1fr));gap:12px}
.e4mc-tile{min-height:72px;border:1px solid #cbd8d9;border-radius:11px;background:#f8fbfa;color:#34454b;font-size:15px;font-weight:700;cursor:pointer;padding:12px}
.e4mc-tile:hover{background:#eef5f3;border-color:#91aaad}
#e4mcDetail{margin-top:14px;border:1px solid #cbd8d9;border-radius:12px;padding:14px;background:#fff}
#e4mcDetail[hidden]{display:none!important}.e4mc-detail-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:10px}.e4mc-detail-head h3{margin:0;font-size:18px}.e4mc-close{border:1px solid #cbd8d9;border-radius:8px;background:#f4f8f7;padding:7px 11px;cursor:pointer}.e4mc-wrap{overflow:auto;max-height:560px}.e4mc-table{width:100%;border-collapse:collapse;min-width:860px}.e4mc-table th,.e4mc-table td{padding:8px;border-bottom:1px solid #e3eaea;text-align:left;vertical-align:top;font-size:12px}.e4mc-table th{position:sticky;top:0;background:#f4f8f7;color:#52666a;z-index:1}
@media(max-width:850px){.e4mc-grid{grid-template-columns:repeat(2,minmax(140px,1fr))}}
</style><script>
(function(){
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function x(s){return String(s??'').replace(/[&<>\"']/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[m]})}
 function isE4(){var n=((machines[lang]||[])[currentMachineIndex]||'').toLowerCase();return n.indexOf('4')>=0&&(n.indexOf('экструдер')>=0||n.indexOf('אקסטרודר')>=0||n.indexOf('extruder')>=0)}
 const groups=[
 {k:'plc',title:['PLC / CPU','PLC / CPU','PLC / CPU'],rows:[
  ['Главный PLC CPU','-900U2','Siemens CPU 317F-2 PN/DP','6ES7317-2FK14-0AB0','1'],
  ['Карта памяти PLC','-900U2','SIMATIC S7 Micro Memory Card 2 MB','6ES7953-8LL31-0AA0','1']
 ]},
 {k:'io',title:['Модули I/O','מודולי I/O','I/O modules'],rows:[
  ['Цифровой вход DI','-203U2','Siemens SM321','6ES7321-1BL00-0AA0 · 32 DI / 24VDC','1'],
  ['Цифровой вход DI','-203U3','Siemens SM321','6ES7321-1BL00-0AA0 · 32 DI / 24VDC','1'],
  ['Цифровой вход DI','-203U4','Siemens SM321','6ES7321-1BL00-0AA0 · 32 DI / 24VDC','1'],
  ['Цифровой выход DO','-203U6','Siemens SM322','6ES7322-1BL00-0AA0 · 32 DO / 24VDC / 0.5A','1'],
  ['Цифровой выход DO','-203U7','Siemens SM322','6ES7322-1BL00-0AA0 · 32 DO / 24VDC / 0.5A','1'],
  ['Цифровой выход DO','-204U1','Siemens SM322','6ES7322-1BL00-0AA0 · 32 DO / 24VDC / 0.5A','1'],
  ['Аналоговый вход AI','-201U3','Siemens SM331','6ES7331-7KF02-0AB0 · AI 8x12 bit · 0/4–20mA','1'],
  ['Аналоговый выход AO','-201U5 / +2-201U6','Siemens SM332','6ES7332-5HD01-0AB0 · AO 4x12 bit','1'],
  ['Интерфейс распределённого I/O','-203U1','Siemens IM153','6ES7153-1AA03-0XB0','1']
 ]},
 {k:'safety',title:['PLC безопасности','PLC בטיחות','Safety PLC'],rows:[
  ['Станция PROFIsafe','-206U1','Siemens ET200S safety station','6ES7151-7FA20-0AB0','1'],
  ['Модуль питания safety','-206U2','Siemens power module','6ES7138-4CB11-0AA0','1'],
  ['Безопасный вход F-DI','-206U3','Siemens F-DI','6ES7138-4FA03-0AB0 · 4/8 F-DI 24VDC','1'],
  ['Безопасный вход F-DI','-206U4','Siemens F-DI','6ES7138-4FA03-0AB0 · 4/8 F-DI 24VDC','1'],
  ['Безопасный вход F-DI','-206U4.1','Siemens F-DI','6ES7138-4FA03-0AB0 · 4/8 F-DI 24VDC','1'],
  ['Безопасный выход F-DO','-206U5','Siemens F-DO','6ES7138-4FB02-0AB0 · 4 F-DO 24VDC / 2A','1'],
  ['Безопасный выход F-DO','-206U6','Siemens F-DO','6ES7138-4FB02-0AB0 · 4 F-DO 24VDC / 2A','1'],
  ['Безопасный выход F-DO','-206U7','Siemens F-DO','6ES7138-4FB02-0AB0 · 4 F-DO 24VDC / 2A','1']
 ]},
 {k:'ethernet',title:['Ethernet / связь','Ethernet / תקשורת','Ethernet / communication'],rows:[
  ['Ethernet switch','-891U2','Siemens SCALANCE XB008','6GK5008-0BA00-1AB2','1'],
  ['Ethernet switch','-891U7','Siemens SCALANCE XB008','6GK5008-0BA00-1AB2','1'],
  ['Communication Processor','-900U5','Siemens CP343-1','SIMATIC S7-300 communication processor','1']
 ]},
 {k:'drives',title:['Драйверы','דרייבים','Drives'],rows:[
  ['Привод объёмного насоса Extruder A','-38U1','ABB ACS 800-01-0006-3','3.9 kW · Profibus ADD=26','1'],
  ['Привод объёмного насоса Extruder B','-43U1','ABB ACS 800-01-0030-3','20.3 kW · 390V · 42.5A · ADD=16','1'],
  ['Главный привод Extruder A','-53U1','ABB ACS 800-01-0100-3','75 kW · 400V · 136A · ADD=21','1'],
  ['Главный привод Extruder B','-61U1','ABB ACS 800-04-0400-3','315 kW · 400V · 529A · ADD=11','1'],
  ['Привод входного валка каландра','-91U1','ABB ACS 800-01-0011-3','6.5 kW · 380V · 14.8A · ADD=70','1'],
  ['Привод центрального валка каландра','-95U1','ABB ACS 800-01-0020-3','12 kW · 380V · 27.5A · ADD=71','1'],
  ['Привод выходного валка каландра','-99U1','ABB ACS 800-01-0011-3','6.5 kW · 380V · 14.8A · ADD=72','1'],
  ['Привод перемещения каландра','-110U1','ABB ACS 550-01-03A3-4J-404','0.25 kW','1'],
  ['Привод охлаждающего валка','-120U1','ABB ACS 800-01-0006-3','4.0 kW · 380V · 10A · ADD=73','1'],
  ['Привод тянущего устройства','-130U1','ABB ACS 800-01-0005-3','2.7 kW · 380V · 7A · ADD=81','1'],
  ['Привод прижимного валка','-145U1','ABB ACS 550-01-03A3-4J-404','0.25 kW · 400V · 0.78A · ADD=75','1'],
  ['Привод размотчика 1','-152U1','ABB ACS 550-01-04A1-4','Profibus ADD=76','1'],
  ['Привод размотчика 2','-162U1','ABB ACS 550-01-04A1-4','Profibus ADD=77','1']
 ]},
 {k:'power',title:['Питание 24VDC','ספקי 24VDC','24VDC supply'],rows:[
  ['Буферный модуль SITOP','-5U1','Siemens SITOP','6EP1961-3BA01','1'],
  ['Блок питания SITOP PSU200M','-5U2','Siemens SITOP PSU200M','6EP1333-3BA10 · 5A','1'],
  ['Трёхфазный блок питания 24VDC','-21U1','Siemens SITOP','6EP1436-2BA10 · 400–500VAC / 24VDC 20A','1'],
  ['Селективный модуль защиты','-21U3','Siemens SITOP PSE200U','6EP1961-2BA21 · 10A','1']
 ]},
 {k:'contactors',title:['Контакторы','קונטקטורים','Contactors'],rows:[
  ['Контактор','+2-36KM2','Siemens 3RT1016-1AF01','Доп. контакт 3RH1911-1FA11','1'],
  ['Контактор','+2-40KM1','Siemens 3RT1016-1AF01','','1'],
  ['Контактор','+2-45KM1','Siemens 3RT1035-1AG20','','1'],
  ['Контактор','+2-55KM2','Siemens 3RT1446-1AG20','','1'],
  ['Контактор','+2-57KM4','Siemens 3RT1025-1AG20','','1'],
  ['Контактор','+2-65KM4','Siemens 3RT1026-1AG20','','1']
 ]},
 {k:'relays',title:['Реле','ממסרים','Relays'],rows:[
  ['Промежуточное реле','+2-27KA7','Phoenix Contact','2966171','1'],
  ['Промежуточное реле','+2-29KA7','Phoenix Contact','2966171','1'],
  ['Реле','+2-29KA2','Omron MY3','110VAC','1'],
  ['Реле','+2-29KA2','Omron MY4','110V','1']
 ]},
 {k:'breakers',title:['Автоматы / защита','מאמ״תים / הגנות','Breakers / protection'],rows:[
  ['Главный автоматический выключатель','-5QF6','Siemens 3WL1220-2BB44-1AJ2-Z T40','2000A · 4P · 66kA','1'],
  ['Автоматический выключатель','-8QF1','Siemens 5SY8206-7','6A · C · 2P','1'],
  ['УЗО / дифференциальный блок','-8QF1','Siemens 5SM2322-0','30mA AC · 2P · 0.3–40A','1'],
  ['Автоматический выключатель','-21QF1','Siemens 5SY8306-7','6A · C · 3P','1']
 ]},
 {k:'terminals',title:['Клеммы / разъёмы','מהדקים / מחברים','Terminals / connectors'],rows:[
  ['Клеммная плата','XPLC','Terminal board','PLC connections','1'],
  ['Клеммная плата','X118','Terminal board','External / cabinet connections','1'],
  ['Клеммная плата','X117','Terminal board','External / cabinet connections','1'],
  ['Клеммная плата','X32','Terminal board','Cabinet connections','1'],
  ['Клеммная плата','X31','Terminal board','Cabinet connections','1']
 ]},
 {k:'signals',title:['Сигнализация / лампы','איתות / נוריות','Signals / lamps'],rows:[
  ['Сигнальная лампа / светильник','-8HL1','Sikur Italia COO7-50','7W','1'],
  ['Красная сигнальная лампа','-9HL2','Sirena FLR90353','Red','1'],
  ['Аварийная лампа максимальной температуры','-27KA7 / lamp circuit','Alarm lamp','Max temperature alarm','1'],
  ['Аварийная лампа температуры расплава','-27KA8 / lamp circuit','Alarm lamp','Melt max temperature alarm','1']
 ]}
 ];
 function titleOf(g){return g.title[lang==='he'?1:lang==='en'?2:0]}
 window.e4mcOpen=function(k){var g=groups.find(function(a){return a.k===k});if(!g)return;var d=document.getElementById('e4mcDetail');if(!d)return;var rows=g.rows.map(function(r){return '<tr><td>'+x(r[0])+'</td><td><b>'+x(r[1])+'</b></td><td>'+x(r[2])+'</td><td>'+x(r[3]||'—')+'</td><td>'+x(r[4]||'1')+'</td></tr>'}).join('');d.innerHTML='<div class="e4mc-detail-head"><h3>'+x(titleOf(g))+'</h3><button class="e4mc-close" onclick="e4mcClose()">'+tx('Закрыть','סגור','Close')+'</button></div><div class="e4mc-wrap"><table class="e4mc-table"><thead><tr><th>'+tx('Название','שם','Name')+'</th><th>'+tx('Номер на чертеже','מספר בשרטוט','Drawing designation')+'</th><th>'+tx('Модель / Part No.','דגם / מק״ט','Model / Part No.')+'</th><th>'+tx('Данные / назначение','נתונים / תפקיד','Data / function')+'</th><th>'+tx('На машине','במכונה','On machine')+'</th></tr></thead><tbody>'+rows+'</tbody></table></div>';d.hidden=false;d.scrollIntoView({behavior:'smooth',block:'nearest'})}
 window.e4mcClose=function(){var d=document.getElementById('e4mcDetail');if(d)d.hidden=true}
 function render(){if(!isE4())return;var anchor=document.getElementById('extruderMainPanelBlock');if(!anchor||!anchor.parentNode)return;var old=document.getElementById('e4MainCabinetInventory');if(old)old.remove();var d=document.createElement('div');d.id='e4MainCabinetInventory';d.innerHTML='<h2>'+tx('Главный электрический шкаф','לוח חשמל ראשי','Main electrical cabinet')+'</h2><div class="e4mc-grid">'+groups.map(function(g){return '<button class="e4mc-tile" onclick="e4mcOpen(\''+g.k+'\')">'+x(titleOf(g))+'</button>'}).join('')+'</div><div id="e4mcDetail" hidden></div>';anchor.parentNode.insertBefore(d,anchor)}
 function hook(){var f=window.openExtruderMainPanel;if(typeof f==='function'&&!f.__e4inventory){var w=function(){var r=f.apply(this,arguments);setTimeout(render,50);setTimeout(render,250);return r};w.__e4inventory=true;window.openExtruderMainPanel=w}}
 hook();document.addEventListener('DOMContentLoaded',hook);document.addEventListener('click',function(){setTimeout(function(){hook();var p=document.getElementById('extruderMainPanelPage');if(p&&p.classList.contains('active'))render()},80)});document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){setTimeout(render,80)})});
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
