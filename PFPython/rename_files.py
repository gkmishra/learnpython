import os
def rename_files():
    targetdir = "/tmp/test"
    file_list = os.listdir(targetdir)
    os.chdir(targetdir)
    #current_dir = os.getcwd()
    #print current_dir
    for file in file_list:
        newFileName = file.translate(None,"0123456789")
        print "Renaming - " + file + " To - " + newFileName
        os.rename(file , newFileName )

rename_files()
