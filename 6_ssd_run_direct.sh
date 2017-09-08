./caffe train \
--solver="models/VGGNet/VOC0712/SSD_300x300/food_solver.prototxt" \
--weights="VGG_VOC0712_SSD_300x300_iter_120000.caffemodel" \
--gpu 0,1,2,3 2>&1 | tee jobs/VGGNet/VOC0712/SSD_300x300/VGG_VOC0712_SSD_300x300.log
