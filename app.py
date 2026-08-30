import legacy

LANG_FIX = r'''<script>
(function(){
  const CACHE_KEY='warehouse_translation_cache_v1';
  let trCache={};
  try{trCache=JSON.parse(localStorage.getItem(CACHE_KEY)||'{}')}catch(e){trCache={}}

  function saveCache(){
    try{localStorage.setItem(CACHE_KEY,JSON.stringify(trCache))}catch(e){}
  }

  function looksLikePartNumber(s){
    if(!s)return true;
    const letters=(s.match(/[A-Za-zА-Яа-яא-ת]/g)||[]).length;
    const digits=(s.match(/[0-9]/g)||[]).length;
    const spaces=(s.match(/\s/g)||[]).length;
    return digits>0 && letters>0 && spaces===0;
  }

  async function tr(text,target){
    text=(text||'').trim();
    if(!text || looksLikePartNumber(text))return text;
    const key=target+'|'+text;
    if(trCache[key])return trCache[key];
    try{
      const u='https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl='+target+'&dt=t&q='+encodeURIComponent(text);
      const r=await fetch(u);
      if(!r.ok)return text;
      const j=await r.json();
      const out=(j[0]||[]).map(x=>x[0]).join('').trim()||text;
      trCache[key]=out; saveCache(); return out;
    }catch(e){return text}
  }

  function staticWarehouseTerm(text,target){
    const d={
      'בסיס לממסרים':{ru:'Колодка реле',he:'בסיס לממסרים',en:'Relay socket'},
      'בסיס ממסר':{ru:'Колодка реле',he:'בסיס ממסר',en:'Relay socket'},
      'ממסר צעד':{ru:'Импульсное реле',he:'ממסר צעד',en:'Impulse relay'},
      'פחת':{ru:'УЗО',he:'פחת',en:'RCD'},
      'מאמ׳׳ת':{ru:'Автоматический выключатель',he:'מאמ״ת',en:'Circuit breaker'},
      'מאמ״ת':{ru:'Автоматический выключатель',he:'מאמ״ת',en:'Circuit breaker'},
      'למנוע':{ru:'для двигателя',he:'למנוע',en:'for motor'},
      'כוכב +משולש':{ru:'звезда-треугольник',he:'כוכב-משולש',en:'star-delta'}
    };
    let out=text||'';
    Object.keys(d).forEach(k=>{out=out.split(k).join(d[k][target]||k)});
    return out;
  }

  async function displayText(text,target,kind){
    let s=staticWarehouseTerm(text,target);
    if(!s || looksLikePartNumber(s))return s;
    if(kind==='name'){
      // Keep catalogue/part numbers intact; translate only human-readable wording around them.
      const chunks=s.split(/(\b[A-Z0-9][A-Z0-9._+\/-]*\d[A-Z0-9._+\/-]*\b)/gi);
      const out=[];
      for(const c of chunks){
        if(!c){out.push(c);continue}
        if(/\d/.test(c)&&!/\s/.test(c)){out.push(c);continue}
        out.push(await tr(c,target));
      }
      return out.join('');
    }
    return await tr(s,target);
  }

  const oldRender=window.renderWarehouseItems;
  window.renderWarehouseItems=function(){
    if(!window.currentWarehouseCat && typeof currentWarehouseCat==='undefined')return;
    const cat=(typeof currentWarehouseCat!=='undefined'?currentWarehouseCat:window.currentWarehouseCat);
    if(!cat)return;
    const q=(warehouseSearch.value||'').toLowerCase(),mf=manufacturerFilter.value||'';
    const rows=inventory.map((x,i)=>({x,i})).filter(o=>o.x.cat===cat).filter(o=>!mf||o.x.manufacturer===mf).filter(o=>!q||[o.x.name,o.x.manufacturer,o.x.specs,o.x.machine,o.x.notes].join(' ').toLowerCase().includes(q));
    warehouseItemsBody.innerHTML=rows.map(o=>`<tr data-widx="${o.i}"><td><b class="tr-name">${esc(o.x.name)}</b></td><td>${esc(o.x.manufacturer)}</td><td class="tr-specs">${esc(o.x.specs)}</td><td class="qty">${esc(String(o.x.qty??''))}</td><td class="tr-machine">${esc(o.x.machine||'')}</td><td>${o.x.price?esc(String(o.x.price)):''}</td><td class="item-actions owner-only"><button onclick="openWarehouseEdit(${o.i})">✎</button><button onclick="deleteWarehouseItem(${o.i})">×</button></td></tr>`).join('');
    const target=(typeof lang!=='undefined'?lang:'ru');
    rows.forEach(async o=>{
      const row=warehouseItemsBody.querySelector(`tr[data-widx="${o.i}"]`); if(!row)return;
      const [n,s,m]=await Promise.all([
        displayText(o.x.name,target,'name'),
        displayText(o.x.specs,target,'specs'),
        displayText(o.x.machine||'',target,'machine')
      ]);
      if(!row.isConnected)return;
      const ne=row.querySelector('.tr-name'),se=row.querySelector('.tr-specs'),me=row.querySelector('.tr-machine');
      if(ne)ne.textContent=n;if(se)se.textContent=s;if(me)me.textContent=m;
    });
  };

  // Re-render the open warehouse section immediately, if one is already visible.
  try{if(document.getElementById('warehouseCategory').classList.contains('active'))window.renderWarehouseItems()}catch(e){}
})();
</script>'''

legacy.HTML = legacy.HTML.replace('</body>', LANG_FIX + '</body>')
app = legacy.app

if __name__ == '__main__':
    app.run(debug=True)
