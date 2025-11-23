<div align="center" style="background:linear-gradient(120deg,#0ea5e9 0%,#6366f1 100%);padding:40px;border-radius:12px">

<h1 style="color:white;">
<i class="fa-solid fa-database"></i>
SQLAlchemy ORM — Interactive README
</h1>

<p style="color:#d0e7ff;font-size:18px;">
An interactive README with images, video, icons, resource buttons and a downloadable markdown file.
</p>

<a href="#downloads" style="
background:#06b6d4;padding:12px 18px;border-radius:10px;color:#051025;
text-decoration:none;font-weight:bold;margin-right:8px;">
<i class="fa-solid fa-download"></i> Download README.md
</a>

<a href="#video" style="
border:1px solid rgba(255,255,255,0.3);
padding:12px 18px;border-radius:10px;color:white;
text-decoration:none;font-weight:bold;">
<i class="fa-solid fa-play"></i> Watch tutorial
</a>

</div>

---

# 🔍 Quick Overview

This page shows how an ORM (SQLAlchemy) maps Python classes to database tables and provides ready examples of creating, reading, updating and deleting data.

## ⚙️ How it works
1. Define a Python class that represents a table (model).  
2. Use a session to add, query and commit objects.  
3. SQLAlchemy generates SQL automatically and stores data in **mydb.db**.

## 📦 Included
- HTML-style README (works in GitHub)
- Images + icons
- YouTube tutorial embed
- Download button for README.md
- Resource buttons

---

# 📚 Resources

<a href="https://docs.sqlalchemy.org" target="_blank" style="display:block;padding:10px;background:#0f172a;border-radius:8px;margin:6px 0;color:#d9f1ff;text-decoration:none;">
<i class="fa-brands fa-python"></i> SQLAlchemy Docs
</a>

