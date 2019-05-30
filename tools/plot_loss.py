import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#lines = open('models/model4/resnet50/caffe.INFO','r').readlines()
lines = open('models_180910/model3/resnet50/caffe.INFO','r').readlines()

train_loss = []
test = [[] for _ in range(2)]
iter,iter_test = [],[]
i = 0
idx = [0,1]
nlines = len(lines)
while i < nlines:
    line = lines[i]
    # if 'solver.cpp:218] Iteration' in line:
    if 'solver.cpp:239] Iteration' in line:
        line = line.split()
        iter.append(int(line[5]))
        train_loss.append(float(line[-1]))
        i += 1
    elif 'Testing net (#0)' in line:
        line = line.split()
        # print(line)
        i += 1
        if i >= nlines:break
        while 'Restarting data prefetching from start.' in lines[i] \
            or 'blocking_queue.cpp:49] Waiting for data' in lines[i]:
            i += 1
            if i >= nlines:break
        if i+3 >= nlines:break
        for n,j in enumerate(idx):
            try:
                test[n].append(float(lines[i+j].split()[-1]))
            except:
                print(i,j)
                print(line)
                for n,j in enumerate(idx):
                    print(lines[i+j])
        iter_test.append(int(line[5][:-1]))
        i += 3
    else:
        i += 1

labels = ['acc/top-1','acc/top-5']
# print('train_iter: ', iter)
# print('train_loss:', train_loss)
# print('test_iter: ', iter_test)
# print('test: ', test)
# for i, t in enumerate(test):
#   print('test_loss ({}): {}'.format(labels[i],t))
        
plt.plot(iter,train_loss,label='train loss', color='b')
plt.ylim([0,1])

plt.twinx()
plt.ylim([0.85,1.01]) 
colors = ['r','g']
for i, t in enumerate(test):
    plt.plot(iter_test,t,label=labels[i],color=colors[i])
plt.legend()

# find the max-acc and corres-index for top-1 and top-5
for i, t in enumerate(test):
    t = np.asarray(t,dtype=np.float32)
    # print(t.shape)
    t = t[::-1]
    # print(t.argmax())
    idx = len(t)-t.argmax()-1
    print(labels[i], iter_test[idx], t.max())


# find the test model with corres-iter
print('-------    model    --------') 
for i, t in enumerate(test):
    t = np.asarray(t,dtype=np.float32)
    iter_test_array = np.asarray(iter_test)
    idx  = np.where((iter_test_array % 10000)==0)
    # print(idx)
    t = t[idx]
    iter_test_array = iter_test_array[idx]
    # print(t.shape)
    t = t[::-1]
    # print(t.argmax())
    idx = len(t)-t.argmax()-1
    print(labels[i], iter_test_array[idx], t.max())    

plt.savefig('loss_180910.png')
# plt.show()
# print(iter)
# print(train_loss)
# print(iter_test)
# print(test)
