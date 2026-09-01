def apply(legacy):
    patch = r'''<style>
/* A8 — fully isolated Extruder 5 / Extruder B mini-program, rebuilt from drawings. */
#extruderSectionPage.e5-exb-private > *{display:none!important}
#extruderSectionPage.e5-exb-private > #e5ExBPrivate{display:block!important}
#e5ExBPrivate{margin:10px 0 20px;padding:15px;border:2px solid #9fb8ba;border-radius:14px;background:#fff}
.e5xb-grid{display:grid;grid-template-columns:repeat(3,minmax(160px,1fr));gap:12px}.e5xb-tile{min-height:86px;border:1px solid #cbd8d9;border-radius:11px;background:#f4f8f7;color:#34454b;font-size:14px;font-weight:700;padding:12px;cursor:pointer}.e5xb-head{display:flex;justify-content:space-between;align-items:center;gap:10px}.e5xb-back{padding:8px 12px;border:1px solid #cbd8d9;border-radius:8px;background:#f4f8f7;cursor:pointer;font-weight:700}.e5xb-sub{font-size:12px;color:#687b80;margin:5px 0 12px}.e5xb-wrap{overflow:auto;max-height:680px}.e5xb-table{width:100%;border-collapse:collapse;min-width:1100px}.e5xb-table th,.e5xb-table td{padding:8px;border-bottom:1px solid #e3eaea;text-align:left;font-size:12px;vertical-align:top}.e5xb-table th{position:sticky;top:0;background:#e8f1ef;z-index:1}@media(max-width:850px){.e5xb-grid{grid-template-columns:repeat(2,minmax(130px,1fr))}}
</style><script>
(function(){
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function esc(s){return String(s==null?'':s).replace(/[&<>\"']/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[m]})}
 function target(si){try{var mi=Number(currentMachineIndex),s=si==null?Number(currentExtruderSection):Number(si);if(mi===16&&s===2)return true;var mn=((machines[lang]||[])[mi]||'').toLowerCase(),sn=((extruderSections[lang]||[])[s]||'').toLowerCase();return mn.indexOf('5')>=0&&(mn.indexOf('экструдер')>=0||mn.indexOf('אקסטרודר')>=0||mn.indexOf('extruder')>=0)&&(sn.indexOf('экструдер b')>=0||sn.indexOf('extruder b')>=0||sn.indexOf(' b')>=0)}catch(e){return false}}
 var cats=[
  ['main',['Главный мотор / привод Extruder B','מנוע / הנעה ראשית Extruder B','Extruder B main motor / drive']],
  ['barrel',['CB1 — зоны нагрева цилиндра','CB1 — אזורי חימום צילינדר','CB1 — barrel heating zones']],
  ['ssr',['CB1 — SSR / предохранители','CB1 — SSR / נתיכים','CB1 — SSR / fuses']],
  ['pid',['CB1 — термопары / PID / PLC','CB1 — תרמוקפלים / PID / PLC','CB1 — thermocouples / PID / PLC']],
  ['cooling',['CB1 — охлаждение / электроклапаны','CB1 — קירור / שסתומים חשמליים','CB1 — cooling / solenoid valves']],
  ['aux',['CB1 — смазка / термостатирование','CB1 — סיכה / תרמוסטט','CB1 — lubrication / thermostatic unit']],
  ['cb3heat',['CB3 — screenchanger / pump / pipes heating','CB3 — חימום מחליף מסנן / משאבה / צנרת','CB3 — screenchanger / pump / pipes heating']],
  ['cb3io',['CB3 — PLC / I/O / Safety','CB3 — PLC / I/O / Safety','CB3 — PLC / I/O / Safety']],
  ['meltpump',['Насос расплава B / привод','משאבת התך B / הנעה','Melt pump B / drive']],
  ['cb4',['CB4 — вакуумные насосы / клапаны / I/O','CB4 — משאבות ואקום / שסתומים / I/O','CB4 — vacuum pumps / valves / I/O']]
 ];
 function row(n,d,m,p,data){return[n,d,m,p,data]}
 var D={
 main:[
  row('Главный двигатель Extruder B','-81M2','ABB','M3BP 355 SMB4','315 kW · 550 A · 400 V · 50 Hz · 1488 rpm · cosφ 0.86'),
  row('Преобразователь частоты главного двигателя','-81U2','ABB','ACS880-04-585A-3','Drive for Extruder B main motor'),
  row('Сетевой фильтр','-81V2','','FN3270H-600-99','600 A'),
  row('Предохранитель привода','-81FU2','','170M6814D','1000 A aR'),
  row('Вентилятор главного двигателя','-84M1','','','0.75 kW · 1.65 A · 400 V · 50 Hz · 3~'),
  row('Пускатель вентилятора','-84Q1','Siemens','3RA6120-2CB32','1–4 A · Class 10'),
  row('Safety output вентилятора','-963A0','Siemens','6ES7136-6DB00-0CA0','F-DQ 4x24VDC/2A PM HF · channel DQ2 · Q557.2'),
  row('Feedback/protection вентилятора','-952A0','Siemens','6ES7131-6BF00-0BA0','DI 8x24VDC ST · DI6 · I678.6')
 ],
 barrel:[
  row('Зона 1 — нагреватели','-401R1','','','13.5 kW · 19.51 A · 3×4.5 kW'),
  row('Зона 2 — нагреватели','-402R1','','','10.5 kW · 15.17 A · 3×3.5 kW'),
  row('Зона 3 — нагреватели','-403R1 / -403R2','','','6.5 kW · 9.39 A · 2 kW + 2 kW + 2.5 kW'),
  row('Зона 4 — нагреватели','-404R1','','','8.0 kW · 11.56 A · 3×2.67 kW'),
  row('Зона 5 — нагреватели','-405R1 / -405R2','','','5.5 kW · 7.95 A · 1.75 + 1.75 + 2.0 kW'),
  row('Зона 6 — нагреватели','-406R1','','','8.0 kW · 11.56 A · 3×2.67 kW'),
  row('Зона 7 — нагреватели','-407R1 / -407R2','','','5.5 kW · 7.95 A · 2.0 + 1.75 + 1.75 kW'),
  row('Зона 8 — нагреватели','-408R1','','','8.0 kW · 11.56 A · 3×2.67 kW'),
  row('Зона 9 — нагреватели','-409R1','','','7.5 kW · 10.84 A · 3×2.5 kW'),
  row('Зона 10 — нагреватели','-410R1','','','5.5 kW · 7.95 A · 2 + 2 + 1.5 kW'),
  row('Зона 11 — нагреватели','-411R1','','','7.5 kW · 10.84 A · 3×2.5 kW'),
  row('Зона 12 — нагреватели','-412R1','','','7.5 kW · 10.84 A · 3×2.5 kW'),
  row('Дегазация 1 — нагреватели','-413R2','','','0.8 kW · 3.48 A · 2×0.4 kW'),
  row('Дегазация 2 — нагреватели','-414R2','','','0.8 kW · 3.48 A · 2×0.4 kW'),
  row('Адаптер сменщика фильтра — нагреватели','-415R2','','','4.0 kW · 17.39 A · 0.6 + 0.6 + 2.0 + 0.8 kW')
 ],
 ssr:[
  row('SSR зона 1','-401KP1 / -401KP2 / -401KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 2','-402KP1 / -402KP2 / -402KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 3','-403KP1 / -403KP2 / -403KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 4','-404KP1 / -404KP2 / -404KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 5','-405KP1 / -405KP2 / -405KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 6','-406KP1 / -406KP2 / -406KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 7','-407KP1 / -407KP2 / -407KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 8','-408KP1 / -408KP2 / -408KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 9','-409KP1 / -409KP2 / -409KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 10','-410KP1 / -410KP2 / -410KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 11','-411KP1 / -411KP2 / -411KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR зона 12','-412KP1 / -412KP2 / -412KP3','Carlo Gavazzi','RGS1A60D50KKE','3 pcs · 50 A · control 24 VDC'),
  row('SSR дегазация 1','-413KP2','Carlo Gavazzi','RGS1A60D50KKE','1 pc · 50 A · control 24 VDC'),
  row('SSR дегазация 2','-414KP2','Carlo Gavazzi','RGS1A60D50KKE','1 pc · 50 A · control 24 VDC'),
  row('SSR адаптер screenchanger','-415KP2','Carlo Gavazzi','RGS1A60D50KKE','1 pc · 50 A · control 24 VDC'),
  row('Fuse zone 1','-401FU2','Siba','5017906.25','3×25 A gR 10x38'),row('Fuse zone 2','-402FU2','Siba','5017906.20','3×20 A gR 10x38'),row('Fuse zone 3','-403FU2','Siba','5017906.16','3×16 A gR 10x38'),row('Fuse zone 4','-404FU2','Siba','5017906.20','3×20 A gR 10x38'),row('Fuse zone 5','-405FU2','Siba','5017906.16','3×16 A gR 10x38'),row('Fuse zone 6','-406FU2','Siba','5017906.20','3×20 A gR 10x38'),row('Fuse zone 7','-407FU2','Siba','5017906.16','3×16 A gR 10x38'),row('Fuse zone 8','-408FU2','Siba','5017906.20','3×20 A gR 10x38'),row('Fuse zone 9','-409FU2','Siba','5017906.20','3×20 A gR 10x38'),row('Fuse zone 10','-410FU2','Siba','5017906.16','3×16 A gR 10x38'),row('Fuse zone 11','-411FU2','Siba','5017906.20','3×20 A gR 10x38'),row('Fuse zone 12','-412FU2','Siba','5017906.20','3×20 A gR 10x38'),row('Fuse degassing 1','-413FU2','Siba','5017906.10','10 A gR'),row('Fuse degassing 2','-414FU2','Siba','5017906.10','10 A gR'),row('Fuse screenchanger adapter','-415FU2','Siba','5017906.25','25 A gR')
 ],
 pid:[
  row('ET200SP interface','-906A1','Siemens','6ES7155-6AU00-0CN0','IM155-6 PN HF'),
  row('AI current module','-912A0','Siemens','6ES7134-6GD00-0BA1','AI 4xI 2-/4-wire ST · 4 channels'),
  row('Thermocouple module','-922A0','Siemens','6ES7134-6JF00-0CA1','AI 8xRTD/TC HF · 8 channels · zones 1–8'),
  row('Thermocouple module','-924A0','Siemens','6ES7134-6JF00-0CA1','AI 8xRTD/TC HF · 8 channels · zones 9–15 / auxiliaries'),
  row('RTD/TC module','-925A0','Siemens','6ES7134-6JD00-0CA1','AI 4xRTD/TC HF · lubrication/auxiliary temperatures'),
  row('F-DI safety','-942A0','Siemens','6ES7136-6BA00-0CA0','8 safety digital inputs'),
  row('DI module','-952A0','Siemens','6ES7131-6BF00-0BA0','8 digital inputs'),row('DI module','-953A0','Siemens','6ES7131-6BF00-0BA0','8 digital inputs'),
  row('F-DQ safety','-962A0','Siemens','6ES7136-6DB00-0CA0','4 safety digital outputs'),
  row('Heating output module','-972A0','Siemens','6ES7132-6BF00-0BA0','DQ 8x24VDC/0.5A · Q650.0…Q651.x · PID heating commands'),
  row('Heating/output module','-973A0','Siemens','6ES7132-6BF00-0BA0','DQ 8x24VDC/0.5A'),
  row('Relay output module','-976A0','Siemens','6ES7132-6HD00-0BB1','RQ 4x120VDC/230VAC 5A NO'),
  row('Cooling output module','-982A0','Siemens','6ES7132-6BD20-0BA0','DQ 4x24VDC/2A · cooling zones 2–5'),
  row('Cooling output module','-983A0','Siemens','6ES7132-6BD20-0BA0','DQ 4x24VDC/2A · cooling zones 6–9'),
  row('Cooling output module','-984A0','Siemens','6ES7132-6BD20-0BA0','DQ 4x24VDC/2A · cooling zones 10–12 + thermostatic bypass'),
  row('Zone 1 thermocouple','-401ST4','','','IW1064 · -922A0 channel 1'),row('Zone 2 thermocouple','-402ST4','','','IW1066 · -922A0 channel 2'),row('Zone 3 thermocouple','-403ST4','','','IW1068 · -922A0 channel 3'),row('Zone 4 thermocouple','-404ST4','','','IW1070 · -922A0 channel 4')
 ],
 cooling:[
  row('Cooling valve zone 2','-402YV6','','','14 W · Q654.0 · -982A0 DQ0'),row('Cooling valve zone 3','-403YV6','','','14 W · Q654.1 · -982A0 DQ1'),row('Cooling valve zone 4','-404YV6','','','14 W · Q654.2 · -982A0 DQ2'),row('Cooling valve zone 5','-405YV6','','','14 W · Q654.3 · -982A0 DQ3'),row('Cooling valve zone 6','-406YV6','','','14 W · Q655.0 · -983A0 DQ0'),row('Cooling valve zone 7','-407YV6','','','14 W · Q655.1 · -983A0 DQ1'),row('Cooling valve zone 8','-408YV6','','','14 W · Q655.2 · -983A0 DQ2'),row('Cooling valve zone 9','-409YV6','','','14 W · Q655.3 · -983A0 DQ3'),row('Cooling valve zone 10','-410YV6','','','14 W · Q656.0 · -984A0 DQ0'),row('Cooling valve zone 11','-411YV6','','','14 W · Q656.1 · -984A0 DQ1'),row('Cooling valve zone 12','-412YV6','','','14 W · Q656.2 · -984A0 DQ2'),row('Thermostatic unit bypass valve','-421YV6','','','14 W · Q656.3 · -984A0 DQ3')
 ],
 aux:[
  row('Насос смазки — мотор','-85M1','','','1.1 kW · 3 A · 400 V · 50 Hz · 3~'),row('Пускатель насоса смазки','-85Q1','Siemens','3RA6120-2CB32','1–4 A · Class 10'),row('MIN pressure lubrication','-85SP5','','','DI I650.6'),row('MAX pressure lubrication','-85SP6','','','DI I650.7'),row('Температура масла смазки','-925A0','Siemens','6ES7134-6JD00-0CA1','AI · IW1086'),row('Thermostatic unit','+TU / +EB-L1,L2,L3','','','Cylinder thermostatic unit · 3-phase supply'),row('Thermostatic thermocouple','+TU-X1','','','IW1094')
 ],
 cb3heat:[
  row('CB3 main heating contactor','-400KM7','Siemens','3RT2038-3KB40','37 kW · 24 VDC coil'),row('CT phase 1','-400TA2','IME','TABB50C100','100/5 A'),row('CT phase 2','-400TA2.1','IME','TABB50C100','100/5 A'),row('CT phase 3','-400TA2.2','IME','TABB50C100','100/5 A'),
  row('Screenchanger zone SSR','-401KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · 24 VDC · fuse 20 A gR'),row('Heating zone SSR group','-402KP1 / KP2 / KP3','Carlo Gavazzi','RGS1A60D50KKE','3×50 A · fuse 3×20 A gR'),row('Heating zone SSR group','-403KP1 / KP2 / KP3','Carlo Gavazzi','RGS1A60D50KKE','3×50 A · fuse 3×20 A gR'),row('Heating zone SSR group','-404KP1 / KP3','Carlo Gavazzi','RGS1A60D50KKE','2×50 A · fuse 2×10 A gR'),row('Heating zone SSR group','-405KP1 / KP3','Carlo Gavazzi','RGS1A60D50KKE','2×50 A · fuse 2×10 A gR'),row('Heating zone SSR group','-406KP1 / KP3','Carlo Gavazzi','RGS1A60D50KKE','2×50 A · fuse 2×10 A gR'),row('Pipe zone SSR','-407KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 16 A gR'),row('Pipe zone SSR','-408KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 25 A gR'),row('Pipe zone SSR','-409KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 20 A gR'),row('Pipe zone SSR','-410KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 16 A gR'),row('Pipe zone SSR','-411KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 20 A gR'),row('Pipe zone SSR','-412KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 25 A gR'),row('Pipe zone SSR','-413KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 16 A gR'),row('Pipe zone SSR','-414KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 25 A gR'),row('Pipe zone SSR','-415KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 16 A gR'),row('Pipe zone SSR','-416KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 16 A gR'),row('Pipe zone SSR','-417KP2','Carlo Gavazzi','RGS1A60D50KKE','50 A · fuse 10 A gR')
 ],
 cb3io:[
  row('ET200SP interface','-906A1','Siemens','6ES7155-6AU00-0CN0','IM155-6 PN HF'),row('AI current','-912A0','Siemens','6ES7134-6GD00-0BA1','4 analog inputs'),row('TC module','-922A0','Siemens','6ES7134-6JF00-0CA1','8 RTD/TC channels'),row('TC module','-923A0','Siemens','6ES7134-6JF00-0CA1','8 RTD/TC channels'),row('TC module','-924A0','Siemens','6ES7134-6JF00-0CA1','8 RTD/TC channels'),row('TC module','-925A0','Siemens','6ES7134-6JF00-0CA1','8 RTD/TC channels'),row('F-DI','-942A0','Siemens','6ES7136-6BA00-0CA0','8 safety inputs'),row('DI','-952A0','Siemens','6ES7131-6BF00-0BA0','8 digital inputs'),row('F-DQ','-962A0','Siemens','6ES7136-6DB00-0CA0','4 safety outputs'),row('DQ','-972A0','Siemens','6ES7132-6BF00-0BA0','8 outputs'),row('DQ','-973A0','Siemens','6ES7132-6BF00-0BA0','8 outputs'),row('DQ','-974A0','Siemens','6ES7132-6BF00-0BA0','8 outputs'),row('Relay outputs','-976A0','Siemens','6ES7132-6HD00-0BB1','4 relay outputs 5 A'),row('Relay outputs','-977A0','Siemens','6ES7132-6HD00-0BB1','4 relay outputs 5 A')
 ],
 meltpump:[
  row('Melt / volumetric pump B motor','-101M2','Lenze','MCA 21X35','20.3 kW · 42.5 A · 390 V · 120 Hz · 3520 rpm · cosφ 0.80'),row('Melt pump B drive','-101U2','ABB','ACS880-01-045A-3','Variable speed drive'),row('Ethernet adapter','-102U7','ABB','FENA-11','IP 192.168.28.115 · PN 15'),row('Input filter','-101V2','','FN3270H-50-34','50 A'),row('Fuse','-101FU2','Siemens','3NA3822-7','63 A gG/gL'),row('Melt pump B motor fan','-104M1','','','0.09 kW · 0.26 A · 230 V · 50 Hz · 1~'),row('Fan starter','-104Q1','Siemens','3RA6120-2AB32','0.1–0.4 A · Class 10'),row('Fan safety output','-963A0','Siemens','6ES7136-6DB00-0CA0','DQ3 · Q557.3'),row('Fan protection input','-952A0','Siemens','6ES7131-6BF00-0BA0','DI7 · I678.7')
 ],
 cb4:[
  row('Vacuum pump starter 1','-105Q1','Siemens','3RA6120-2EB32','24 VDC compact starter'),row('Vacuum pump starter 2','-105Q6','Siemens','3RA6120-2EB32','24 VDC compact starter'),row('Vacuum pump starter 3','-106Q1','Siemens','3RA6120-2EB32','24 VDC compact starter'),row('24 VDC power supply','-21U1','Siemens','6EP1333-3BA10','SITOP PSU200M 5 A'),row('Selective protection','-21U3','Siemens','6EP1961-2BA21','SITOP PSE200U 10 A'),row('ET200SP interface','-906A1','Siemens','6ES7155-6AU00-0CN0','IM155-6 PN HF'),row('AI module','-912A0','Siemens','6ES7134-6GD00-0BA1','4 analog current inputs'),row('AI module','-913A0','Siemens','6ES7134-6GD00-0BA1','4 analog current inputs'),row('RTD/TC modules','-925A0','Siemens','6ES7134-6JD00-0CA1','2 modules · temperature channels'),row('DI','-952A0','Siemens','6ES7131-6BF00-0BA0','8 digital inputs'),row('DI','-953A0','Siemens','6ES7131-6BF00-0BA0','8 digital inputs'),row('F-DQ','-962A0','Siemens','6ES7136-6DB00-0CA0','4 safety outputs'),row('F-DQ','-966A0','Siemens','6ES7136-6DB00-0CA0','4 safety outputs'),row('DQ','-983A0','Siemens','6ES7132-6BF00-0BA0','8 outputs · pump commands / panel commands'),row('Vacuum pump command 1','110b / Q941.0','','','-983A0 DQ0'),row('Vacuum pump command 2','110b / Q941.1','','','-983A0 DQ1'),row('Vacuum pump command 3','110b / Q941.2','','','-983A0 DQ2'),row('Degassing air temperature sensors','+VB-110aR1…R4','','','4 temperature channels to -925A0')
 ]
 };
 var selected=null;
 function label(c){return c[1][lang==='he'?1:lang==='en'?2:0]}
 function cleanup(){var x=document.getElementById('e5ExBPrivate');if(x)x.remove();var p=document.getElementById('extruderSectionPage');if(p)p.classList.remove('e5-exb-private')}
 function render(){var p=document.getElementById('extruderSectionPage');if(!p||!p.classList.contains('active')||!target()){cleanup();return}p.classList.add('e5-exb-private');var d=document.getElementById('e5ExBPrivate');if(!d){d=document.createElement('div');d.id='e5ExBPrivate';p.appendChild(d)}
 if(selected){var c=cats.find(function(x){return x[0]===selected}),rows=D[selected]||[];d.innerHTML='<div class="e5xb-head"><h2>'+esc(label(c))+'</h2><button class="e5xb-back" id="e5xbCatBack">'+tx('← Назад','← חזרה','← Back')+'</button></div><div class="e5xb-sub">S.3909 · OR16/268 · Extruder B · sources: C1 / CB1 / CB3 / CB4</div><div class="e5xb-wrap"><table class="e5xb-table"><thead><tr><th>'+tx('Оборудование','ציוד','Equipment')+'</th><th>'+tx('Номер на чертеже','מספר בשרטוט','Drawing designation')+'</th><th>'+tx('Производитель','יצרן','Manufacturer')+'</th><th>Part No.</th><th>'+tx('Точные данные с чертежа','נתונים מדויקים מהשרטוט','Exact drawing data')+'</th></tr></thead><tbody>'+rows.map(function(r){return '<tr>'+r.map(function(v){return '<td>'+esc(v)+'</td>'}).join('')+'</tr>'}).join('')+'</tbody></table></div>'}else{d.innerHTML='<button class="e5xb-back" id="e5xbMainBack">'+tx('← Назад','← חזרה','← Back')+'</button><h2>'+tx('Экструдер B — электрическое оборудование','אקסטרודר B — ציוד חשמלי','Extruder B — electrical equipment')+'</h2><div class="e5xb-sub">'+tx('Отдельный модуль. Данные перенесены поэлементно из S.3909: C1, CB1, CB3, CB4.','מודול נפרד. הנתונים הועברו רכיב-רכיב מ-S.3909: C1, CB1, CB3, CB4.','Isolated module. Component-level data from S.3909: C1, CB1, CB3, CB4.')+'</div><div class="e5xb-grid">'+cats.map(function(c){return '<button class="e5xb-tile" data-e5xb="'+c[0]+'">'+esc(label(c))+'</button>'}).join('')+'</div>'}
 d.querySelectorAll('[data-e5xb]').forEach(function(b){b.onclick=function(e){e.preventDefault();e.stopPropagation();selected=this.dataset.e5xb;render()}});var b=document.getElementById('e5xbCatBack');if(b)b.onclick=function(e){e.preventDefault();e.stopPropagation();selected=null;render()};b=document.getElementById('e5xbMainBack');if(b)b.onclick=function(e){e.preventDefault();e.stopPropagation();cleanup();if(typeof openExtruder==='function')openExtruder(currentMachineIndex)}}
 var prev=window.openExtruderSection;if(typeof prev==='function'&&!prev.__e5xbPrivateA8Detailed){window.openExtruderSection=function(i){var t=target(i);selected=null;if(!t){cleanup();return prev.apply(this,arguments)}var r=prev.apply(this,arguments);setTimeout(render,0);return r};window.openExtruderSection.__e5xbPrivateA8Detailed=true}
 document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){if(target())setTimeout(render,0)})});
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
