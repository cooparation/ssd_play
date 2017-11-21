#!/usr/bin/env python
import os
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import global_dir
from random import shuffle
from collections import OrderedDict

file_type_list =['GIF', 'gif', 'jpeg',  'bmp', 'png', 'JPG',  'jpg', 'JPEG']
#file_type_list = ['jpg']

# note: JPEGImages and Annotations are contained in data_dir
def getTrainTestLists(data_dir):
    paths = [data_dir + '/JPEGImages']
    filenames = OrderedDict()
    types = set()
    write_lines = []
    for path in paths:
        for root, _, files in os.walk(path):
            for fname in files:
                types.add(fname.split('.')[-1])
                if fname.split('.')[-1] in file_type_list:
                    file_path = os.path.join(root, fname)
                    print 'file_path', file_path
                    label_name = file_path.split(path+'/')[-1]
                    label_name = label_name.split('/')[0]
                    if label_name in filenames.keys():
                        label = filenames[label_name][0]
                        filenames[label_name][1] += 1
                    else:
                        label = len(filenames)
                        filenames[label_name] =[label,1]
                    # print(cv2.imread(file_path).shape)
                    #write_lines.append((file_path.split('/')[-1]).split('.')[0] + '\n')
                    xml_file_path = file_path.replace('JPEGImages', 'Annotations')
                    xml_file_path = xml_file_path.replace('jpg', 'xml')

                    write_lines.append(file_path + ' ' + xml_file_path + '\n')

    shuffle(write_lines)

    L  = int(len(write_lines)*0.1)
    f = open('./data/test.txt','w')
    f.writelines(write_lines[:L])
    f.close()

    f = open( './data/trainval.txt','w')
    f.writelines(write_lines[L:])
    f.close()

    image_lists = []
    for line in range(0, len(write_lines)):
        image_path = write_lines[line].split(' ')[0]
        image_name = image_path.split('/')[-1]
        if image_name.split('.')[-1] in file_type_list:
            image_name = image_name.split('.')[0] + '\n'
            image_lists.append(image_name)
        else:
            print 'image error', image_path
            sys.exit(2)

    f = open(data_dir + '/ImageSets/Main/test.txt','w')
    f.writelines(image_lists[:L])
    f.close()
    f = open(data_dir + '/ImageSets/Main/trainval.txt','w')
    f.writelines(image_lists[L:])
    f.close()

if __name__ == '__main__':

    data_dir = '/apps/liusj/FoodDetDatasets'
    getTrainTestLists(data_dir)

    list_files = './data/test.txt'
    test_name_file = './data/test_name_file.txt'

    #root get_image_size root_dir list_files test_name_file
    os.system('./get_image_size ' + '/' + ' ' + list_files +' ' + test_name_file)
