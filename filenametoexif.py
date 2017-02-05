#!/usr/bin/env python3

# A python script to tag photos times based on their filenames. 
#
# This was written when I had a bunch of pictures with their exif data stripped. It
# automates the tagging process using the filename.
#
# Requires piexif (pip3 install piexif)

import piexif
#import pprint #Used for Testing - no longer needed.
import os

# Insert the source of pictures
source = './Pics'

def file_list(path): #Returns the list of directories in said path (as a list)
	files = []
	os.chdir(path)
	for item in os.listdir(os.getcwd()):
		if item[-3:] == 'jpg' or item[-4:] == 'jpeg':
			files.append(item) #adding another item to list
	return files


def write_exif(photo,date):
	exif_dict = piexif.load(photo)
	exif_dict['Exif'] = {36867:date,36868:date}
	exif_bytes = piexif.dump(exif_dict)
	print(photo)
	piexif.insert(exif_bytes,photo)


def tag():
	for f in file_list(source):
		# Hardcoded pattern to follow for getting date out of filename
		date = f[4:8]  + ':' + f[8:10] + ':' + f[10:12] + ' ' + f[13:15] + ':' + f[15:17] + ':' + f[17:19]
		write_exif(f,date)
		#print(date)




#file_list(source)
tag()
