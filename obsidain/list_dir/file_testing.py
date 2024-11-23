from pathlib import Path
import os


pure_path = (Path(__file__))
pure_path_2 = Path(r'C:\Users\oyalu\Documents\Storage-Cloud-SE\Storage-Cloud-SE\Django\obsidain\list_dir\Test.py')

x = pure_path/'4'
print('\n',x,type(x))
x= pure_path_2.relative_to('list_dir')
print(x)