import os
from os import path
from posixpath import dirname
import shutil
#           [----------------------------------FILES EXTENSIONS------------------------------------------------------]
soundEx = ('.3ga','.aac','m3u','m3u8','.aiff','.amr','.ape','.arf','.asf','.asx','.cda','.dvf','.flac','.gp4','.gp5','.gpx','.mp3','.wav','.wma','.wpl')
imageEx = (".jpg",'.xpm','.xcf.gz','.xcf',".png",".gif",".webp",".jpeg",".ai",".bmp",".ico",".ps",".psd",".svg",".tif",".tiff")
videoEx = ('.mp4','.mov','.avi','.flv','.mkv','.wmv','.avchd','.webm','.264','avc','.h264','.mpeg-4')
compressedEX = ('.gz','.tar.bz2','.tar.gz','.7z','.tgz',".bz2",'.arj','.bin','.cab','deb','.hqx','.rar','.iso','.lha','.ear','.rpm','.jar','.tar','.sit','.sea','.zip','.war')
windowsprogEx = ('.exe','.msi')
#           [----------------------------------FILES EXTENSIONS------------------------------------------------------]

thePath = input("enter the apslote path: "r"")
some    =    path.abspath(thePath)
checkk = os.listdir(some)
pdfdir = "PDFs"
musicdir = "Audio"
imagedir = "Images"
videodir = "Videos"
compressedfilesdir = "Ziped_files"
windowsprogdir = "windows_applications"
pdfspath = os.path.join(thePath, pdfdir)
musicpath = os.path.join(thePath, musicdir)
imagepath = os.path.join(thePath, imagedir)
videopath = os.path.join(thePath, videodir)
compressedpath = os.path.join(thePath, compressedfilesdir)
windowsprogpath = os.path.join(thePath, windowsprogdir)
othersdir       = "Others"
otherspath     = os.path.join(thePath, othersdir)



#     !----------------- PDFs section -----------------!
if pdfdir not in checkk:
        os.mkdir(pdfspath)
elif pdfdir in checkk:
    pass

for filename in os.listdir(some):
    srcPath = os.path.join(thePath, filename)
    if filename.endswith(".pdf"):
        print(filename)
        shutil.copy(srcPath,pdfspath)
        os.remove(srcPath)
#     !----------------- Music section -----------------!
if musicdir not in checkk:
        os.mkdir(musicpath)
elif musicdir in checkk:
    pass

for filename in os.listdir(some):
    srcPath = os.path.join(thePath, filename)
    if filename.endswith(soundEx):
        print(filename)
        shutil.copy(srcPath,musicpath)
        os.remove(srcPath)

#     !----------------- Images section -----------------!
    # V
if imagedir not in checkk:
                  # V
        os.mkdir(imagepath)
        # V
elif imagedir in checkk:
    pass

for filename in os.listdir(some):
    srcPath = os.path.join(thePath, filename)
    if filename.endswith(imageEx):
        print(filename)
                             # V
        shutil.copy(srcPath,imagepath)
        os.remove(srcPath)
                        # V
#     !----------------- Videos section -----------------!
    # V
if videodir not in checkk:
                  # V
        os.mkdir(videopath)
        # V
elif videodir in checkk:
    pass

for filename in os.listdir(some):
    srcPath = os.path.join(thePath, filename)
                          # V
    if filename.endswith(videoEx):
        print(filename)
                             # V
        shutil.copy(srcPath,videopath)
        os.remove(srcPath)

                       # V
#     !----------------- Zip section -----------------!
    # V
if compressedfilesdir not in checkk:
                  # V
        os.mkdir(compressedpath)
        # V
elif compressedfilesdir in checkk:
    pass

for filename in os.listdir(some):
    srcPath = os.path.join(thePath, filename)
                          # V
    if filename.endswith(compressedEX):
        print(filename)
                             # V
        shutil.copy(srcPath,compressedpath)
        os.remove(srcPath)

                         # V
#     !----------------- WINDOWSPROG section -----------------!
    # V
if windowsprogdir not in checkk:
                  # V
        os.mkdir(windowsprogpath)
        # V
elif windowsprogdir in checkk:
    pass

for filename in os.listdir(some):
    srcPath = os.path.join(thePath, filename)
                          # V
    if filename.endswith(windowsprogEx):
        print(filename)
                             # V
        shutil.copy(srcPath,windowsprogpath)
        os.remove(srcPath)

#     !----------------- WINDOWSPROG section -----------------!
    # V
if othersdir not in checkk:
                  # V
        os.mkdir(otherspath)
        # V
elif othersdir in checkk:
    pass

for filename in os.listdir(some):
        if path.isdir(thePath+"\\"+filename) == True:
            continue
        srcPath = os.path.join(thePath, filename)
        shutil.copy(srcPath,otherspath)
        os.remove(srcPath)

