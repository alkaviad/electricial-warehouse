def apply(legacy):
    patch = r'''<style>
body.e4-main-cabinet-open #genericPartsInline{display:none!important}
body.e4-main-cabinet-open #extruderMainPanelBlock{display:none!important}
</style>
<script>
(function(){
  function mark(){
    var full=document.getElementById('e4FullCabinet');
    var inv=document.getElementById('e4MainCabinetInventory');
    var open=!!((full&&full.offsetParent!==null)||(inv&&inv.offsetParent!==null));
    document.body.classList.toggle('e4-main-cabinet-open',open);
  }
  /* Do not intercept clicks here. This patch only controls visibility. */
  document.addEventListener('click',function(){setTimeout(mark,0)},false);
  new MutationObserver(mark).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class','style']});
  setTimeout(mark,100);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
