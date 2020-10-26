import os
"""
Recursively converts Obsidian's image path
![[<rootFolder>/assets/subFolder/filename.png]]
into
![<default_image_caption>](<replacement>/assets/subFolder/filename.png)
in rootFolders.

Give the main folder name to rootFolder (example "hacktoberCTF-2020")
Give the default image caption  to default_image_caption or leave it blank(example "Image")
"""
replacement="../../"
rootFolder=""
default_image_caption=""
for root, dirs, files in os.walk(rootFolder, topdown=False):
    for name in files:
        if name.endswith(".md"):
            print(os.path.join(root, name))
            file_path=os.path.join(root, name)
            data=open(file_path,'r+').read()
            data=data.replace("![[",f"![{default_image_caption}](")
            data=data.replace(rootFolder+"/",replacement)
            data=data.replace("]]",")")
            open(file_path,"w+").write(data)
