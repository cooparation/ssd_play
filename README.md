# SSD project based on caffe

## Deps
* caffe-ssd: https://github.com/weiliu89/caffe.git
* commit: 9d6e8151eedf3e8d3abaecde47b788a1ec2d2156

## Usage:
* create soft link of some bin files(caffe, convert_annoset, get_image_size) with caffe-ssd project
* export PYTHONPATH=$SSD_CAFFE_ROOT/python:$PYTHONPATH
* write labelmap_voc.prototxt files
* run with the continuously num files
* 1_createXml.py: create xml formats from origin labels or use labelImg tools to get the xml format labels
* 2_createTrainVal.py: generate the test and trainval image name lists in ImageSets/Main, generate trainval test file lists and get test image size
* [3_create_list.sh]: optional, 2_createTrainVal.py, generate the test, trainval image lists and get test image size
* 4_create_data.sh: get label map and generate LMDB datas
* 5_ssd_run.py: run ssd training and get the solver.prototxt and train_net
* 6_ssd_run_direct.sh: training the net directly based on the train_net have generated

## Note:
* testLabelImgs/JPEGImages: the jpeg images
* testLabelImgs/labels: the labels for each image
* testLabelImgs/Annotations: the labels with .xml format
* testLabelImgs/ImageSets/Main: the test and trainval txt files
* the original labels is created by BBox-Label-Tool, the format is:  
`` object_num``  
`` className x1min y1min x1max y1max``  
`` className x2min y2min x2max y2max``  

## Output Dirs
* models:
* examples:
* job:
* results:
* data/test.txt
* data/trainval.txt
* data/test_name_size.txt

## Net Instruction
* ``http://www.cnblogs.com/hansjorn/p/7445411.html  

