STYLE = r'''<style id="clean-table-style">
/* Unified clean industrial tables */
:root{--tbl-border:#d7e0e2;--tbl-head:#e9f0f1;--tbl-head2:#f5f8f8;--tbl-hover:#eef6f7;--tbl-text:#26383d}
.table-wrap,.warehouse-table-wrap,.parts-table-wrap{width:100%;overflow:auto;border:1px solid var(--tbl-border);border-radius:12px;background:#fff;box-shadow:0 2px 8px rgba(38,56,61,.06)}
table{border-collapse:separate!important;border-spacing:0!important;width:100%;background:#fff;color:var(--tbl-text)}
thead th{position:sticky;top:0;z-index:2;background:var(--tbl-head)!important;color:#26383d!important;font-weight:800!important;white-space:nowrap;border-bottom:2px solid #bdcccf!important;padding:11px 12px!important;text-align:center!important}
tbody td{padding:10px 12px!important;border-bottom:1px solid var(--tbl-border)!important;vertical-align:middle!important;background:#fff}
tbody tr:nth-child(even) td{background:var(--tbl-head2)}
tbody tr:hover td{background:var(--tbl-hover)!important}
tbody tr:last-child td{border-bottom:0!important}
th+th,td+td{border-inline-start:1px solid #e5ebec!important}
td b,.internal-code{font-weight:750;color:#20363b}
.qty-control{min-width:132px}
.qty-control button{width:40px!important;height:40px!important;border-radius:9px!important;background:#f3f7f7!important}
.qty-control .qnum{font-size:18px!important;min-width:38px!important}
.item-actions{white-space:nowrap;text-align:center}
.item-actions button,td button[onclick*="openMachinePartEdit"],td button[onclick*="openWarehouseEdit"]{min-width:38px;min-height:38px;border:1px solid #c8d4d6;border-radius:8px;background:#fff;cursor:pointer}
/* Keep model / part number and manufacturer readable */
td.internal-code,td:nth-child(1),td:nth-child(2),td:nth-child(3){white-space:nowrap}
/* RTL/Hebrew tables keep the same visual grid, but text follows page direction */
html[dir="rtl"] tbody td{text-align:right}
html[dir="ltr"] tbody td{text-align:left}
html[dir="rtl"] thead th,html[dir="ltr"] thead th{text-align:center!important}
@media(max-width:800px){thead th,tbody td{padding:8px 9px!important;font-size:13px}.qty-control{min-width:116px}.qty-control button{width:36px!important;height:36px!important}}
</style>'''

def apply(legacy):
    if 'id="clean-table-style"' in legacy.HTML:
        return
    legacy.HTML = legacy.HTML.replace('</head>', STYLE + '</head>')
