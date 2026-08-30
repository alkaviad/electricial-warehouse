def apply(legacy):
    patch=r'''<script>(function(){
const D={
'6ES7134-4NB01-0AB0':'Аналоговый вход ET200S — 2 AI Thermocouple HF, 2 входа термопар, 15 bit + sign',
'6ES7138-4CA01-0AB0':'ET200S PM-E — силовой/питающий модуль 24 VDC для группы I/O',
'6ES7138-4CA01-0AA0':'ET200S PM-E — силовой/питающий модуль 24 VDC для группы I/O',
'7MH4920-0AA01':'SIWAREX CF — измерительный модуль для 1 тензодатчика силы, для ET200S',
'6ES7138-4DB03-0AA0':'ET200S 1SSI — 1-канальный SSI-интерфейс для абсолютного энкодера',
'6ES7132-4HB01-0AB0':'Релейный выход ET200S — 2 релейных выхода 24 VDC…230 VAC/5 A',
'6ES7134-4FB01-0AB0':'Аналоговый вход ET200S — 2 AI напряжение, ±10/±5/1…5 V, 2 канала',
'6ES7135-4FB01-0AB0':'Аналоговый выход ET200S — 2 AO напряжение, ±10 V / 1…5 V, 2 канала',
'322-1BH01-0AA0':'SIMATIC S7-300 SM322 — цифровой выход, 16×24 VDC/0.5 A, 16 выходов',
'343-1CX10-0XE0':'SIMATIC NET CP343-1 — коммуникационный процессор Industrial Ethernet/PROFINET',
'332-5HB01-0AA0':'SIMATIC S7-300 SM332 — аналоговый выход, 2 канала',
'321-1BL00-0AA0':'SIMATIC S7-300 SM321 — цифровой вход, 32×24 VDC, 32 входа',
'321-1BH02-0AA0':'SIMATIC S7-300 SM321 — цифровой вход, 16×24 VDC, 16 входов',
'331-1KF02-0AB0':'SIMATIC S7-300 SM331 — аналоговый вход, 8 каналов',
'332-5HD01-0AB0':'SIMATIC S7-300 SM332 — аналоговый выход, 4 канала',
'6ES7131-4BF00-0AA0':'Цифровой вход ET200S — DI 8×24 VDC, 8 входов',
'6ES7131-4BD01-0AA0':'Цифровой вход ET200S — DI 4×24 VDC, 4 входа',
'6ES7132-4BF00-0AA0':'Цифровой выход ET200S — DO 8×24 VDC/0.5 A, 8 выходов',
'6ES7132-4BF00-0AB0':'Цифровой выход ET200S — DO 8×24 VDC/0.5 A, 8 выходов, High Feature',
'6ES7132-4BD02-0AA0':'Цифровой выход ET200S — DO 4×24 VDC/0.5 A, 4 выхода',
'6ES7132-4BD32-0AA0':'Цифровой выход ET200S — DO 4×24 VDC/2 A, 4 выхода',
'6ES7134-4GB11-0AB0':'Аналоговый вход ET200S — 2 AI ток, 2 канала',
'6ES7151-1AA05-0AB0':'ET200S IM151-1 — головной/интерфейсный модуль PROFIBUS DP',
'6ES7151-1AA06-0AB0':'ET200S IM151-1 — головной/интерфейсный модуль PROFIBUS DP',
'6ES7151-7FA20-0AB0':'ET200S IM151-7 F-CPU — головной модуль со встроенным fail-safe CPU',
'6ES7972-0AA02-0XA0':'PROFIBUS DP — шинный разъём/коннектор',
'6ES7972-0AA01-0XA0':'PROFIBUS DP — шинный разъём/коннектор',
'PA202':'OMRON CJ1W-PA202 — блок питания PLC CJ-series, 100–240 VAC',
'CJ2MCPU32':'OMRON CJ2M-CPU32 — центральный процессор PLC CJ2M, Ethernet',
'MAD42':'OMRON CJ1W-MAD42 — аналоговый I/O: 4 входа + 2 выхода',
'ID211':'OMRON CJ1W-ID211 — цифровой вход, 16×24 VDC, 16 входов',
'OD211':'OMRON CJ1W-OD211 — цифровой транзисторный выход, 16 выходов',
'X20CP1483':'B&R X20 — CPU/PLC контроллер',
'X20IF10E3-1':'B&R X20 — коммуникационный модуль Ethernet POWERLINK',
'X20DI9371':'B&R X20 — цифровой вход, 12 входов 24 VDC',
'X20DO9322':'B&R X20 — цифровой выход, 12 выходов 24 VDC',
'X20AI1744':'B&R X20 — аналоговый вход, 4 канала',
'X20AI4622':'B&R X20 — аналоговый вход, 4 канала',
'X20AO4622':'B&R X20 — аналоговый выход, 4 канала',
'X20CS1070':'B&R X20 — коммуникационный модуль последовательной связи'
};
function n(s){return String(s||'').toUpperCase().replace(/[\s._\-/]+/g,'').replace(/O/g,'0')}
const N={};Object.keys(D).forEach(k=>N[n(k)]=D[k]);
let changed=false;inventory.forEach(x=>{if(x.cat!=='plc_modules')return;let m=String(x.machine||'').trim();if(/^(Line|Row|שורה)\s*4$/i.test(m)){x.machine='Экструдер 4';changed=true}else if(/^(Line|Row|שורה)\s*5$/i.test(m)){x.machine='Экструдер 5';changed=true}else if(/^(Line|Row|שורה)\s*6$/i.test(m)){x.machine='Экструдер 6';changed=true}let d=N[n(x.name)]||N[n(x.internalCode)];if(d&&String(x.specs||'').trim()!==d){x.specs=d;changed=true}});if(changed)localStorage.setItem('warehouse_inventory_v2',JSON.stringify(inventory));
})();</script>''';legacy.HTML=legacy.HTML.replace('</body>',patch+'</body>')
