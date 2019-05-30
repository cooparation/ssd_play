# coding=utf-8
#!/usr/bin/env python
import os
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import global_dir
from random import shuffle
from collections import OrderedDict
import shutil

import xml.etree.cElementTree as ET # parse xml

file_type_list =['GIF', 'gif', 'jpeg',  'bmp', 'png', 'JPG',  'jpg', 'JPEG']
#file_type_list = ['jpg']

# Brief: if the xml file has the classes
#        then get the class names and
#        corresponding object numbers
def getEachClassName_nImgs_nObjs(xml_list_path, CLASSES):
#path_root = ['./VOC2007/Annotations',
#             './VOC2012/Annotations']
#CLASSES = ["dog",  "person"]
    # [object_name, object_number]
    each_result = OrderedDict()
    xml_name = os.path.basename(xml_list_path)
    tree = ET.parse(xml_list_path)
    root = tree.getroot() # get root node
    for child in root.findall('object'):
        name = child.find('name').text
        if name in CLASSES:
           if name in each_result.keys():
               each_result[name] += 1
           else:
               each_result[name] = 1
    return each_result


##############################
# Brief: extract a lists of [classename num_images num_objects]
# note: JPEGImages and Annotations are contained in data_dir
def getTotalClassName_nImgs_nObjs(data_dir, classes, list_files):
    paths_src = [data_dir + '/JPEGImages', data_dir + '/Annotations']
    lines = open(list_files, 'r').readlines()

    types = set()
    write_lines = []
    num_images = 0
    num_objects = 0
    total_result = OrderedDict()
    for line in lines:
        image_name = line.split()[0]
        label = line.split()[1]
        if label != '1':
           continue
        image_name_jpg = image_name + '.jpg'
        image_file_path = os.path.join(data_dir, 'JPEGImages', image_name_jpg)
        xml_file_path = image_file_path.replace('JPEGImages', 'Annotations')
        xml_file_path = xml_file_path.replace('jpg', 'xml')
        each_result = getEachClassName_nImgs_nObjs(xml_file_path, CLASSES)
        #print 'each_result', each_result
        for key in each_result.keys():
            if key in total_result.keys():
                #num images
                total_result[key][0] += 1
                #num Objects
                total_result[key][1] += each_result[key]
            else:
                total_result[key] = [1, each_result[key]]
            num_objects += each_result[key]
        if len(each_result) >= 1:
            num_images += 1

    total_result['total'] = [num_images, num_objects]
    print 'total_result:',total_result

    ###  write full path of image_list_path and conresponding xml_file_path
    ### to dst_data_dir/ImageSets/Main/
    write_lines.append('\'none\': (0, 0),'+'\n')
    for key in total_result.keys():
        write_lines.append('\'%s\': (%d, %d),' %(key, total_result[key][0],
            total_result[key][1]) + '\n')
    f = open('name_nImgs_nObjs.txt','w')
    f.writelines(write_lines)
    f.close()

if __name__ == '__main__':

    # input data_dir and data list, copy to JPEGImages and Annotations of dst_data_dir
    data_dir = '/workspace/D2/sanjun/VOCdevkit/VOC2012'

    list_files = '/workspace/D2/sanjun/VOCdevkit/VOC2012/ImageSets/Main/person_trainval.txt'

    CLASSES = ['person']

    getTotalClassName_nImgs_nObjs(data_dir, CLASSES, list_files)
