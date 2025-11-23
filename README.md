::: {.section .hero}
::: {style="max-width:980px;margin:0 auto"}
#  SQLAlchemy ORM --- Interactive README

An interactive HTML README with images, video, icons, resource buttons
and a built-in download button for a ready-to-use README.md file.

::: {style="margin-top:14px"}
[ Download README.md](#download "Download README.md"){.btn .btn-primary
onclick="downloadMarkdown()"} [ Watch tutorial](#video){.btn .btn-ghost
style="margin-left:8px"
onclick="document.getElementById('video').scrollIntoView({behavior:'smooth'})"}
:::
:::
:::

::: container
::: {.card .grid}
<div>

##  Quick Overview {#quick-overview style="color:#bfe6ff"}

This page shows how an ORM (SQLAlchemy) maps Python classes to database
tables and provides ready examples of creating, reading, updating and
deleting data.

\`\`\`

### How it works {#how-it-works style="margin-top:12px;color:#dff7ff"}

1.  Define a Python class that represents a table (a model).
2.  Use a session to add, query and commit objects.
3.  SQLAlchemy generates SQL under the hood and persists changes to the
    SQLite file `mydb.db`.

### Included {#included style="margin-top:12px;color:#dff7ff"}

-   HTML README with images and icons
-   Embedded YouTube tutorial
-   Download button which writes a README.md file to your machine
-   Buttons linking to official resources

### Resources {#resources style="margin-top:12px;color:#dff7ff"}

::: resources
[ SQLAlchemy Docs](https://docs.sqlalchemy.org){target="_blank"} [ DB
Browser for SQLite](https://sqlitebrowser.org){target="_blank"} [
SQLAlchemy Tutorial
(YouTube)](https://www.youtube.com/watch?v=woKYyhLCcnU){target="_blank"}
[ SQLAlchemy on
GitHub](https://github.com/sqlalchemy/sqlalchemy){target="_blank"}
:::

</div>

::: {style="text-align:center;margin-bottom:12px;color:#d9f1ff"}
### Preview {#preview style="margin:6px 0"}

::: {.preview .card style="padding:8px"}
![ER
Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Entity_Relationship_Model.svg/640px-Entity_Relationship_Model.svg.png)
:::
:::

::: {.card style="margin-top:10px;padding:12px"}
####  Quick commands {#quick-commands style="margin:4px 0;color:#d9f1ff"}

    pip3 install sqlalchemy
    ```

    python3 main.py
    sqlite3 mydb.db
    .tables
    SELECT * FROM users;
:::

\`\`\`
:::

::: {#video .card}
##  Video walkthrough {#video-walkthrough style="color:#bfe6ff"}

Watch a short video that shows the code in action. Click Play to view.

::: {style="position:relative;padding-top:56.25%;"}
:::
:::

::: card
##  Download README.md (markdown) {#download-readme.md-markdown style="color:#bfe6ff"}

The button at the top (or below) will generate a markdown file with the
README content and download it to your computer.

If you want a ZIP with the whole project (main.py, requirements.txt,
README.md) --- press **Download repo** below.

::: {style="margin-top:10px"}
[ Download README.md](#){.btn .btn-primary onclick="downloadMarkdown()"}
[ Download repo (zip)](#){.btn .btn-ghost onclick="downloadZip()"
style="margin-left:8px"}
:::
:::

::: card
##  What was requested (summary) {#what-was-requested-summary style="color:#bfe6ff"}

-   Do not show repository internal structure in the README
-   Include photos, video, buttons and icons using HTML
-   Provide download buttons and links to different resources
-   All resources must be different

This HTML file follows your requests and includes all elements above.
Use the download buttons to get files locally.
:::

\`\`\`
:::

Built for you --- press \"Download README.md\" to save the markdown
file.
