# SSD project based on caffe

## Deps
* caffe-ssd: https://github.com/weiliu89/caffe.git
* commit: 9d6e8151eedf3e8d3abaecde47b788a1ec2d2156

## Usage:
* create soft link of some bin files(caffe, convert_annoset, get_image_size) with caffe-ssd project
* export PYTHONPATH=$SSD_CAFFE_ROOT/python:$PYTHONPATH
* run with the continuously num files
* 1_createXml.py: create xml formats from origin labels
* 2_createTrainVal.py: generate the test and trainval image name lists
* 3_create_list.sh: after 2_createTrainVal.py, generate the test, trainval image lists and get test image size
* 4_create_data.sh: get label map and generate LMDB datas
* 5_ssd_run.py: run ssd training and get the solver.prototxt and train_net
* 6_ssd_run_direct.sh: training the net directly based on the train_net have generated

## Note:
* testLabelImgs/JPEGImages: the jpeg images
* testLabelImgs/labels: the labels for each image
* testLabelImgs/Annotations: the labels with .xml format
* testLabelImgs/ImageSets/Main: the test and trainval txt files

## Output Dirs
* models:
* examples:
* job:
* results:
* labelmap_voc.prototxt
* test.txt
* trainval.txt
* test_name_size.txt
