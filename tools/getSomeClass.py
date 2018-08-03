#!/usr/bin/env python
import os
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import global_dir
from random import shuffle
from collections import OrderedDict
import shutil

file_type_list =['GIF', 'gif', 'jpeg',  'bmp', 'png', 'JPG',  'jpg', 'JPEG']
#file_type_list = ['jpg']

# note: JPEGImages and Annotations are contained in data_dir
def extractVOCSomeClass(src_data_dir, dst_data_dir, list_files):
    paths_src = [src_data_dir + '/JPEGImages', src_data_dir + '/Annotations']
    paths_dst = [dst_data_dir + '/JPEGImages', dst_data_dir + '/Annotations']
    lines = open(list_files, 'r').readlines()
    if not os.path.exists(paths_dst[0]):
        os.makedirs(paths_dst[0])
    if not os.path.exists(paths_dst[1]):
        os.makedirs(paths_dst[1])

    types = set()
    write_lines = []
    num_images = 0
    for line in lines:
        image_name = line.split()[0]
        label = line.split()[1]
        print label
        if label != '1':
            continue
        image_name_jpg = image_name + '.jpg'
        image_file_path = os.path.join(src_data_dir, 'JPEGImages', image_name_jpg)
        #write_lines.append((file_path.split('/')[-1]).split('.')[0] + '\n')
        xml_file_path = image_file_path.replace('JPEGImages', 'Annotations')
        xml_file_path = xml_file_path.replace('jpg', 'xml')

        write_lines.append(image_file_path + ' ' + xml_file_path + '\n')
        shutil.copy(image_file_path, paths_dst[0] + '/')
        shutil.copy(xml_file_path, paths_dst[1] + '/')
        num_images += 1
        print 'copy', num_images, image_file_path, 'to', paths_dst[0]
        print 'copy', num_images, xml_file_path, 'to', paths_dst[1]
    print 'have num_images:', num_images

    ###  write full path of image_list_path and conresponding xml_file_path
    ### to dst_data_dir/ImageSets/Main/
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
        image_path = write_lines[line].split()[0]
        image_name = image_path.split('/')[-1]
        if image_name.split('.')[-1] in file_type_list:
            image_name = image_name.split('.')[0] + '\n'
            image_lists.append(image_name)
        else:
            print 'image error', image_path
            sys.exit(2)

    image_name_files_dir = os.path.join(dst_data_dir, 'ImageSets/Main')
    if not os.path.exists(image_name_files_dir):
        os.makedirs(image_name_files_dir)
    f = open(dst_data_dir + '/ImageSets/Main/test.txt','w')
    f.writelines(image_lists[:L])
    f.close()
    f = open(dst_data_dir + '/ImageSets/Main/trainval.txt','w')
    f.writelines(image_lists[L:])
    f.close()

if __name__ == '__main__':

    # input data_dir and data list, copy to JPEGImages and Annotations of dst_data_dir
    src_data_dir = '/workspace/D2/sanjun/VOCdevkit/VOC2012'
    dst_data_dir = '/workspace/D2/sanjun/ExtractedVOCClasses/person'

    list_files = '/workspace/D2/sanjun/VOCdevkit/VOC2012/ImageSets/Main/person_trainval.txt'

    extractVOCSomeClass(src_data_dir, dst_data_dir, list_files)
