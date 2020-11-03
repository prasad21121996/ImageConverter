from PIL import Image,ImageFilter
import sys
import os

source_folder = sys.argv[1]
destination_folder = sys.argv[2]


image_list = list(filter(lambda  a : 'jpg' in a ,os.listdir(source_folder)))


for x in image_list:
	file = source_folder+ x
	img = Image.open(file)
	file_name,ext = os.path.splitext(x)
	if  False == os.path.isdir(destination_folder) :
		os.mkdir(destination_folder)
	destination_file_name = destination_folder.replace("\\",'') +'\\'+ file_name +'.png'
	print (destination_file_name)
	destination_file_name = destination_folder + file_name +'.png'
	print (destination_file_name)
	img.save(destination_file_name)





