import os
import shutil

if __name__ == '__main__':
    shutil.rmtree('dist')
    shutil.rmtree('build')
    os.system('pyinstaller -F main.py --clean')
    # shutil.copy('dist/main.exe', '../out/')
