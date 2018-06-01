./caffe train \
--solver="PeleeNet/solver_merged.prototxt" \
--gpu 0,1,2,3 2>&1 | tee /apps/liusj/jobs/Pelee/VOC0712/Pelee_300x300/VGG_VOC0712_SSD_300x300.log
#--weights="/apps/liusj/pretrained_models/Pelee/peleenet_inet_acc7243.caffemodel" \
