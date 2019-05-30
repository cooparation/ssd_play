import sys
import os

# write the result to each class file
def write_detection_results(out_dir, input_result_path, label_dict):
    if not os.path.exists(out_dir):
        os.makedirs(targetDir)
    outfile_prefix = 'comp4_det_test_'
    # read the detection result lists
    detection_lines = open(input_result_path)
    detection_lines = [line.strip().split() for line in detection_lines]
    #print(detection_lines)
    fps = []
    class_num = len(label_dict)
    for i in range(0, class_num):
        #print i, label_dict[i]
        fps.append(open(os.path.join(out_dir,
            outfile_prefix+str(label_dict[i])+'.txt'), 'w'))
    for i in range(0, len(detection_lines)):
        print 'line '+ str(i + 1) + '/' + str(len(detection_lines))
        class_id = int(detection_lines[i][1])
        image_name = str(detection_lines[i][0].split('/')[-1].split('.')[0])
        det_conf = float(detection_lines[i][2])
        det_loc = map(float, detection_lines[i][3:])
        #print class_id, image_name, det_conf, det_loc
        fp = fps[class_id]
        fp.write("%s %f %f %f %f %f\n" % (image_name, det_conf, det_loc[0], det_loc[1], det_loc[2], det_loc[3]))
    
    # close the file stream
    for fp in fps:
        fp.close()

if __name__ == '__main__':
    # label_inf contains: 'class_name', 0 background
    label_path = '/workspace/dl/ssd_play/examples/label_inf.txt'
    label_inf = label_path
    
    # result contains: 'image_path class_id det_conf det_loc[4]'
    input_result_path = './build/result.txt'
    
    # ----- get label info -----
    label_lines = open(label_inf).readlines()
    label_lines = [line.strip() for line in label_lines]
    #label_lines = [line.strip().split() for line in label_lines]
    #print label_lines
    label_dict = {}
    key = 0
    for label in label_lines:
        label_dict[key] = label
        key += 1
    print label_dict
    
    class_num = len(label_dict)
    out_dir = './results'
    write_detection_results(out_dir, input_result_path, label_dict)
