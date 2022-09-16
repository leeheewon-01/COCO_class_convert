from glob import glob
from multiprocessing import Pool
train_img_list = glob('D:\\MSCOCO\\val2017\\*.txt')

def replace_in_file(file_path):
	# 파일 읽어들이기
	fr = open(file_path, 'r')
	lines = fr.readlines()
	fr.close()
	
	# old_str -> new_str 치환
	fw = open(file_path, 'w')
	for line in lines:
		sp_lines = line.split()
		if sp_lines[0] == 'None':
			new_word = '0'+' '+sp_lines[1]+' '+sp_lines[2]+' '+sp_lines[3]+' '+sp_lines[4]+'\n'
			fw.write(new_word)
		else:
			fw.write(line)
	fw.close()
	print(file_path)


if __name__ == '__main__':
	p = Pool(processes=20)
	p.map(replace_in_file, train_img_list)
	p.close()
	p.join()