import os
import shutil
from multiprocessing import Pool
import glob
train_img_list = glob.glob('D:\\MSCOCO\\val2017\\*.txt')
train_label_list = glob.glob('D:\\MSCOCO\\val2017\\*.jpg')
def move_file(file):
    shutil.move(file, "D:\\MSCOCO\\valid\\labels")
    print(file)
if __name__ == '__main__':
    pool = Pool(processes=20)
    pool.map(move_file, train_label_list)
    pool.close()
    pool.join()