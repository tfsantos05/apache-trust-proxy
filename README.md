<h2>Project in progress...</h2>
<br>
<p>The intention of this project is simple and efficient. Ending the headache of many server managers by making apache finally acknowledge it's behind a reverse proxy, to <b>stop rewriting the URL</b></p>

<h3>How ?</h3>
<p>In Lua, the URL is re-constructed manually from Nginx-sent headers like <code>X-Forwarded-Host</code> and <code>X-Forwarded-Proto</code>, performing a 'Smart Directory Slash' before Apache's builtin 'DirectorySlash' does anything.<br>Lua detects if the file is a folder before triggering any changes instead of appending / at every request.</p>

<p>As I said, this project is in progress. I count on Lua to do this easily, but I will be implmenting C mod for easy installation</p>
<h5>Stay tuned 🤪</h5>
