def apply(legacy):
    patch = r'''<style>
.e4draw{margin:14px 0 18px;padding:14px;border:1px solid #cbd8d9;border-radius:13px;background:#f7faf9}.e4draw-title{font-size:17px;font-weight:800;margin-bottom:5px}.e4draw-note{font-size:13px;color:#65777b;margin-bottom:12px}.e4draw-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(145px,1fr));gap:9px}.e4draw-card{border:1px solid #c8d5d6;border-radius:10px;background:#fff;padding:11px;min-height:68px}.e4draw-card b{display:block;margin-bottom:5px}.e4draw-card span{font-size:12px;color:#65777b;line-height:1.35}.e4draw-zero{display:inline-block;margin-top:6px;padding:2px 7px;border-radius:10px;background:#eef3f2;font-size:11px;font-weight:700;color:#52666a}
</style>
<script>
(function(){
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function isE4(){let n=((machines[lang]||[])[currentMachineIndex]||'').toLowerCase();return n.includes('4')&&(n.includes('экструдер')||n.includes('אקסטרודר')||n.includes('extruder'))}
 function sec(){return ((extruderSections[lang]||[])[currentExtruderSection]||'').toLowerCase()}
 const groups={
  calender:[
   ['Приводы / инверторы','דרייבים / ממירים','Drives / inverters','Inlet roll; Central roll; Outlet roll; Calender movement; Cooling roll; Take-off; Pressure roll'],
   ['Моторы','מנועים','Motors','Inlet roll; Central roll; Outlet roll; Coupler; Exit haul-off'],
   ['Вентиляторы моторов','מאווררי מנועים','Motor fans','Inlet; Central; Outlet; Cooling roll; Coupler; Take-off'],
   ['Безопасность / авария','בטיחות / חירום','Safety / emergency','Calender emergency; Gates; Exit haul-off emergency'],
   ['Гидравлика','הידראוליקה','Hydraulics','Calender oleodynamic station; Down / up'],
   ['Управление','בקרה','Control','Auxiliary circuits; valves; control signals']
  ],
  a:[
   ['Приводы / инверторы','דרייבים / ממירים','Drives / inverters','Extruder A motor; Volumetric pump A'],
   ['Моторы','מנועים','Motors','Extruder A; Volumetric pump A'],
   ['Вентиляторы','מאווררים','Fans','Extruder A motor fan; Pump motor fan'],
   ['Вакуум','ואקום','Vacuum','Extruder A vacuum pump 1'],
   ['Дозирование','מינון','Dosing','Extruder A dosing'],
   ['Безопасность / STO','בטיחות / STO','Safety / STO','Emergency; STO; safety I/O']
  ],
  b:[
   ['Приводы / инверторы','דרייבים / ממירים','Drives / inverters','Extruder B motor; Volumetric pump B'],
   ['Моторы','מנועים','Motors','Extruder B; Volumetric pump B'],
   ['Вентиляторы','מאווררים','Fans','Extruder B motor fan; Pump motor fan'],
   ['Вакуум / дегазация','ואקום / דגזינג','Vacuum / degassing','Vacuum pumps 1–3; degassing'],
   ['Азот / клапаны','חנקן / שסתומים','Nitrogen / valves','Nitrogen S.V. circuit'],
   ['Безопасность / STO','בטיחות / STO','Safety / STO','Emergency; STO; safety I/O']
  ],
  main:[
   ['PLC / CPU','PLC / CPU','PLC / CPU','PLC layouts and CPU'],
   ['I/O модули','מודולי I/O','I/O modules','Standard and safety I/O'],
   ['Безопасность PLC','PLC בטיחות','Safety PLC','Safe PLC racks / modules'],
   ['Питание 24VDC','ספקי 24VDC','24VDC supplies','24VDC supply'],
   ['Ethernet / связь','Ethernet / תקשורת','Ethernet / communication','Ethernet switches; Profibus'],
   ['Главное питание','הזנה ראשית','Main supply','General supply and auxiliary circuits']
  ]
 };
 function choose(){let s=sec();if(s.includes('кал')||s.includes('קלנ')||s.includes('cal'))return groups.calender;if((s.includes('a')||s.includes('משני'))&&(s.includes('extr')||s.includes('אקס')))return groups.a;if((s.includes('b')||s.includes('ראשי'))&&(s.includes('extr')||s.includes('אקס')))return groups.b;return null}
 function render(){let host=document.getElementById('extruderSectionPage');if(!host||!host.classList.contains('active')||!isE4())return;let old=document.getElementById('e4DrawingGroups');if(old)old.remove();let g=choose();if(!g)return;let d=document.createElement('div');d.id='e4DrawingGroups';d.className='e4draw';d.innerHTML='<div class="e4draw-title">'+tx('Оборудование по электрическим чертежам','ציוד לפי שרטוטי החשמל','Equipment from electrical drawings')+'</div><div class="e4draw-note">'+tx('Структура Экструдера 4 по заводским схемам. Складской запас будет показываться отдельно.','מבנה אקסטרודר 4 לפי שרטוטי היצרן. מלאי המחסן יוצג בנפרד.','Extruder 4 structure from manufacturer drawings. Warehouse stock is shown separately.')+'</div><div class="e4draw-grid">'+g.map(x=>'<div class="e4draw-card"><b>'+x[lang==='he'?1:lang==='en'?2:0]+'</b><span>'+x[3]+'</span><div class="e4draw-zero">'+tx('Склад: 0 / проверить','מחסן: 0 / לבדוק','Warehouse: 0 / check')+'</div></div>').join('')+'</div>';let p=document.getElementById('extruderSectionPanelBlock')||document.getElementById('extruderPartsInline');host.insertBefore(d,p||host.firstChild)}
 const old=window.openExtruderSection;window.openExtruderSection=function(i){old(i);setTimeout(render,20)};
 const oldMain=window.openExtruderMainPanel;if(oldMain)window.openExtruderMainPanel=function(){oldMain();setTimeout(function(){if(!isE4())return;let h=document.getElementById('extruderMainPanelBlock');if(!h)return;let o=document.getElementById('e4MainGroups');if(o)o.remove();let d=document.createElement('div');d.id='e4MainGroups';d.className='e4draw';d.innerHTML='<div class="e4draw-title">'+tx('Оборудование по электрическим чертежам','ציוד לפי שרטוטי החשמל','Equipment from electrical drawings')+'</div><div class="e4draw-grid">'+groups.main.map(x=>'<div class="e4draw-card"><b>'+x[lang==='he'?1:lang==='en'?2:0]+'</b><span>'+x[3]+'</span></div>').join('')+'</div>';h.parentNode.insertBefore(d,h)} ,20)};
 document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(render,30)));
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
