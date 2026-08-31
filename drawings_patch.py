def apply(legacy):
    patch = r'''<style>
#drawingsPage .drawings-wrap{overflow:auto;border:1px solid var(--line);border-radius:10px;background:#fff}
#drawingsPage table{min-width:520px}
#drawingsPage td,#drawingsPage th{font-size:14px}
</style>
<script>
(function(){
 const side=document.querySelector('.side');
 if(side&&!document.getElementById('drawingsBtn')){
   const b=document.createElement('button');b.className='diamond-button';b.id='drawingsBtn';b.onclick=()=>openDrawingsPage();
   b.innerHTML='<div class="diamond"><div class="diamond-inner"><span class="icon">📐</span><span id="drawingsNav"></span></div></div>';
   side.appendChild(b);
 }
 const content=document.querySelector('.content');
 if(content&&!document.getElementById('drawingsPage')){
   const p=document.createElement('div');p.id='drawingsPage';p.className='page';
   p.innerHTML='<h2 id="drawingsTitle"></h2><p class="subtitle" id="drawingsSub"></p><div class="drawings-wrap"><table><thead><tr><th id="drawingMachineHead"></th><th id="drawingFilesHead"></th></tr></thead><tbody id="drawingsBody"></tbody></table></div>';
   content.appendChild(p);
 }
 function machineNames(){try{if(typeof getNames==='function')return getNames('machines')}catch(e){};return (defaults&&defaults.machines&&defaults.machines[lang])||[]}
 window.renderDrawingsPage=function(){
   const nav=document.getElementById('drawingsNav'),title=document.getElementById('drawingsTitle'),sub=document.getElementById('drawingsSub'),mh=document.getElementById('drawingMachineHead'),fh=document.getElementById('drawingFilesHead'),body=document.getElementById('drawingsBody');if(!body)return;
   const tx=lang==='he'?{nav:'שרטוטי חשמל',title:'שרטוטי חשמל',sub:'כל המכונות והשרטוטים החשמליים שלהן',machine:'מכונה',files:'קבצים / שרטוטים',empty:'טרם נוספו'}:lang==='en'?{nav:'Electrical drawings',title:'Electrical drawings',sub:'All machines and their electrical drawings',machine:'Machine',files:'Files / drawings',empty:'Not added yet'}:{nav:'Электрические чертежи',title:'Электрические чертежи',sub:'Все машины и их электрические чертежи',machine:'Машина',files:'Файлы / чертежи',empty:'Пока не добавлены'};
   nav.textContent=tx.nav;title.textContent=tx.title;sub.textContent=tx.sub;mh.textContent=tx.machine;fh.textContent=tx.files;
   body.innerHTML=machineNames().map(n=>'<tr><td><b>'+esc(n)+'</b></td><td class="subtitle">'+tx.empty+'</td></tr>').join('');
 };
 window.openDrawingsPage=function(){document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));document.getElementById('drawingsPage').classList.add('active');renderDrawingsPage();window.scrollTo({top:0,left:0,behavior:'auto'})};
 document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(renderDrawingsPage,0)));
 renderDrawingsPage();
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
