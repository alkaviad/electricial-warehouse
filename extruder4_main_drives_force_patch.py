def apply(legacy):
    patch = r'''<style>
#e4ForcedMainDrives{margin:14px 0 18px;padding:14px;border:2px solid #9fb7b9;border-radius:13px;background:#fff}
#e4ForcedMainDrives h3{margin:0 0 5px;font-size:18px}#e4ForcedMainDrives .note{font-size:13px;color:#5f7276;margin-bottom:10px}
#e4ForcedMainDrives .wrap{overflow:auto;max-height:560px}#e4ForcedMainDrives table{width:100%;border-collapse:collapse;min-width:900px}
#e4ForcedMainDrives th,#e4ForcedMainDrives td{padding:8px;border-bottom:1px solid #e2e9e9;text-align:left;vertical-align:top}
#e4ForcedMainDrives th{position:sticky;top:0;background:#f6faf9;font-size:12px;color:#52666a;z-index:1}
</style><script>
(function(){
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function esc4(s){return String(s||'').replace(/[&<>"']/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]})}
 function isE4(){var n=((machines[lang]||[])[currentMachineIndex]||'').toLowerCase();return n.indexOf('4')>=0&&(n.indexOf('экструдер')>=0||n.indexOf('אקסטרודר')>=0||n.indexOf('extruder')>=0)}
 var drives=[
 ['-38U1','ABB ACS 800-01-0005-3','Extruder A volumetric pump','3.9 kW'],
 ['-43U1','ABB ACS 800-01-0030-3','Extruder B volumetric pump','20.3 kW; 390 V; 42.5 A'],
 ['-53U1','ABB ACS 800-01-0100-3','Extruder A main motor','75 kW; 400 V; 136 A'],
 ['-61U1','ABB ACS 800-04-0400-3','Extruder B main motor','315 kW; 400 V; 529 A'],
 ['-91U1','ABB ACS 800-01-0011-3','Calender inlet roll','6.5 kW; 380 V; 14.8 A'],
 ['-95U1','ABB ACS 800-01-0020-3','Calender central roll','12 kW; 380 V; 27.5 A'],
 ['-99U1','ABB ACS 800-01-0011-3','Calender outlet roll','6.5 kW; 380 V; 14.8 A'],
 ['-110U1','ABB ACS 550-01-03A3-4J-404','Calender movement','0.25 kW'],
 ['-120U1','ABB ACS 800-01-0006-3','Cooling roll','4.0 kW; 380 V; 10 A'],
 ['-130U1','ABB ACS 800-01-0005-3','Take-off','2.7 kW; 380 V; 7 A'],
 ['-145U1','ABB ACS 550-01-03A3-4J-404','Pressure roll','0.25 kW; 400 V; 0.78 A'],
 ['-152U1','ABB ACS 550-01-04A1-4','Uncoiler 1','Profibus ADD=76'],
 ['-162U1','ABB ACS 550-01-04A1-4','Uncoiler 2','Profibus ADD=77']
 ];
 function render(){
  if(!isE4())return;
  var host=document.getElementById('extruderMainPanelPage')||document.getElementById('extruderMainPanelBlock');if(!host)return;
  var old=document.getElementById('e4ForcedMainDrives');if(old)old.remove();
  var box=document.createElement('div');box.id='e4ForcedMainDrives';
  box.innerHTML='<h3>'+tx('Драйверы / частотные приводы — главный шкаф +2','דרייבים / ממירי תדר — ארון ראשי +2','Drives / frequency inverters — main cabinet +2')+'</h3><div class="note">'+tx('Здесь показываются приводы по физическому месту установки в центральном шкафу, независимо от того, какой узел машины они приводят.','כאן מוצגים הדרייבים לפי מקום ההתקנה הפיזי בארון הראשי, בלי קשר לאיזה חלק במכונה הם שייכים.','Drives are listed here by physical installation in the main cabinet, regardless of the machine section they operate.')+'</div><div class="wrap"><table><thead><tr><th>'+tx('Номер на чертеже','מספר בשרטוט','Drawing designation')+'</th><th>'+tx('Модель / Part No.','דגם / מק״ט','Model / Part No.')+'</th><th>'+tx('Назначение','תפקיד','Function')+'</th><th>'+tx('Данные','נתונים','Data')+'</th></tr></thead><tbody>'+drives.map(function(r){return '<tr><td><b>'+esc4(r[0])+'</b></td><td>'+esc4(r[1])+'</td><td>'+esc4(r[2])+'</td><td>'+esc4(r[3])+'</td></tr>'}).join('')+'</tbody></table></div>';
  var anchor=document.getElementById('extruderMainPanelBlock');if(anchor&&anchor.parentNode)anchor.parentNode.insertBefore(box,anchor);else host.insertBefore(box,host.firstChild);
 }
 function hook(){var f=window.openExtruderMainPanel;if(typeof f==='function'&&!f.__e4forced){var w=function(){var r=f.apply(this,arguments);setTimeout(render,40);setTimeout(render,250);return r};w.__e4forced=true;window.openExtruderMainPanel=w}}
 hook();document.addEventListener('DOMContentLoaded',hook);document.addEventListener('click',function(){setTimeout(function(){hook();var p=document.getElementById('extruderMainPanelPage');if((p&&p.classList.contains('active'))||document.getElementById('extruderMainPanelBlock'))render()},80)});document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){setTimeout(render,80)})});
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
