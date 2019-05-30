import numpy as np
import sys,os
import cv2
caffe_root = '/workspace/dl/ssd/caffe/'
sys.path.insert(0, caffe_root + 'python')
import caffe

net_file= '/workspace/dl/ssd_play/tmp/deploy.prototxt'
caffe_model='/workspace/D2/sanjun/snapshot/mobilenetv2/_iter_120000.caffemodel'
#MobileNetSSD_deploy.caffemodel'
test_dir = "images"

if not os.path.exists(caffe_model):
    print("MobileNetSSD_deploy.caffemodel does not exist,")
    print("use merge_bn.py to generate it.")
    exit()
net = caffe.Net(net_file, caffe_model, caffe.TEST)

CLASSES = ('background', 'person')
#CLASSES = ('background',
#           'aeroplane', 'bicycle', 'bird', 'boat',
#           'bottle', 'bus', 'car', 'cat', 'chair',
#           'cow', 'diningtable', 'dog', 'horse',
#           'motorbike', 'person', 'pottedplant',
#           'sheep', 'sofa', 'train', 'tvmonitor')


def preprocess(src):
    img = cv2.resize(src, (300,300))
    img = img - 127.5
    img = img * 0.007843
    return img

def postprocess(img, out):
    h = img.shape[0]
    w = img.shape[1]
    box = out['detection_out'][0,0,:,3:7] * np.array([w, h, w, h])

    cls = out['detection_out'][0,0,:,1]
    conf = out['detection_out'][0,0,:,2]
    return (box.astype(np.int32), conf, cls)

def detect(imgfile, result_lines):
    origimg = cv2.imread(imgfile)
    image_name = os.path.basename(imgfile)
    img = preprocess(origimg)

    img = img.astype(np.float32)
    img = img.transpose((2, 0, 1))

    net.blobs['data'].data[...] = img
    out = net.forward()
    box, conf, cls = postprocess(origimg, out)
    #print box, conf, cls

    for i in range(len(box)):
       p1 = (box[i][0], box[i][1])
       p2 = (box[i][2], box[i][3])
       cv2.rectangle(origimg, p1, p2, (0,255,0))
       p3 = (max(p1[0], 15), max(p1[1], 15))
       title = "%s:%.2f" % (CLASSES[int(cls[i])], conf[i])
       cv2.putText(origimg, title, p3, cv2.FONT_ITALIC, 0.6, (0, 255, 0), 1)
       result_lines.append('%s %d %f %f %f %f %f\n' % (imgfile, int(cls[i]),
           float(conf[i]), p1[0], p1[1], p2[0], p2[1]))
    #cv2.imshow("SSD", origimg)
    cv2.imwrite(os.path.join("output_tmp", image_name), origimg)

    k = cv2.waitKey(0) & 0xff
        #Exit if ESC pressed
    if k == 27 : return False
    return True

if __name__ == '__main__':
    #for f in os.listdir(test_dir):
    #    if detect(test_dir + "/" + f) == False:
    #image_list = './build/image_lists.txt'
    image_list = '../data/test_person.txt'
    image_lines = open(image_list).readlines()
    image_lines = [line.strip() for line in image_lines]
    result_lines = []
    fp = open('./build/result.txt', 'w')
    for f in image_lines:
        f = f.strip().split(' ')[0]
        if detect(f, result_lines) == False:
           break

    print result_lines
    fp.writelines(result_lines)
