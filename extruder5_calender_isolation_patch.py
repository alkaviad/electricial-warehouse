def apply(legacy):
    patch = r'''<style>
/* Extruder 5 / Calender only. This patch never changes global station layout. */
#extruderSectionPage.e5-calender-isolated > #e5StationCatalog{display:block!important}
#extruderSectionPage.e5-calender-isolated > #e4StationCatalog{display:none!important}
#e5StationCatalog #e5CalenderMainBack{display:inline-block;margin:0 0 12px;padding:8px 12px;border:1px solid #cbd8d9;border-radius:8px;background:#f4f8f7;color:#34454b;font-weight:700;cursor:pointer}
</style>
<script>
(function(){
  function isE5Calender(){
    try{
      var mn=((machines[lang]||[])[currentMachineIndex]||'').toLowerCase();
      var sn=((extruderSections[lang]||[])[currentExtruderSection]||'').toLowerCase();
      return mn.indexOf('5')>=0 && (mn.indexOf('экструдер')>=0||mn.indexOf('אקסטרודר')>=0||mn.indexOf('extruder')>=0) && (sn.indexOf('кал')>=0||sn.indexOf('קלנ')>=0||sn.indexOf('cal')>=0);
    }catch(e){return false}
  }
  function addCalenderBack(){
    if(!isE5Calender())return;
    var catalog=document.getElementById('e5StationCatalog');
    if(!catalog)return;
    /* Category detail already has its own Back button. Add this only on the main Calender squares screen. */
    if(catalog.querySelector('#e5stBack'))return;
    var b=catalog.querySelector('#e5CalenderMainBack');
    if(!b){
      b=document.createElement('button');
      b.type='button';b.id='e5CalenderMainBack';
      catalog.insertBefore(b,catalog.firstChild);
    }
    b.textContent=lang==='he'?'← חזור לאקסטרודר 5':lang==='en'?'← Back to Extruder 5':'← Назад в Экструдер 5';
    b.onclick=function(e){
      e.preventDefault();e.stopPropagation();
      if(typeof openExtruder==='function')openExtruder(currentMachineIndex);
      return false;
    };
  }
  function syncIsolation(){
    var p=document.getElementById('extruderSectionPage');
    if(!p)return;
    if(isE5Calender()){
      p.classList.add('e5-calender-isolated');
      addCalenderBack();
    }else p.classList.remove('e5-calender-isolated');
  }
  var old=window.openExtruderSection;
  if(typeof old==='function'&&!old.__e5calIsolationA5){
    window.openExtruderSection=function(){
      var r=old.apply(this,arguments);
      setTimeout(syncIsolation,0);setTimeout(syncIsolation,100);setTimeout(syncIsolation,300);
      return r;
    };
    window.openExtruderSection.__e5calIsolationA5=true;
  }
  var page=document.getElementById('extruderSectionPage');
  if(page){new MutationObserver(function(){if(isE5Calender())setTimeout(addCalenderBack,0)}).observe(page,{childList:true,subtree:false});}
  document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){setTimeout(syncIsolation,50)})});
  setTimeout(syncIsolation,100);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
