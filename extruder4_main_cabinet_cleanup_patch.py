def apply(legacy):
    patch = r'''<style>
body.e4-main-cabinet-open #genericPartsInline{display:none!important}
</style>
<script>
(function(){
  function mark(){
    var full=document.getElementById('e4FullCabinet');
    var inv=document.getElementById('e4MainCabinetInventory');
    var open=!!((full&&full.offsetParent!==null)||(inv&&inv.offsetParent!==null));
    document.body.classList.toggle('e4-main-cabinet-open',open);
  }
  document.addEventListener('click',function(ev){
    if(ev.target.closest('#e4FullCabinet,#e4MainCabinetInventory')){
      ev.stopPropagation();
      setTimeout(mark,0);
    } else setTimeout(mark,0);
  },true);
  new MutationObserver(mark).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class','style']});
  setTimeout(mark,100);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
