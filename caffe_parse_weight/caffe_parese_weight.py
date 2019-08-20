import caffe

net = caffe.Net('deploy.prototxt', caffe.TEST)
conv1_weight = net.params['conv1'][0].data
file = open('conv1_weight.txt', mode='w')
for i in range(conv1_weight.shape[0]):
    file.write(str('kenel{index}\n'.format(index=i)))
    for j in range(conv1_weight.shape[1]):
        file.write(str('chanel{index}\n'.format(index=j)))
        for k in range(conv1_weight.shape[2]):
            file.write(str('{data}\n'.format(data=conv1_weight[i][j][k])))
file.close()


