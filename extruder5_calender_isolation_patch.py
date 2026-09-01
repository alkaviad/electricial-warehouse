def apply(legacy):
    patch = r'''<style>
/* A7 — isolated Extruder 5 / Calender patch only. */
#e5StationCatalog #e5CalenderMainBack{display:inline-block;margin:0 0 12px;padding:8px 12px;border:1px solid #cbd8d9;border-radius:8px;background:#f4f8f7;color:#34454b;font-weight:700;cursor:pointer}
</style>
<script>
(function(){
  function isE5Calender(sectionIndex){
    try{
      var mi=Number(currentMachineIndex),si=sectionIndex==null?Number(currentExtruderSection):Number(sectionIndex);
      if(mi===16&&si===3)return true;
      var mn=((machines[lang]||[])[mi]||'').toLowerCase();
      var sn=((extruderSections[lang]||[])[si]||'').toLowerCase();
      return mn.indexOf('5')>=0&&(mn.indexOf('экструдер')>=0||mn.indexOf('אקסטרודר')>=0||mn.indexOf('extruder')>=0)&&(sn.indexOf('кал')>=0||sn.indexOf('קלנ')>=0||sn.indexOf('cal')>=0);
    }catch(e){return false}
  }
  function applyLocalState(){
    if(!isE5Calender())return;
    var e5=document.getElementById('e5StationCatalog');
    if(!e5)return;
    e5.style.setProperty('display','block','important');
    var e4=document.getElementById('e4StationCatalog');
    if(e4)e4.style.setProperty('display','none','important');
    if(e5.querySelector('#e5stBack'))return;
    var b=e5.querySelector('#e5CalenderMainBack');
    if(!b){b=document.createElement('button');b.type='button';b.id='e5CalenderMainBack';e5.insertBefore(b,e5.firstChild)}
    b.textContent=lang==='he'?'← חזרה':lang==='en'?'← Back':'← Назад';
    b.onclick=function(ev){if(ev){ev.preventDefault();ev.stopPropagation()}if(typeof openExtruder==='function')openExtruder(currentMachineIndex);return false};
  }
  var old=window.openExtruderSection;
  if(typeof old==='function'&&!old.__e5calIsolationA7){
    window.openExtruderSection=function(sectionIndex){
      var target=isE5Calender(sectionIndex);
      var realTimeout=window.setTimeout;
      if(target){
        /* The older Calender renderer schedules the same screen several times. Suppress only those duplicate local redraw timers during this one Calender opening. */
        window.setTimeout=function(fn,delay){if(delay===0||delay===80||delay===250)return 0;return realTimeout.apply(window,arguments)};
      }
      var r;
      try{r=old.apply(this,arguments)}finally{if(target)window.setTimeout=realTimeout}
      if(target){realTimeout(applyLocalState,20);realTimeout(applyLocalState,120)}
      return r;
    };
    window.openExtruderSection.__e5calIsolationA7=true;
  }
  var page=document.getElementById('extruderSectionPage');
  if(page)new MutationObserver(function(muts){
    if(!isE5Calender())return;
    for(var i=0;i<muts.length;i++){
      if(muts[i].type==='childList'){setTimeout(applyLocalState,0);break}
    }
  }).observe(page,{childList:true,subtree:false});
  document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){setTimeout(applyLocalState,50)})});
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
