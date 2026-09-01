def apply(legacy):
    patch = r'''<style>
/* Extruder 5 / Calender only. This patch never changes global station layout. */
#extruderSectionPage.e5-calender-isolated > #e5StationCatalog{display:block!important}
#extruderSectionPage.e5-calender-isolated > #e4StationCatalog{display:none!important}
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
  function syncIsolation(){
    var p=document.getElementById('extruderSectionPage');
    if(!p)return;
    if(isE5Calender()) p.classList.add('e5-calender-isolated');
    else p.classList.remove('e5-calender-isolated');
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
  document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){setTimeout(syncIsolation,50)})});
  setTimeout(syncIsolation,100);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
