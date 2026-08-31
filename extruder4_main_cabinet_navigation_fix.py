def apply(legacy):
    patch = r'''<style>
/* Main cabinet is a menu first. Detailed equipment is shown only after a tile is opened. */
#e4MainCabinetInventory{display:none!important}
#e4MainGroups{display:block!important}
#e4MainPhysicalDrives,#e4ForcedMainDrives{display:none!important}
</style>
<script>
(function(){
 function tx(ru,he,en){return lang==='he'?he:lang==='en'?en:ru}
 function e(s){return String(s??'').replace(/[&<>"']/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]})}
 function isE4(){var n=((machines[lang]||[])[currentMachineIndex]||'').toLowerCase();return n.indexOf('4')>=0&&(n.indexOf('экструдер')>=0||n.indexOf('אקסטרודר')>=0||n.indexOf('extruder')>=0)}
 var drives=[
 ['-38U1','ABB ACS 800-01-0006-3','Extruder A volumetric pump','3.9 kW; ADD=26'],
 ['-43U1','ABB ACS 800-01-0030-3','Extruder B volumetric pump','20.3 kW; 390 V; 42.5 A; ADD=16'],
 ['-53U1','ABB ACS 800-01-0100-3','Extruder A main motor','75 kW; 400 V; 136 A; ADD=21'],
 ['-61U1','ABB ACS 800-04-0400-3','Extruder B main motor','315 kW; 400 V; 529 A; ADD=11'],
 ['-91U1','ABB ACS 800-01-0011-3','Calender inlet roll','6.5 kW; 380 V; 14.8 A; ADD=70'],
 ['-95U1','ABB ACS 800-01-0020-3','Calender central roll','12 kW; 380 V; 27.5 A; ADD=71'],
 ['-99U1','ABB ACS 800-01-0011-3','Calender outlet roll','6.5 kW; 380 V; 14.8 A; ADD=72'],
 ['-110U1','ABB ACS 550-01-03A3-4J-404','Calender movement','0.25 kW'],
 ['-120U1','ABB ACS 800-01-0006-3','Cooling roll','4.0 kW; 380 V; 10 A; ADD=73'],
 ['-130U1','ABB ACS 800-01-0005-3','Take-off','2.7 kW; 380 V; 7 A; ADD=81'],
 ['-145U1','ABB ACS 550-01-03A3-4J-404','Pressure roll','0.25 kW; ADD=75'],
 ['-152U1','ABB ACS 550-01-04A1-4','Uncoiler 1','Profibus ADD=76'],
 ['-162U1','ABB ACS 550-01-04A1-4','Uncoiler 2','Profibus ADD=77']
 ];
 function closeDetail(){var d=document.getElementById('e4MainSelectedDetail');if(d)d.remove();var old=document.getElementById('e4MainDetail');if(old)old.remove()}
 window.e4ShowMainDrives=function(){
   closeDetail();var h=document.getElementById('extruderMainPanelBlock');if(!h)return;
   var d=document.createElement('div');d.id='e4MainSelectedDetail';d.className='e4detailbox';
   d.innerHTML='<button class="close" onclick="document.getElementById(\'e4MainSelectedDetail\').remove()">'+tx('← Закрыть','← סגור','← Close')+'</button><h3>'+tx('Драйверы — главный электрический шкаф +2','דרייבים — ארון חשמל ראשי +2','Drives — main electrical cabinet +2')+'</h3><div class="e4detailbox-wrap"><table><thead><tr><th>'+tx('Номер на чертеже','מספר בשרטוט','Drawing designation')+'</th><th>'+tx('Драйвер / модель','דרייב / דגם','Drive / model')+'</th><th>'+tx('Назначение','ייעוד','Function')+'</th><th>'+tx('Данные','נתונים','Data')+'</th></tr></thead><tbody>'+drives.map(function(r){return '<tr><td><b>'+e(r[0])+'</b></td><td>'+e(r[1])+'</td><td>'+e(r[2])+'</td><td>'+e(r[3])+'</td></tr>'}).join('')+'</tbody></table></div>';
   h.parentNode.insertBefore(d,h);
 }
 function addDriveTile(){
   if(!isE4())return;var box=document.getElementById('e4MainGroups');if(!box)return;
   box.style.setProperty('display','block','important');
   var grid=box.querySelector('.e4draw-grid');if(!grid)return;
   var old=document.getElementById('e4MainDriveTile');if(old)old.remove();
   var c=document.createElement('div');c.id='e4MainDriveTile';c.className='e4draw-card clickable';c.onclick=window.e4ShowMainDrives;
   c.innerHTML='<b>'+tx('Драйверы / частотные приводы','דרייבים / ממירי תדר','Drives / frequency inverters')+'</b><span>'+tx('Только драйверы, физически установленные в главном шкафу +2','רק הדרייבים שמותקנים פיזית בארון הראשי +2','Only drives physically installed in main cabinet +2')+'</span>';
   grid.appendChild(c);
 }
 function clean(){
   if(!isE4())return;var inv=document.getElementById('e4MainCabinetInventory');if(inv)inv.style.setProperty('display','none','important');
   var p=document.getElementById('e4MainPhysicalDrives');if(p)p.style.setProperty('display','none','important');
   var f=document.getElementById('e4ForcedMainDrives');if(f)f.style.setProperty('display','none','important');
   addDriveTile();
 }
 var oldOpen=window.openExtruderMainPanel;if(typeof oldOpen==='function'){window.openExtruderMainPanel=function(){var r=oldOpen.apply(this,arguments);setTimeout(clean,90);setTimeout(clean,320);return r}}
 document.addEventListener('click',function(){setTimeout(function(){var p=document.getElementById('extruderMainPanelPage');if(p&&p.classList.contains('active'))clean()},120)});
 document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){setTimeout(clean,100)})});
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
