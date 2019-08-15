import os
import shutil
import time

def file_copy(filepath):
    str_time = time.strftime('%Y-%m-%d-%H%M%S')

    print('1:',str_time)
    # shutil.copy(src, dst)

if __name__ == '__main__':
    os.chdir(r'P:\\sql server')
    src = r'P:\\sql server\\master.mdf'
    file_copy(src)
