#!/usr/bin/env python
import os
import cv2
from random import shuffle
from collections import OrderedDict

paths = ['testLabelImgs/JPEGImages']
file_type_list =['GIF', 'gif', 'jpeg',  'bmp', 'png', 'JPG',  'jpg', 'JPEG']
#file_type_list = ['jpg']

filenames = OrderedDict()
write_lines = []
types = set()
for path in paths:
    for root, _, files in os.walk(path):
        for fname in files:
            types.add(fname.split('.')[-1])
            if fname.split('.')[-1] in file_type_list:
                file_path = os.path.join(root,fname)
                label_name = file_path.split(path+'/')[-1]
                label_name = label_name.split('/')[0]
                if label_name in filenames.keys():
                    label = filenames[label_name][0]
                    filenames[label_name][1] += 1
                else:
                    label = len(filenames)
                    filenames[label_name] =[label,1]
                # print(cv2.imread(file_path).shape)
                # write_lines.append(file_path+' '+str(label)+'\n')
                write_lines.append((file_path.split('/')[-1]).split('.')[0] + '\n')
shuffle(write_lines)
print(types)
L  = int(len(write_lines)*0.1)
f = open('./testLabelImgs/ImageSets/Main/test.txt','w')
f.writelines(write_lines[:L])
f.close()

f = open('./testLabelImgs/ImageSets/Main/trainval.txt','w')
f.writelines(write_lines[L:])
f.close()
