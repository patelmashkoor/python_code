# CLUTTER CLEANER/ FOLDER CLEANER.

import os

def CreateIfNotExist(folder):
    if not os.path.exists ( folder ):
        os.listdir ()

def move (folderName,files):
    for file in files:
        os.replace ( file, f"{folderName}/{file}" )

files = os.listdir ()
files.remove ( "main.py" )
print ( files )
CreateIfNotExist ( 'images' )
CreateIfNotExist ( 'docs' )
CreateIfNotExist ( 'medias' )
CreateIfNotExist ( 'Others' )

imgExts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext( files )[1].lower() in imgExts]

docExts = [".doc", "docx", ".xlsx", ".txt", ".pdf"]
docs = [file for file in files if os.path.splitext( files )[1].lower() in docExts]

mediaExts = [".flv", ".mp4", ".mp3"]
medias = [file for file in files if os.path.splitext( files )[1].lower() in mediaExts]


others = []
for file in files:
    ext = os.path.splitext( files )[1].lower ()
    if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile ( file ):
        others.append( file )


move("Images",images)
move("Docs",docs)
move("Medias",medias)
move("Others",others)
