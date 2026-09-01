def apply(legacy):
    patch = r'''<style>
#e5StationCatalog{margin:10px 0 20px;padding:15px;border:2px solid #9fb8ba;border-radius:14px;background:#fff}.e5st-grid{display:grid;grid-template-columns:repeat(3,minmax(150px,1fr));gap:12px}.e5st-tile{min-height:74px;border:1px solid #cbd8d9;border-radius:11px;background:#f4f8f7;color:#34454b;font-size:14px;font-weight:700;padding:12px;cursor:pointer}.e5st-detail{border:1px solid #cbd8d9;border-radius:12px;padding:14px}.e5st-wrap{overflow:auto;max-height:620px}.e5st-table{width:100%;border-collapse:collapse;min-width:860px}.e5st-table th,.e5st-table td{padding:8px;border-bottom:1px solid #e3eaea;text-align:left;font-size:12px;vertical-align:top}.e5st-table th{position:sticky;top:0;background:#e8f1ef}.e5st-head{display:flex;justify-content:space-between;align-items:center;gap:10px}.e5st-back{padding:8px 12px;border:1px solid #cbd8d9;border-radius:8px;background:#f4f8f7;cursor:pointer}.e5st-location{font-weight:700;margin:3px 0 13px}.e5st-sub{font-size:12px;color:#687b80;margin-bottom:12px}@media(max-width:850px){.e5st-grid{grid-template-columns:repeat(2,minmax(130px,1fr))}}
</style><script>
(function(){
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function esc5(s){return String(s??'').replace(/[&<>\"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[m]))}
 function isTarget(){
   if(Number(currentMachineIndex)===16 && Number(currentExtruderSection)===3)return true;
   let mn=((machines[lang]||[])[currentMachineIndex]||'').toLowerCase();
   let sn=((extruderSections[lang]||[])[currentExtruderSection]||'').toLowerCase();
   return mn.includes('5')&&(mn.includes('экструдер')||mn.includes('אקסטרודר')||mn.includes('extruder'))&&(sn.includes('кал')||sn.includes('קלנ')||sn.includes('cal'));
 }
 const cats=[
  ['drives',['Драйверы в шкафу','דרייבים בארון','Drives in cabinet']],
  ['starters',['Пускатели / защита в шкафу','מתנעים / הגנה בארון','Starters / protection in cabinet']],
  ['contactors',['Контакторы в шкафу','קונטקטורים בארון','Contactors in cabinet']],
  ['io',['PLC / I/O в шкафу','PLC / I/O בארון','PLC / I/O in cabinet']],
  ['safety',['Safety I/O в шкафу','Safety I/O בארון','Safety I/O in cabinet']],
  ['power',['Питание / вспомогательные цепи','ספקים / מעגלי עזר','Power / auxiliary circuits']],
  ['motors',['Моторы участка','מנועי השטח','Field motors']],
  ['sensors',['Датчики участка','חיישני השטח','Field sensors']],
  ['valves',['Клапаны / гидравлика участка','שסתומים / הידראוליקה','Field valves / hydraulics']],
  ['other',['Прочее оборудование участка','ציוד שטח נוסף','Other field equipment']]
 ];
 const D={
  drives:[
   ['Привод','-685U1','ABB','ACS355-03E-01A2-4','CK1 · frame R0'],
   ['PROFINET модуль','-685U7','ABB','FENA-11','CK1'],
   ['Привод клина','-711U1','ABB','BSD0200','0.2 kW axis · CK1'],
   ['Привод клина','-715U1','ABB','BSD0200','0.2 kW axis · CK1'],
   ['Привод клина','-721U1','ABB','BSD0200','0.2 kW axis · CK1'],
   ['Привод клина','-725U1','ABB','BSD0200','0.2 kW axis · CK1'],
   ['Привод перемещения','-751U1','ABB','ACS355-03E-01A9-4','CK1 · frame R0'],
   ['PROFINET модуль','-751U7','ABB','FENA-11','CK1']
  ],
  starters:[
   ['Реверсивный пускатель','-675Q1','Siemens','3RM1302-2AA04','0.4–2.0 A · failsafe'],
   ['Реверсивный пускатель','-678Q1','Siemens','3RM1302-2AA04','0.4–2.0 A · failsafe'],
   ['Реверсивный пускатель','-755Q1','Siemens','3RM1307-2AA04','1.6–7.0 A · failsafe'],
   ['Защита двигателя','-761QM1','Siemens','3RV2011-1JA20 / 3RV2011-1HA20','7–10 A / 5.5–8 A']
  ],
  contactors:[
   ['Контактор','-710KM4','Siemens','3RT2025-2BB40','7.5 kW · 24 VDC · S0'],
   ['Контактор','-710KM5','Siemens','3RT2025-2BB40','7.5 kW · 24 VDC · S0'],
   ['Контактор','-761KM3','Siemens','3RT2016-2BB41','4 kW · 24 VDC · S00']
  ],
  io:[
   ['ET200SP interface','-906A1','Siemens','6ES7155-6AU00-0CN0','IM155-6 PN HF'],
   ['Аналоговый выход AQ','-932A0','Siemens','6ES7135-6HD00-0BA1','AQ 4xU/I ST ET200SP'],
   ['Цифровой вход DI','-959A0','Siemens','6ES7131-6BF60-0AA0','DI 8x24VDC SCR BA'],
   ['Цифровой выход DQ','-976A0','Siemens','6ES7132-6BF60-0AA0','DQ 8x24VDC/0.5A SINK BA']
  ],
  safety:[
   ['Failsafe I/O','-942A0','Siemens','','Safe PLC / F-I/O · CK1'],
   ['Failsafe I/O','-943A0','Siemens','','Safe PLC / F-I/O · CK1'],
   ['Failsafe I/O','-944A0','Siemens','','Safe PLC / F-I/O · CK1'],
   ['Failsafe I/O','-945A0','Siemens','','Safe PLC / F-I/O · CK1']
  ],
  power:[
   ['Вспомогательные цепи шкафа','848','', '', 'CK1 auxiliary circuit'],
   ['Ethernet switch / сеть','900','', '', 'CK1 network section']
  ],
  motors:[
   ['Мотор входного левого клина','-711M1','ABB','BSM0200CN00','0.2 kW · 1.5 A · 91 V · 200 Hz · 3000 rpm'],
   ['Мотор выходного левого клина','-721M1','ABB','BSM0200CN00','0.2 kW · 1.5 A · 91 V · 200 Hz · 3000 rpm'],
   ['Мотор насоса гидростанции','-761M1','', '', 'Calender hydraulic unit']
  ],
  sensors:[
   ['Тензодатчик тяги','791 / 1120','', '', 'Haul-off load cell'],
   ['Пирометр температуры материала','793','', '', 'Material temperature pyrometer'],
   ['Датчик давления валов','768','', '', 'Roll pressure measurement']
  ],
  valves:[['Гидравлические электроклапаны','763–765','', '', 'Calender hydraulic unit']],
  other:[
   ['Jog каландера','785','', '', 'Calender jog'],
   ['Аварийная цепь','786','', '', 'Line emergency'],
   ['Регулирование размотчика','832','', '', 'Unwinder regulation']
  ]
 };
 let selected=null;
 function label(c){return c[1][lang==='he'?1:lang==='en'?2:0]}
 function cleanup(){
   let old=document.getElementById('e5StationCatalog');if(old)old.remove();
   let p=document.getElementById('extruderSectionPage');if(!p)return;
   let grid=p.querySelector('.detail-grid');if(grid)grid.style.display='';
 }
 function render(){
   let p=document.getElementById('extruderSectionPage');
   if(!p||!p.classList.contains('active'))return;
   if(!isTarget()){cleanup();return}
   let old=document.getElementById('e5StationCatalog');if(old)old.remove();
   let generic=p.querySelector('.detail-grid');if(generic)generic.style.display='none';
   let d=document.createElement('div');d.id='e5StationCatalog';
   if(selected){
     let c=cats.find(v=>v[0]===selected),rows=D[selected]||[];
     d.innerHTML='<div class="e5st-head"><h2>'+esc5(label(c))+'</h2><button class="e5st-back" id="e5stBack">'+tx('← Назад','← חזור','← Back')+'</button></div><div class="e5st-location">'+tx('Экструдер 5 · Каландр · электрический шкаф CK1','אקסטרודר 5 · קלנדר · ארון חשמל CK1','Extruder 5 · Calender · electrical cabinet CK1')+'</div><div class="e5st-wrap"><table class="e5st-table"><thead><tr><th>'+tx('Название','שם','Name')+'</th><th>'+tx('Номер на чертеже','מספר בשרטוט','Drawing designation')+'</th><th>'+tx('Производитель','יצרן','Manufacturer')+'</th><th>Part No.</th><th>'+tx('Данные','נתונים','Data')+'</th></tr></thead><tbody>'+rows.map(r=>'<tr>'+r.map(v=>'<td>'+esc5(v)+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>';
   }else{
     d.innerHTML='<h2>'+tx('Каландр — электрическое оборудование','קלנדר — ציוד חשמלי','Calender — electrical equipment')+'</h2><div class="e5st-location">CK1 — '+tx('локальный электрический шкаф каландера','ארון החשמל המקומי של הקלנדר','local calender electrical cabinet')+'</div><div class="e5st-sub">'+tx('Оборудование внутри шкафа и полевое оборудование участка показаны отдельно.','ציוד בתוך הארון וציוד השטח מוצגים בנפרד.','Cabinet equipment and field equipment are shown separately.')+'</div><div class="e5st-grid">'+cats.map(c=>'<button type="button" class="e5st-tile" data-e5cal="'+c[0]+'">'+esc5(label(c))+'</button>').join('')+'</div>';
   }
   let title=document.getElementById('sectionTitle');
   if(title&&title.parentNode===p)title.insertAdjacentElement('afterend',d);else p.insertBefore(d,p.firstChild);
   d.querySelectorAll('[data-e5cal]').forEach(b=>b.onclick=function(e){e.stopPropagation();selected=this.dataset.e5cal;render()});
   let back=document.getElementById('e5stBack');if(back)back.onclick=function(e){e.stopPropagation();selected=null;render()};
 }
 let prev=window.openExtruderSection;
 if(typeof prev==='function'&&!prev.__e5calA3){
   window.openExtruderSection=function(i){selected=null;let r=prev.apply(this,arguments);setTimeout(render,0);setTimeout(render,80);setTimeout(render,250);return r};
   window.openExtruderSection.__e5calA3=true;
 }
 let obs=new MutationObserver(function(){setTimeout(render,0)});
 let page=document.getElementById('extruderSectionPage');if(page)obs.observe(page,{attributes:true,attributeFilter:['class']});
 document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(render,50)));
 setTimeout(render,100);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
