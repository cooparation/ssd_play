./caffe train \
--solver="ResNet_SSD/solver.prototxt" \
--gpu 0,1,2,3 2>&1 | tee jobs/VGGNet/ResNet_SSD_300x300.log
#--weights="VGG_VOC0712_SSD_300x300_iter_120000.caffemodel" \