<a href="https://sqlitebrowser.org" target="_blank" style="display:block;padding:10px;background:#0f172a;border-radius:8px;margin:6px 0;color:#d9f1ff;text-decoration:none;">
<i class="fa-solid fa-database"></i> DB Browser for SQLite
</a>
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SQLAlchemy ORM — Interactive README</title>
  <!-- Font Awesome for icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    body{font-family:Inter, Arial, sans-serif;line-height:1.5;margin:0;background:#0f172a;color:#e6eef8}
    .hero{background:linear-gradient(120deg,#0ea5e9 0%,#6366f1 100%);padding:48px 16px;text-align:center}
    .card{background:#0b1220;border-radius:12px;padding:20px;margin:16px;box-shadow:0 6px 20px rgba(2,6,23,0.6)}
    .container{max-width:980px;margin: -40px auto 40px;}
    h1{font-size:30px;margin:8px 0;color:#fff}
    p.lead{color:#d0e7ff;opacity:0.95}
    .grid{display:grid;grid-template-columns:1fr 320px;gap:16px}
    .btn{display:inline-block;padding:10px 14px;border-radius:10px;text-decoration:none;font-weight:700}
    .btn-primary{background:#06b6d4;color:#051025}
    .btn-ghost{background:transparent;border:1px solid rgba(255,255,255,0.08);color:#d6e9ff}
    .resources a{display:block;margin:8px 0;padding:10px;border-radius:8px;background:rgba(255,255,255,0.03);color:#d9f1ff;text-decoration:none}
    .preview img{max-width:100%;border-radius:8px}
    pre{background:#001219;padding:12px;border-radius:8px;overflow:auto}
    .icon{font-size:18px;margin-right:8px}
    footer{padding:20px;text-align:center;color:#9fb7d3}
    /* small screens */
    @media(max-width:880px){.grid{grid-template-columns:1fr}}
  </style>
</head>
<body>
  <section class="hero">
    <div style="max-width:980px;margin:0 auto">
      <h1><i class="fa-solid fa-database" style="color:#fff;margin-right:10px"></i> SQLAlchemy ORM — Interactive README</h1>
      <p class="lead">An interactive HTML README with images, video, icons, resource buttons and a built-in download button for a ready-to-use README.md file.</p>
      <div style="margin-top:14px">
        <a class="btn btn-primary" href="#download" onclick="downloadMarkdown()" title="Download README.md"><i class="fa-solid fa-download"></i> Download README.md</a>
        <a class="btn btn-ghost" href="#video" style="margin-left:8px" onclick="document.getElementById('video').scrollIntoView({behavior:'smooth'})"><i class="fa-solid fa-play"></i> Watch tutorial</a>
      </div>
    </div>
  </section>

  <div class="container">
    <div class="card grid">
      <div>
        <h2 style="color:#bfe6ff"><i class="fa-solid fa-circle-info" style="color:#9be7ff;margin-right:8px"></i> Quick Overview</h2>
        <p>This page shows how an ORM (SQLAlchemy) maps Python classes to database tables and provides ready examples of creating, reading, updating and deleting data.</p>

```
    <h3 style="margin-top:12px;color:#dff7ff">How it works</h3>
    <ol>
      <li>Define a Python class that represents a table (a model).</li>
      <li>Use a session to add, query and commit objects.</li>
      <li>SQLAlchemy generates SQL under the hood and persists changes to the SQLite file <code>mydb.db</code>.</li>
    </ol>

    <h3 style="margin-top:12px;color:#dff7ff">Included</h3>
    <ul>
      <li>HTML README with images and icons</li>
      <li>Embedded YouTube tutorial</li>
      <li>Download button which writes a README.md file to your machine</li>
      <li>Buttons linking to official resources</li>
    </ul>

    <h3 style="margin-top:12px;color:#dff7ff">Resources</h3>
    <div class="resources">
      <a href="https://docs.sqlalchemy.org" target="_blank"><i class="fa-brands fa-python icon"></i> SQLAlchemy Docs</a>
      <a href="https://sqlitebrowser.org" target="_blank"><i class="fa-solid fa-database icon"></i> DB Browser for SQLite</a>
      <a href="https://www.youtube.com/watch?v=woKYyhLCcnU" target="_blank"><i class="fa-brands fa-youtube icon"></i> SQLAlchemy Tutorial (YouTube)</a>
      <a href="https://github.com/sqlalchemy/sqlalchemy" target="_blank"><i class="fa-brands fa-github icon"></i> SQLAlchemy on GitHub</a>
    </div>

  </div>

  <aside>
    <div style="text-align:center;margin-bottom:12px;color:#d9f1ff">
      <h3 style="margin:6px 0">Preview</h3>
      <div class="preview card" style="padding:8px">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Entity_Relationship_Model.svg/640px-Entity_Relationship_Model.svg.png" alt="ER Diagram">
      </div>
    </div>

    <div class="card" style="margin-top:10px;padding:12px">
      <h4 style="margin:4px 0;color:#d9f1ff"><i class="fa-solid fa-code icon"></i> Quick commands</h4>
      <pre>pip3 install sqlalchemy
```

python3 main.py
sqlite3 mydb.db
.tables
SELECT * FROM users;</pre> </div>

```
  </aside>
</div>

<div class="card" id="video">
  <h2 style="color:#bfe6ff"><i class="fa-solid fa-video icon"></i> Video walkthrough</h2>
  <p>Watch a short video that shows the code in action. Click Play to view.</p>
  <div style="position:relative;padding-top:56.25%;">
    <iframe src="https://www.youtube.com/embed/woKYyhLCcnU" style="position:absolute;left:0;top:0;width:100%;height:100%;border:0;border-radius:8px" allowfullscreen title="SQLAlchemy tutorial"></iframe>
  </div>
</div>

<div class="card">
  <h2 style="color:#bfe6ff"><i class="fa-solid fa-file-lines icon"></i> Download README.md (markdown)</h2>
  <p>The button at the top (or below) will generate a markdown file with the README content and download it to your computer.</p>
  <p>If you want a ZIP with the whole project (main.py, requirements.txt, README.md) — press <strong>Download repo</strong> below.</p>
  <div style="margin-top:10px">
    <a class="btn btn-primary" href="#" onclick="downloadMarkdown()"><i class="fa-solid fa-file-arrow-down"></i> Download README.md</a>
    <a class="btn btn-ghost" href="#" onclick="downloadZip()" style="margin-left:8px"><i class="fa-solid fa-file-zipper"></i> Download repo (zip)</a>
  </div>
</div>

<div class="card">
  <h2 style="color:#bfe6ff"><i class="fa-solid fa-list-check icon"></i> What was requested (summary)</h2>
  <ul>
    <li>Do not show repository internal structure in the README</li>
    <li>Include photos, video, buttons and icons using HTML</li>
    <li>Provide download buttons and links to different resources</li>
    <li>All resources must be different</li>
  </ul>
  <p style="color:#9fb7d3">This HTML file follows your requests and includes all elements above. Use the download buttons to get files locally.</p>
</div>
```

  </div>

  <footer>
    Built for you — press "Download README.md" to save the markdown file.
  </footer>

  <script>
    // markdown content to download
    const README_MD = `# SQLAlchemy ORM — Demo

This demo shows basic use of SQLAlchemy ORM with SQLite.

## What it includes
- Creating database
- Defining a model
- Inserting data
- Querying data
- Updating and deleting rows

## How to run


1. Install dependencies:
```
pip3 install sqlalchemy
```
2. Run the demo:
```
python3 main.py
```

## Resources
- https://docs.sqlalchemy.org
- https://sqlitebrowser.org
- https://www.youtube.com/watch?v=woKYyhLCcnU

## Quick commands
```
sqlite3 mydb.db
.tables
SELECT * FROM users;
```

`;

    function download(filename, text) {
      const a = document.createElement('a');
      const blob = new Blob([text], {type: 'text/markdown'});
      const url = URL.createObjectURL(blob);
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    }

    function downloadMarkdown(){
      download('README.md', README_MD);
    }

    function downloadZip(){
      // create simple zip with three files using JSZip if available, otherwise download README only
      if(window.JSZip){
        const zip = new JSZip();
        zip.file('README.md', README_MD);
        zip.file('main.py', `from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.query(User).delete()
session.commit()
u1 = User(name=\"Azer\", age=14)
u2 = User(name=\"Leyla\", age=16)
session.add_all([u1,u2])
session.commit()
print(\"Inserted 2 Users\")`);
        zip.file('requirements.txt', 'sqlalchemy');
        zip.generateAsync({type:'blob'}).then(function(content){
          const a = document.createElement('a');
          const url = URL.createObjectURL(content);
          a.href = url; a.download = 'sqlalchemy-orm-demo.zip'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
        });
      } else {
        // fallback: download README only
        download('README.md', README_MD);
        alert('ZIP fallback: JSZip not loaded, downloaded README only.');
      }
    }
  </script>

  <!-- JSZip CDN (optional for zip download) -->

  <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>

</body>
</html>

<a href="https://www.youtube.com/watch?v=woKYyhLCcnU" target="_blank" style="display:block;padding:10px;background:#0f172a;border-radius:8px;margin:6px 0;color:#d9f1ff;text-decoration:none;">
<i class="fa-brands fa-youtube"></i> SQLAlchemy Tutorial (YouTube)
</a>

<a href="https://github.com/sqlalchemy/sqlalchemy" target="_blank" style="display:block;padding:10px;background:#0f172a;border-radius:8px;margin:6px 0;color:#d9f1ff;text-decoration:none;">
<i class="fa-brands fa-github"></i> SQLAlchemy on GitHub
</a>

---

# 🖼 Preview

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Entity_Relationship_Model.svg/640px-Entity_Relationship_Model.svg.png" width="500" style="border-radius:8px">

---

# 🧪 Quick commands

pip3 install sqlalchemy
python3 main.py
sqlite3 mydb.db
.tables
SELECT * FROM users;



---

# 🎥 Video Walkthrough <a name="video"></a>

<div style="position:relative;padding-top:56%;margin:20px 0;">
<iframe 
    src="https://www.youtube.com/embed/woKYyhLCcnU" 
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;border-radius:8px;"
    allowfullscreen>
</iframe>
</div>

---

# 📥 Downloads <a name="downloads"></a>

Since GitHub cannot run JavaScript download scripts,  
**you must manually create the README.md file using this content**.

For full project download, add a ZIP manually.

---

# 📝 What was requested

✔ Don't show repo file structure  
✔ Include photos, videos, icons, HTML  
✔ Add resource buttons  
✔ Add different types of resources  
✔ Keep HTML styling inside README.md  

---

<div align="center" style="color:#9fb7d3;padding:20px;">
Made for you — enjoy your fully interactive GitHub README.
</div>
