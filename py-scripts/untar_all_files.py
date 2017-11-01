import tarfile,sys
import subprocess
from os import listdir
from os import path,makedirs

def untar_file(file, dir_name):

    if not path.exists(dir_name):
        makedirs(dir_name)
    print "Untar file:%s into directory %s"%(file,dir_name)
    subprocess.Popen(['tar', '-xvf', file, '-C',dir_name])

def untar(directory):
    files = listdir(directory)

    for f in files:
       if f.endswith(".tar"):
           file_directory = f[:-4]
           untar_file(f, file_directory)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: '%s directory name'" % sys.argv[0]
        sys.exit(0)
    untar(sys.argv[1])