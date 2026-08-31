def apply(legacy):
    patch = r'''<script>
(function(){
  const keys=['plc','io','safety','power','ethernet','starters','contactors','relays','breakers','fuses','encoders','drives'];
  document.addEventListener('click',function(ev){
    const tile=ev.target.closest&&ev.target.closest('#e4FullCabinet .e4full-tile');
    if(!tile)return;
    ev.preventDefault();
    ev.stopPropagation();
    if(ev.stopImmediatePropagation)ev.stopImmediatePropagation();
    const tiles=Array.from(document.querySelectorAll('#e4FullCabinet .e4full-tile'));
    const i=tiles.indexOf(tile);
    if(i>=0&&keys[i]&&typeof window.e4FullOpen==='function')window.e4FullOpen(keys[i]);
  },true);
  document.addEventListener('click',function(ev){
    const back=ev.target.closest&&ev.target.closest('#e4FullCabinet .e4full-close');
    if(!back)return;
    ev.preventDefault();
    ev.stopPropagation();
    if(typeof window.e4FullClose==='function')window.e4FullClose();
  },true);
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
