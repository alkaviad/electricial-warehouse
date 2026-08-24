from flask import Flask, render_template_string
app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Elektrika</title>
<style>
*{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;background:#f3f4f6;color:#1f2937}
header{background:#1f2937;color:white;padding:18px}.top,main{max-width:1000px;margin:auto}.top{display:flex;justify-content:space-between;align-items:center}
h1{margin:0}.lang button{padding:8px 11px;margin:2px;border:0;border-radius:8px;cursor:pointer}
main{padding:28px 18px}.subtitle{color:#6b7280;margin-bottom:20px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px}
.card{background:white;border:1px solid #e5e7eb;border-radius:16px;min-height:145px;padding:22px;box-shadow:0 2px 8px #0001}
.icon{font-size:36px}.card h2{margin:12px 0 6px}.card p{margin:0;color:#6b7280;font-size:14px}
.notice{margin-top:24px;padding:14px;background:white;border:1px solid #e5e7eb;border-radius:12px}
</style></head><body>
<header><div class="top"><h1>⚡ <span id="title">Электрика</span></h1><div class="lang">
<button onclick="setLang('ru')">RU</button><button onclick="setLang('he')">עברית</button><button onclick="setLang('en')">EN</button>
</div></div></header>
<main><div class="subtitle" id="subtitle">Личная база главного электрика</div><div class="grid">
<div class="card"><div class="icon">📦</div><h2 id="stock">Общий склад</h2><p id="stockText">Детали, количество и место хранения</p></div>
<div class="card"><div class="icon">🏭</div><h2 id="machines">Машины</h2><p id="machinesText">Оборудование, детали и история каждой машины</p></div>
<div class="card"><div class="icon">🔧</div><h2 id="failures">Поломки</h2><p id="failuresText">История неисправностей и использованных деталей</p></div>
<div class="card"><div class="icon">🛠️</div><h2 id="maintenance">Обслуживание</h2><p id="maintenanceText">Плановые работы и история обслуживания</p></div>
<div class="card"><div class="icon">🔎</div><h2 id="search">Поиск</h2><p id="searchText">Поиск по машинам, складу и поломкам</p></div>
</div><div class="notice" id="notice">Версия 0.1 — первый экран. Следующим этапом подключим базу SQLite и кнопки.</div></main>
<script>
const texts={
ru:{title:"Электрика",subtitle:"Личная база главного электрика",stock:"Общий склад",stockText:"Детали, количество и место хранения",machines:"Машины",machinesText:"Оборудование, детали и история каждой машины",failures:"Поломки",failuresText:"История неисправностей и использованных деталей",maintenance:"Обслуживание",maintenanceText:"Плановые работы и история обслуживания",search:"Поиск",searchText:"Поиск по машинам, складу и поломкам",notice:"Версия 0.1 — первый экран. Следующим этапом подключим базу SQLite и кнопки."},
he:{title:"חשמל",subtitle:"מסד נתונים אישי לחשמלאי ראשי",stock:"מחסן כללי",stockText:"חלקים, כמות ומיקום אחסון",machines:"מכונות",machinesText:"ציוד, חלקים והיסטוריה של כל מכונה",failures:"תקלות",failuresText:"היסטוריית תקלות וחלקים שהוחלפו",maintenance:"תחזוקה",maintenanceText:"טיפולים מתוכננים והיסטוריית תחזוקה",search:"חיפוש",searchText:"חיפוש במכונות, במחסן ובתקלות",notice:"גרסה 0.1 — מסך ראשון. בשלב הבא נחבר מסד נתונים SQLite וכפתורים."},
en:{title:"Electrical",subtitle:"Chief electrician personal database",stock:"Main warehouse",stockText:"Parts, quantity and storage location",machines:"Machines",machinesText:"Equipment, parts and history for each machine",failures:"Failures",failuresText:"Fault history and parts used",maintenance:"Maintenance",maintenanceText:"Scheduled work and maintenance history",search:"Search",searchText:"Search machines, warehouse and failures",notice:"Version 0.1 — first screen. Next we will connect SQLite and functional buttons."}
};
function setLang(l){const t=texts[l];for(const k in t){const e=document.getElementById(k);if(e)e.textContent=t[k]}document.documentElement.lang=l;document.documentElement.dir=l==="he"?"rtl":"ltr";localStorage.setItem("elektrikaLang",l)}
setLang(localStorage.getItem("elektrikaLang")||"ru");
</script></body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
