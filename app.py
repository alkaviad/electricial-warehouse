from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r'''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Электрический склад</title>
  <style>
    *{box-sizing:border-box}
    :root{
      --bg:#eef2f7;
      --panel:#ffffff;
      --dark:#1f2937;
      --muted:#6b7280;
      --line:#d9e0e8;
      --accent:#2563eb;
      --accent-soft:#e8f0ff;
    }
    body{
      margin:0;
      font-family:Arial,Helvetica,sans-serif;
      background:var(--bg);
      color:var(--dark);
    }
    header{
      background:var(--dark);
      color:#fff;
      padding:15px 18px;
      box-shadow:0 2px 10px #0002;
    }
    .top{
      max-width:1200px;
      margin:auto;
      display:flex;
      align-items:center;
      justify-content:space-between;
      gap:14px;
    }
    h1{margin:0;font-size:26px;letter-spacing:.2px}
    .lang{display:flex;gap:6px}
    .lang button{
      border:0;
      border-radius:8px;
      padding:7px 10px;
      cursor:pointer;
      font-weight:700;
    }
    .workspace{
      max-width:1200px;
      margin:0 auto;
      padding:24px 18px;
      display:grid;
      grid-template-columns:190px 1fr;
      gap:28px;
      min-height:calc(100vh - 74px);
    }
    .side{
      display:flex;
      flex-direction:column;
      align-items:center;
      gap:18px;
      padding-top:10px;
    }
    .diamond-button{
      width:118px;
      height:118px;
      border:0;
      background:transparent;
      cursor:pointer;
      padding:0;
    }
    .diamond{
      width:84px;
      height:84px;
      margin:17px auto;
      background:var(--panel);
      border:2px solid var(--line);
      border-radius:15px;
      transform:rotate(45deg);
      box-shadow:0 4px 12px #0001;
      display:flex;
      align-items:center;
      justify-content:center;
      transition:.18s ease;
    }
    .diamond-inner{
      width:100px;
      transform:rotate(-45deg);
      text-align:center;
      font-weight:700;
      font-size:13px;
      line-height:1.15;
      color:var(--dark);
    }
    .diamond-inner .icon{
      display:block;
      font-size:25px;
      margin-bottom:5px;
    }
    .diamond-button:hover .diamond,
    .diamond-button.active .diamond{
      border-color:var(--accent);
      background:var(--accent-soft);
      box-shadow:0 6px 16px #2563eb22;
    }
    .content{
      background:var(--panel);
      border:1px solid var(--line);
      border-radius:18px;
      box-shadow:0 4px 18px #0001;
      padding:28px;
      min-width:0;
    }
    .content-head{
      border-bottom:1px solid var(--line);
      padding-bottom:16px;
      margin-bottom:22px;
    }
    .content-head h2{margin:0 0 7px;font-size:28px}
    .content-head p{margin:0;color:var(--muted)}
    .directory{
      border:1px dashed #bcc7d4;
      border-radius:14px;
      padding:24px;
      background:#fafbfd;
      min-height:360px;
    }
    .directory h3{margin-top:0;font-size:20px}
    .directory p{color:var(--muted);max-width:720px;line-height:1.55}
    .placeholder{
      margin-top:28px;
      padding:18px;
      border-radius:12px;
      background:#f2f5f9;
      color:#52606d;
    }
    @media(max-width:720px){
      h1{font-size:21px}
      .workspace{
        grid-template-columns:116px 1fr;
        gap:12px;
        padding:14px 10px;
      }
      .diamond-button{width:100px;height:100px}
      .diamond{width:70px;height:70px;margin:15px auto;border-radius:12px}
      .diamond-inner{width:90px;font-size:11px}
      .diamond-inner .icon{font-size:21px}
      .content{padding:18px 14px;border-radius:14px}
      .content-head h2{font-size:23px}
      .directory{padding:16px;min-height:330px}
      .lang button{padding:6px 8px;font-size:12px}
    }
  </style>
</head>
<body>
<header>
  <div class="top">
    <h1>⚡ <span id="appTitle">Электрический склад</span></h1>
    <div class="lang">
      <button onclick="setLang('ru')">RU</button>
      <button onclick="setLang('he')">עברית</button>
      <button onclick="setLang('en')">EN</button>
    </div>
  </div>
</header>

<main class="workspace">
  <nav class="side" id="sideNav">
    <button class="diamond-button active" data-section="stock" onclick="openSection('stock',this)">
      <div class="diamond"><div class="diamond-inner"><span class="icon">📦</span><span id="navStock">Склад</span></div></div>
    </button>
    <button class="diamond-button" data-section="machines" onclick="openSection('machines',this)">
      <div class="diamond"><div class="diamond-inner"><span class="icon">🏭</span><span id="navMachines">Машины</span></div></div>
    </button>
    <button class="diamond-button" data-section="failures" onclick="openSection('failures',this)">
      <div class="diamond"><div class="diamond-inner"><span class="icon">🔧</span><span id="navFailures">Поломки</span></div></div>
    </button>
    <button class="diamond-button" data-section="maintenance" onclick="openSection('maintenance',this)">
      <div class="diamond"><div class="diamond-inner"><span class="icon">🛠️</span><span id="navMaintenance">Обслуживание</span></div></div>
    </button>
    <button class="diamond-button" data-section="search" onclick="openSection('search',this)">
      <div class="diamond"><div class="diamond-inner"><span class="icon">🔎</span><span id="navSearch">Поиск</span></div></div>
    </button>
  </nav>

  <section class="content">
    <div class="content-head">
      <h2 id="sectionTitle">Склад</h2>
      <p id="sectionSubtitle">Детали, количество и место хранения</p>
    </div>
    <div class="directory">
      <h3 id="directoryTitle">Директория: Склад</h3>
      <p id="directoryText">Здесь будет содержимое выбранной директории. Следующим шагом мы отдельно построим структуру склада: категории деталей, количество, место хранения и другие нужные поля.</p>
      <div class="placeholder" id="placeholderText">Сейчас готова основа: слева ромбовидные кнопки, справа — отдельная рабочая область выбранного раздела.</div>
    </div>
  </section>
</main>

<script>
const texts={
  ru:{
    appTitle:'Электрический склад',
    navStock:'Склад',navMachines:'Машины',navFailures:'Поломки',navMaintenance:'Обслуживание',navSearch:'Поиск',
    sections:{
      stock:['Склад','Детали, количество и место хранения','Директория: Склад','Здесь будет содержимое выбранной директории. Следующим шагом мы отдельно построим структуру склада: категории деталей, количество, место хранения и другие нужные поля.'],
      machines:['Машины','Оборудование, детали и история каждой машины','Директория: Машины','Здесь будет список машин. Для каждой машины позже сделаем свою карточку, детали и историю.'],
      failures:['Поломки','История неисправностей и использованных деталей','Директория: Поломки','Здесь будет журнал поломок: машина, дата, неисправность, причина, ремонт и использованные детали.'],
      maintenance:['Обслуживание','Плановые работы и история обслуживания','Директория: Обслуживание','Здесь будет плановое обслуживание и история выполненных работ.'],
      search:['Поиск','Поиск по складу, машинам и поломкам','Директория: Поиск','Здесь будет общий поиск по всей базе.']
    },
    placeholder:'Сейчас готова основа: слева ромбовидные кнопки, справа — отдельная рабочая область выбранного раздела.'
  },
  he:{
    appTitle:'מחסן חשמל',
    navStock:'מחסן',navMachines:'מכונות',navFailures:'תקלות',navMaintenance:'תחזוקה',navSearch:'חיפוש',
    sections:{
      stock:['מחסן','חלקים, כמות ומיקום אחסון','תיקייה: מחסן','כאן יוצג תוכן תיקיית המחסן. בשלב הבא נבנה בנפרד קטגוריות, כמויות, מיקום אחסון ושדות נוספים.'],
      machines:['מכונות','ציוד, חלקים והיסטוריה של כל מכונה','תיקייה: מכונות','כאן תהיה רשימת המכונות. לכל מכונה נבנה בהמשך כרטיס, חלקים והיסטוריה.'],
      failures:['תקלות','היסטוריית תקלות וחלקים שהוחלפו','תיקייה: תקלות','כאן יהיה יומן תקלות: מכונה, תאריך, תקלה, סיבה, תיקון וחלקים.'],
      maintenance:['תחזוקה','עבודות מתוכננות והיסטוריית תחזוקה','תיקייה: תחזוקה','כאן יהיו טיפולים מתוכננים והיסטוריית עבודות.'],
      search:['חיפוש','חיפוש במחסן, במכונות ובתקלות','תיקייה: חיפוש','כאן יהיה חיפוש בכל בסיס הנתונים.']
    },
    placeholder:'הבסיס מוכן: כפתורי מעוין משמאל ואזור עבודה נפרד מימין.'
  },
  en:{
    appTitle:'Electrical Warehouse',
    navStock:'Warehouse',navMachines:'Machines',navFailures:'Failures',navMaintenance:'Maintenance',navSearch:'Search',
    sections:{
      stock:['Warehouse','Parts, quantity and storage location','Directory: Warehouse','This area will contain the warehouse directory. Next we will build categories, quantities, storage locations and the required fields.'],
      machines:['Machines','Equipment, parts and history for each machine','Directory: Machines','This area will contain the machine list. Each machine will later have its own card, parts and history.'],
      failures:['Failures','Fault history and parts used','Directory: Failures','This area will contain the fault log: machine, date, fault, cause, repair and parts used.'],
      maintenance:['Maintenance','Scheduled work and maintenance history','Directory: Maintenance','This area will contain planned maintenance and completed work history.'],
      search:['Search','Search warehouse, machines and failures','Directory: Search','This area will provide a global search across the database.']
    },
    placeholder:'The basic layout is ready: diamond navigation on the left and a dedicated working area on the right.'
  }
};

let currentLang=localStorage.getItem('elektrikaLang')||'ru';
let currentSection='stock';

function openSection(section,button){
  currentSection=section;
  document.querySelectorAll('.diamond-button').forEach(b=>b.classList.remove('active'));
  if(button)button.classList.add('active');
  renderSection();
}

function renderSection(){
  const t=texts[currentLang];
  const s=t.sections[currentSection];
  document.getElementById('sectionTitle').textContent=s[0];
  document.getElementById('sectionSubtitle').textContent=s[1];
  document.getElementById('directoryTitle').textContent=s[2];
  document.getElementById('directoryText').textContent=s[3];
  document.getElementById('placeholderText').textContent=t.placeholder;
}

function setLang(l){
  currentLang=l;
  const t=texts[l];
  document.documentElement.lang=l;
  document.documentElement.dir=l==='he'?'rtl':'ltr';
  document.getElementById('appTitle').textContent=t.appTitle;
  document.getElementById('navStock').textContent=t.navStock;
  document.getElementById('navMachines').textContent=t.navMachines;
  document.getElementById('navFailures').textContent=t.navFailures;
  document.getElementById('navMaintenance').textContent=t.navMaintenance;
  document.getElementById('navSearch').textContent=t.navSearch;
  localStorage.setItem('elektrikaLang',l);
  renderSection();
}

setLang(currentLang);
</script>
</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
