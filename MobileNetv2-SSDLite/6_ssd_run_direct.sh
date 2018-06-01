./caffe train \
--solver="./MobileNetv2-SSDLite/voc/solver_train.prototxt" \
--gpu 0,1,2,3 2>&1 | tee /apps/liusj/jobs/MBv2-SSDLite/VOC0712/mbv2-ssdlite_300x300/VGG_VOC0712_SSD_300x300.log
#--weights="/apps/liusj/pretrained_models/Pelee/peleenet_inet_acc7243.caffemodel" \
