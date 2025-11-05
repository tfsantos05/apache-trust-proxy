from urllib.request import urlopen
import shutil
import os

url = ""
apache_root = "/etc/apache2"
i = ""

def y_or_n(prompt:str, newline:bool = False) -> bool:
  i = ""
  while i not in ('y','n'):
    print(prompt, end="" if newline == False else "\n")
    i = input().lower()
  return True if i == 'y' else False

def fetch_file(url):
  return urlopen(url).read().decode("utf-8") 
    

i = y_or_n("Is your Apache root folder \"/etc/apache2\" ? (y/n)\n>>> ")
if (!i):
  while (os.path.isdir(i) == False):
    print("Enter your Apache directory \n>>> ",end="")
    i = input()
  apache_root = i

i = y_or_n(f"We will created a folder called 'lua' inside {apache_root} and one called 'trust-proxy' inside it. Cool? (y/n) >>> ")
if (i): 
  p = os.path.realpath(os.path.join(apache_root,"lua","trust-proxy"))
  os.makedirs(p,exist_ok=True)
  print(p + " created")
  print("Downloading and placing Lua scripts...")
  with open(os.path.realpath(os.path.join(p,"proxy_dirslash.lua")),"w") as f: f.write(fetch_file("url1"))
  print(f"proxy_dirslash.lua placed inside {p}")
  # I'll make more if needed  

# The conf file
print("Placing the conf file inside conf-available")
with open(os.path.realpath(os.path.join(apache_root,"conf_available")),"w") as f: f.write(fetch_file("url2"))

if (y_or_n("Wanna enable it now? (y/n)\n >>> ")):
  os.system("a2enconf trust_proxy")
  print("You still need to reload apache2 manually.\nBut for now it's done! Enjoy :)")

                                                                      
