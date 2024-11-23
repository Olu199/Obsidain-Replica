from pathlib import Path
import os
import re
p = Path(r'C:\Users\oyalu\Documents\obsidian')

count = 0
for root_address,directory_address,file in os.walk(p):
    dir_name = Path(root_address).name

    if not re.search(pattern='\.',string=dir_name):
        pass

[print(c.parent.joinpath(f'{c.name}') )for c  in p.iterdir() if not re.search(pattern='^\.',string=c.name)]

     

