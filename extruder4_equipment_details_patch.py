def apply(legacy):
    patch = r'''<style>
.e4detailbox{margin:12px 0 18px;padding:14px;border:1px solid #cbd8d9;border-radius:12px;background:#fff}.e4detailbox h3{margin:0 0 10px;font-size:18px}.e4detailbox .close{margin-bottom:10px;padding:8px 12px;border:1px solid #b9c8ca;border-radius:8px;background:#eef5f3;cursor:pointer}.e4detailbox table{width:100%;border-collapse:collapse;min-width:760px}.e4detailbox-wrap{overflow:auto}.e4detailbox th,.e4detailbox td{padding:8px 9px;border-bottom:1px solid #e3eaea;text-align:left;vertical-align:top}.e4detailbox th{font-size:12px;color:#5b6d71}.e4draw-card{cursor:pointer}.e4draw-card:hover{box-shadow:0 2px 8px rgba(0,0,0,.10);transform:translateY(-1px)}
</style>
<script>
(function(){
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function e(s){return (window.esc?esc(String(s??'')):String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])))}
 function isE4(){let n=((machines[lang]||[])[currentMachineIndex]||'').toLowerCase();return n.includes('4')&&(n.includes('экструдер')||n.includes('אקסטרודר')||n.includes('extruder'))}
 function sectionKey(){let s=((extruderSections[lang]||[])[currentExtruderSection]||'').toLowerCase();if(s.includes('кал')||s.includes('קלנ')||s.includes('cal'))return'calender';if((s.includes('a')||s.includes('משני'))&&(s.includes('extr')||s.includes('אקס')))return'a';if((s.includes('b')||s.includes('ראשי'))&&(s.includes('extr')||s.includes('אקס')))return'b';return'other'}
 const data={
  calender:{
   drives:[
    {ru:'Привод входного валка',he:'דרייב גליל כניסה',en:'Inlet roll drive',d:'-91U1',model:'ABB ACS 800-01-0011-3',spec:'6.5 kW; Profibus ADD=70',motor:'-91M1'},
    {ru:'Привод центрального валка',he:'דרייב גליל מרכזי',en:'Central roll drive',d:'-95U1',model:'ABB ACS 800-01-0020-3',spec:'12 kW; Profibus ADD=71',motor:'-95M1'},
    {ru:'Привод выходного валка',he:'דרייב גליל יציאה',en:'Outlet roll drive',d:'-99U1',model:'ABB ACS 800-01-0011-3',spec:'6.5 kW; Profibus ADD=72',motor:'-99M1'},
    {ru:'Привод перемещения каландра',he:'דרייב תנועת קלנדר',en:'Calender movement drive',d:'-110U1',model:'ABB ACS 550-01-03A3-4J-404',spec:'0.25 kW',motor:'-110M1'},
    {ru:'Привод охлаждающего валка',he:'דרייב גליל קירור',en:'Cooling roll drive',d:'-120U1',model:'ABB ACS 800-01-0006-3',spec:'6.5 kW; Profibus ADD=73',motor:'-120M1'},
    {ru:'Привод тянущего устройства',he:'דרייב משיכה',en:'Take-off drive',d:'-130U1',model:'ABB ACS 800-01-0005-3',spec:'2.7 kW; Profibus ADD=81',motor:'-130M1'},
    {ru:'Привод прижимного валка',he:'דרייב גליל לחץ',en:'Pressure roll drive',d:'-145U1',model:'ABB ACS 550-01-03A3-4J-404',spec:'0.25 kW; Profibus ADD=75',motor:'-145M1'}
   ],
   motors:[
    {ru:'Мотор входного валка',he:'מנוע גליל כניסה',en:'Inlet roll motor',d:'-91M1',model:'AX 100K.2',spec:'6.5 kW'},
    {ru:'Мотор центрального валка',he:'מנוע גליל מרכזי',en:'Central roll motor',d:'-95M1',model:'AX 100K.4',spec:'12 kW'},
    {ru:'Мотор выходного валка',he:'מנוע גליל יציאה',en:'Outlet roll motor',d:'-99M1',model:'AX 100K.2',spec:'6.5 kW'},
    {ru:'Мотор перемещения каландра',he:'מנוע תנועת קלנדר',en:'Calender movement motor',d:'-110M1',model:'VEM K221R 71G6',spec:'0.25 kW'},
    {ru:'Мотор охлаждающего валка',he:'מנוע גליל קירור',en:'Cooling roll motor',d:'-120M1',model:'AX 80CS.2',spec:'6.5 kW'},
    {ru:'Мотор тянущего устройства',he:'מנוע משיכה',en:'Take-off motor',d:'-130M1',model:'AX 80CS.075',spec:'2.7 kW'},
    {ru:'Мотор прижимного валка',he:'מנוע גליל לחץ',en:'Pressure roll motor',d:'-145M1',model:'VEM K21R 71K4',spec:'0.25 kW'}
   ],
   fans:[{ru:'Вентилятор мотора входного валка',he:'מאוורר מנוע גליל כניסה',en:'Inlet roll motor fan',d:'-94M1',model:'',spec:'0.075 kW'},{ru:'Вентилятор мотора центрального валка',he:'מאוורר מנוע גליל מרכזי',en:'Central roll motor fan',d:'-98M1',model:'',spec:'0.075 kW'}],
   safety:[{ru:'Аварийная цепь каландра',he:'מעגל חירום קלנדר',en:'Calender emergency',d:'',model:'Safety circuit',spec:''},{ru:'Ограждения каландра',he:'שערי קלנדר',en:'Calender gates',d:'',model:'Safety circuit',spec:''}],
   hydraulics:[{ru:'Гидростанция каландра',he:'יחידה הידראולית קלנדר',en:'Calender hydraulic station',d:'',model:'',spec:''},{ru:'Подъём / опускание каландра',he:'הרמה / הורדה קלנדר',en:'Calender up / down',d:'-112M1',model:'',spec:'1.8 kW'}],
   control:[{ru:'Управление каландром',he:'בקרת קלנדר',en:'Calender control',d:'',model:'PLC / I/O signals',spec:'Auxiliary circuits and control signals'}]
  },
  a:{
   drives:[{ru:'Привод экструдера A',he:'דרייב אקסטרודר A',en:'Extruder A drive',d:'-53U1',model:'ABB ACS 800-01-0100-3',spec:'75 kW; Profibus ADD=21',motor:'-53M1'},{ru:'Привод объёмного насоса A',he:'דרייב משאבה נפחית A',en:'Volumetric pump A drive',d:'-38U1',model:'ABB ACS 800-01-0006-3',spec:'3.9 kW; Profibus ADD=26',motor:'-38M1'}],
   motors:[{ru:'Мотор экструдера A',he:'מנוע אקסטרודר A',en:'Extruder A motor',d:'-53M1',model:'ABB M3AA 250 SMB',spec:'75 kW'},{ru:'Мотор объёмного насоса A',he:'מנוע משאבה נפחית A',en:'Volumetric pump A motor',d:'-38M1',model:'LENZE MCA 14L35',spec:'3.9 kW'}]
  },
  b:{
   drives:[{ru:'Привод экструдера B',he:'דרייב אקסטרודר B',en:'Extruder B drive',d:'-61U1',model:'ABB ACS 800-04-0400-3',spec:'315 kW; Profibus ADD=11',motor:'-61M1'},{ru:'Привод объёмного насоса B',he:'דרייב משאבה נפחית B',en:'Volumetric pump B drive',d:'-43U1',model:'ABB ACS 800-01-0030-3',spec:'20.3 kW; Profibus ADD=16',motor:'-43M1'}],
   motors:[{ru:'Мотор экструдера B',he:'מנוע אקסטרודר B',en:'Extruder B motor',d:'-61M1',model:'ABB M2BA 355 SMA4',spec:'315 kW'},{ru:'Мотор объёмного насоса B',he:'מנוע משאבה נפחית B',en:'Volumetric pump B motor',d:'-43M1',model:'LENZE MCA 21X35',spec:'20.3 kW'}]
  },
  main:{
   plc:[{ru:'Главный PLC CPU',he:'CPU ראשי של PLC',en:'Main PLC CPU',d:'-900U2',model:'Siemens CPU 317F-2 PN/DP',spec:'6ES7317-2FK14-0AB0'},{ru:'Карта памяти PLC',he:'כרטיס זיכרון PLC',en:'PLC memory card',d:'-900U2',model:'SIMATIC S7 Micro Memory Card 2 MB',spec:'6ES7953-8LL31-0AA0'}],
   ethernet:[{ru:'Ethernet switch',he:'מתג Ethernet',en:'Ethernet switch',d:'-891U2',model:'Siemens SCALANCE XB008',spec:'6GK5008-0BA00-1AB2'},{ru:'Ethernet switch',he:'מתג Ethernet',en:'Ethernet switch',d:'-891U7',model:'Siemens SCALANCE XB008',spec:'6GK5008-0BA00-1AB2'}],
   power:[{ru:'Модуль селективной защиты 24VDC',he:'מודול הגנה סלקטיבית 24VDC',en:'24VDC selective protection module',d:'-21U3',model:'Siemens SITOP PSE200U',spec:'6EP1961-2BA21; 24VDC / 10A'}]
  }
 };
 function label(x){return x[lang]||x.ru||x.en||''}
 function renderRows(rows){return rows.map(x=>'<tr><td><b>'+e(label(x))+'</b></td><td><b>'+e(x.d||'—')+'</b></td><td>'+e(x.model||'—')+'</td><td>'+e(x.spec||'—')+'</td><td>'+tx('На машине','במכונה','On machine')+'</td><td>0</td></tr>').join('')}
 function show(title,rows,host){let old=document.getElementById('e4AllDetail');if(old)old.remove();let d=document.createElement('div');d.id='e4AllDetail';d.className='e4detailbox';d.innerHTML='<button class="close" onclick="document.getElementById(\'e4AllDetail\').remove()">'+tx('← Закрыть','← סגור','← Close')+'</button><h3>'+e(title)+'</h3><div class="e4detailbox-wrap"><table><thead><tr><th>'+tx('Название','שם','Name')+'</th><th>'+tx('Номер на чертеже','מספר בשרטוט','Drawing designation')+'</th><th>'+tx('Модель / Part No.','דגם / מק״ט','Model / Part No.')+'</th><th>'+tx('Данные','נתונים','Data')+'</th><th>'+tx('Статус','סטטוס','Status')+'</th><th>'+tx('Склад','מחסן','Warehouse')+'</th></tr></thead><tbody>'+renderRows(rows)+'</tbody></table></div>';host.parentNode.insertBefore(d,host.nextSibling)}
 function classifyTitle(t){t=(t||'').toLowerCase();if(t.includes('привод')||t.includes('דרייב')||t.includes('drive')||t.includes('inverter'))return'drives';if(t.includes('мотор')||t.includes('מנוע')||t.includes('motor'))return'motors';if(t.includes('вент')||t.includes('מאוורר')||t.includes('fan'))return'fans';if(t.includes('безопас')||t.includes('בטיחות')||t.includes('safety')||t.includes('emergency'))return'safety';if(t.includes('гидр')||t.includes('הידרא')||t.includes('hydraulic'))return'hydraulics';if(t.includes('управ')||t.includes('בקרה')||t.includes('control'))return'control';if(t.includes('plc')&&t.includes('cpu'))return'plc';if(t.includes('ethernet')||t.includes('связ')||t.includes('תקשורת')||t.includes('communication'))return'ethernet';if(t.includes('24v'))return'power';return''}
 function bindSection(){if(!isE4())return;let box=document.getElementById('e4DrawingGroups');if(!box)return;let sk=sectionKey(),src=data[sk]||{};box.querySelectorAll('.e4draw-card').forEach(c=>{if(c.dataset.e4bound)return;c.dataset.e4bound='1';c.addEventListener('click',function(){let title=(c.querySelector('b')||{}).textContent||'',k=classifyTitle(title),rows=src[k]||[];if(rows.length)show(title,rows,box);else show(title,[{ru:'Раздел присутствует в электрической схеме',he:'הסעיף קיים בשרטוט החשמל',en:'Section exists in the electrical drawing',d:'',model:'',spec:''}],box)})})}
 function bindMain(){if(!isE4())return;let box=document.getElementById('e4MainGroups');if(!box)return;box.querySelectorAll('.e4draw-card').forEach(c=>{if(c.dataset.e4bound)return;c.dataset.e4bound='1';c.addEventListener('click',function(ev){ev.stopPropagation();let title=(c.querySelector('b')||{}).textContent||'',k=classifyTitle(title),rows=data.main[k]||[];if(rows.length)show(title,rows,box)})})}
 const oe=window.openExtruderSection;window.openExtruderSection=function(i){oe(i);setTimeout(bindSection,80)};
 const om=window.openExtruderMainPanel;if(om)window.openExtruderMainPanel=function(){om();setTimeout(bindMain,80)};
 document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(()=>{bindSection();bindMain()},100)));
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
