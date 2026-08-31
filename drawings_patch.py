def apply(legacy):
    patch = r'''<style>
#drawingsPage .drawings-wrap{overflow:auto;border:1px solid var(--line);border-radius:10px;background:#fff}
#drawingsPage table{min-width:620px}
#drawingsPage td,#drawingsPage th{font-size:14px;padding:12px}
#drawingsPage .drawing-open{border:1px solid var(--line);border-radius:8px;padding:8px 13px;background:#eef5f3;color:var(--ink);font-weight:700;cursor:pointer}
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
   p.innerHTML='<h2 id="drawingsTitle"></h2><p class="subtitle" id="drawingsSub"></p><div class="drawings-wrap"><table><thead><tr><th id="drawingMachineHead"></th><th id="drawingPlaceHead"></th><th id="drawingOpenHead"></th></tr></thead><tbody id="drawingsBody"></tbody></table></div>';
   content.appendChild(p);
 }
 function machineNames(){try{if(typeof getNames==='function')return getNames('machines')}catch(e){};return (defaults&&defaults.machines&&defaults.machines[lang])||[]}
 window.renderDrawingsPage=function(){
   const nav=document.getElementById('drawingsNav'),title=document.getElementById('drawingsTitle'),sub=document.getElementById('drawingsSub'),mh=document.getElementById('drawingMachineHead'),ph=document.getElementById('drawingPlaceHead'),oh=document.getElementById('drawingOpenHead'),body=document.getElementById('drawingsBody');if(!body)return;
   const tx=lang==='he'?{nav:'שרטוטי חשמל',title:'שרטוטי חשמל',sub:'טבלת מכונות וגישה לשרטוטים',machine:'מכונה',place:'מיקום השרטוטים',open:'פתיחה',empty:'עדיין לא הוגדר',button:'פתח שרטוטים'}:lang==='en'?{nav:'Electrical drawings',title:'Electrical drawings',sub:'Machine table and access to drawings',machine:'Machine',place:'Drawing storage',open:'Open',empty:'Not configured yet',button:'Open drawings'}:{nav:'Электрические чертежи',title:'Электрические чертежи',sub:'Таблица машин и доступ к чертежам',machine:'Машина',place:'Где хранятся чертежи',open:'Открыть',empty:'Пока не настроено',button:'Открыть чертежи'};
   nav.textContent=tx.nav;title.textContent=tx.title;sub.textContent=tx.sub;mh.textContent=tx.machine;ph.textContent=tx.place;oh.textContent=tx.open;
   body.innerHTML=machineNames().map(n=>'<tr><td><b>'+esc(n)+'</b></td><td class="subtitle">'+tx.empty+'</td><td><button class="drawing-open" disabled>'+tx.button+'</button></td></tr>').join('');
 };
 window.openDrawingsPage=function(){document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));document.getElementById('drawingsPage').classList.add('active');renderDrawingsPage();window.scrollTo({top:0,left:0,behavior:'auto'})};
 document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(renderDrawingsPage,0)));
 renderDrawingsPage();
})();
</script>'''
    legacy.HTML = legacy.HTML.replace('</body>', patch + '</body>')
