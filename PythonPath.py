# Absolute path -from root directory
# relative path - from current directory

from pathlib import Path

#p = Path('.')

chic = Path('crimes-in-chicago') 
sel = Path('CrawlerWikipedia.py')
print(chic.exists()) # .exists() works with folders and files
print(sel.exists())

folder = Path('Folder')
print(folder.mkdir())
print(folder.rmdir())
print(folder.exists())

path = Path('.')
print([doc for doc in path.iterdir() if doc.is_dir()]) # lists directories
print(list(path.glob('*.*'))) # lists files
print(Path('FCCResponsiveWebDesPrinciples.html').is_dir(),Path('FCCResponsiveWebDesPrinciples.html').exists())


text = Path('PythonText.txt') # using Path to access .txt files
with open(text, 'r') as t:
    print(t.readlines())

p = Path()
py_files = p.glob('*.py') # glob returns a generator object
print(type(py_files))  

for x in py_files: # Print all .py files
    print(x)