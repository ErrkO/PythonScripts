import os, re, shutil

FileExtension_Regex = r'\..{1,5}$'

Downloads_Path = r'F:\Users\erico\Downloads'

Applications = [ '.exe','.msi' ]
Archives = [ '.7z','.deb','.img','.iso','.rar','.zip','.zips' ]
Code = [ '.py','.pdb','.sql' ]
Document = [ '.epub','.html','.pdf','.tex','.txt' ]
Extension = [ '.vsix' ]
Image = [ '.ico','.png','.jpg' ]
Other = [ '.bin','.cache', '.ct' ]
Videos = [ '.avi' ]

Folders = [ Applications, Archives, Code,
            Document, Extension, Image,
            Videos, Other ]

def InitFolders():
    pass

def IsFile(file):
    if re.match(FileExtension_Regex,file):
        return False
    elif re.match(r'\.py ',file):
        return False
    else:
        return True

def IsOfExtension(file,lst):
    for ext in lst:
        if file == ext:
            return True
    return False

def SortFile(file):
    splits = re.findall(FileExtension_Regex,file)
    pass

def GrabExtension(file):
    return re.split(FileExtension_Regex,file[:-5])[1]

def Main():
    for file in os.listdir(Downloads_Path):
        if IsFile(file):
            SortFile(file)

Main()