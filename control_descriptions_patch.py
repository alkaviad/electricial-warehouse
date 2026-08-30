def apply(legacy):
    patch = r'''<script>
(function(){
const D={
'6ES7131-6BF01-0BA0':'Цифровой вход ET200SP — DI 8×24 VDC, 8 входов',
'6ES7131-6BF00-0BA0':'Цифровой вход ET200SP — DI 8×24 VDC, 8 входов',
'6ES7131-6BH00-0BA0':'Цифровой вход ET200SP — DI 16×24 VDC, 16 входов',
'6ES7131-6BH01-0BA0':'Цифровой вход ET200SP — DI 16×24 VDC, 16 входов',
'6ES7132-6BF01-0BA0':'Цифровой выход ET200SP — DQ 8×24 VDC/0.5 A, 8 выходов',
'6ES7132-6BF00-0BA0':'Цифровой выход ET200SP — DQ 8×24 VDC/0.5 A, 8 выходов',
'6ES7132-6BH00-0BA0':'Цифровой выход ET200SP — DQ 16×24 VDC/0.5 A, 16 выходов',
'6ES7132-6BH01-0BA0':'Цифровой выход ET200SP — DQ 16×24 VDC/0.5 A, 16 выходов',
'6ES7132-6BD20-0BA0':'Цифровой выход ET200SP — DQ 4×24 VDC/2 A, 4 выхода',
'6ES7132-6BD21-0BA0':'Цифровой выход ET200SP — DQ 4×24 VDC/2 A, 4 выхода',
'6ES7132-6HD00-0BB1':'Релейный выход ET200SP — RQ 4×120 VDC…230 VAC/5 A, 4 НО выхода',
'6ES7134-6GD00-0BA1':'Аналоговый вход ET200SP — AI 4×I, 2-/4-проводный, 4 токовых входа, 16 bit',
'6ES7134-6GD01-0BA1':'Аналоговый вход ET200SP — AI 4×I, 2-/4-проводный, 4 токовых входа, 16 bit',
'6ES7134-6HD00-0BA1':'Аналоговый вход ET200SP — AI 4×U/I, 4 входа напряжение/ток, 16 bit',
'6ES7134-6HD01-0BA1':'Аналоговый вход ET200SP — AI 4×U/I, 4 входа напряжение/ток, 16 bit',
'6ES7134-6JD00-0CA1':'Аналоговый вход ET200SP — AI 4×RTD/TC, 4 входа температуры, 16 bit',
'6ES7134-6JF00-0CA1':'Аналоговый вход ET200SP — AI 8×RTD/TC, 8 входов температуры, 16 bit',
'6ES7135-6HD00-0BA1':'Аналоговый выход ET200SP — AQ 4×U/I, 4 аналоговых выхода, 16 bit',
'6ES7131-4BF00-0AA0':'Цифровой вход ET200S — DI 8×24 VDC, 8 входов',
'6ES7131-4BD01-0AA0':'Цифровой вход ET200S — DI 4×24 VDC, 4 входа',
'6ES7132-4BF00-0AA0':'Цифровой выход ET200S — DO 8×24 VDC/0.5 A, 8 выходов',
'6ES7132-4BF00-0AB0':'Цифровой выход ET200S — DO 8×24 VDC/0.5 A, 8 выходов',
'6ES7132-4BD02-0AA0':'Цифровой выход ET200S — DO 4×24 VDC/0.5 A, 4 выхода',
'6ES7134-4GB11-0AB0':'Аналоговый вход ET200S — 2 AI, 2 аналоговых входа',
'6ES7134-4NB01-0AB0':'Аналоговый вход ET200S — электронный модуль измерения температуры, 2 канала',
'6ES7135-4FB01-0AB0':'Аналоговый выход ET200S — 2 AO, 2 аналоговых выхода',
'321-1BL00-0AA0':'SIMATIC S7-300 SM321 — цифровой вход, 32×24 VDC, 32 входа',
'321-1BH02-0AA0':'SIMATIC S7-300 SM321 — цифровой вход, 16×24 VDC, 16 входов',
'322-1BH01-0AA0':'SIMATIC S7-300 SM322 — цифровой выход, 16×24 VDC/0.5 A, 16 выходов',
'331-1KF02-0AB0':'SIMATIC S7-300 SM331 — аналоговый вход, 8 каналов',
'332-5HD01-0AB0':'SIMATIC S7-300 SM332 — аналоговый выход, 4 канала',
'343-1CX10-0XE0':'SIMATIC NET CP343-1 — коммуникационный процессор Industrial Ethernet/PROFINET',
'6ES7155-6AU00-0BN0':'ET200SP IM155-6 PN — интерфейсный модуль PROFINET, головной модуль станции',
'6ES7151-1AA05-0AB0':'ET200S IM151-1 — интерфейсный/головной модуль PROFIBUS DP',
'6ES7151-1AA06-0AB0':'ET200S IM151-1 — интерфейсный/головной модуль PROFIBUS DP',
'6ES7151-7FA20-0AB0':'ET200S IM151-7 F-CPU — головной модуль с fail-safe CPU',
'6ES7193-6BP20-0DA0':'ET200SP BaseUnit — базовый/клеммный модуль для установки I/O',
'6ES7193-6BP40-0DA0':'ET200SP BaseUnit — базовый/клеммный модуль для установки I/O',
'6ES7972-0BA42-0XA0':'PROFIBUS DP — шинный разъём/коннектор',
'X20DI9371':'B&R X20 — цифровой вход, 12 входов 24 VDC',
'X20DO9322':'B&R X20 — цифровой выход, 12 выходов 24 VDC',
'X20AI1744':'B&R X20 — аналоговый вход, 4 канала',
'X20AI4622':'B&R X20 — аналоговый вход, 4 канала',
'X20AO4622':'B&R X20 — аналоговый выход, 4 канала',
'ID211':'OMRON CJ1W-ID211 — цифровой вход, 16×24 VDC, 16 входов',
'OD211':'OMRON CJ1W-OD211 — транзисторный цифровой выход, 16 выходов',
'MAD42':'OMRON CJ1W-MAD42 — комбинированный аналоговый I/O: 4 входа + 2 выхода'
};
function n(s){return String(s||'').toUpperCase().replace(/[\s._\-/]+/g,'').replace(/O/g,'0')}
const N={};Object.keys(D).forEach(k=>N[n(k)]=D[k]);
function enrich(){let changed=false;inventory.forEach(x=>{if(x.cat!=='plc_modules')return;let d=N[n(x.name)]||N[n(x.internalCode)];if(!d)return;let old=String(x.specs||'').trim();if(!old||old.length<12||/Line [45]/i.test(old)||/כרטיס|בקר|הרחבה|analog|digital/i.test(old)){x.specs=d+(old&&!d.includes(old)?' · '+old:'');changed=true}});if(changed){try{localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory))}catch(e){}}}
enrich();
})();
</script>'''
    legacy.HTML=legacy.HTML.replace('</body>',patch+'</body>')
