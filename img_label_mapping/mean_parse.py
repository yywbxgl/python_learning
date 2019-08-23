import caffe
import numpy as np

# 使输出的参数完全显示
# 若没有这一句，因为参数太多，中间会以省略号“……”的形式代替
# np.set_printoptions(threshold='nan')

MEAN_PROTO_PATH = 'imagenet_mean.binaryproto'               # 待转换的pb格式图像均值文件路径
MEAN_NPY_PATH = 'my_mean.npy'                         # 转换后的numpy格式图像均值文件路径

blob = caffe.proto.caffe_pb2.BlobProto()           # 创建protobuf blob
data = open(MEAN_PROTO_PATH, 'rb' ).read()         # 读入mean.binaryproto文件内容
blob.ParseFromString(data)                         # 解析文件内容到blob

array = np.array(caffe.io.blobproto_to_array(blob))# 将blob中的均值转换成numpy格式，array的shape （mean_number，channel, hight, width）
mean_npy = array[0]                              # 一个array中可以有多组均值存在，故需要通过下标选择其中一组均值
print(array.shape)
print(mean_npy.shape)
print(mean_npy)
print(mean_npy[0].shape)
print(mean_npy[1].shape)
print(mean_npy[2].shape)

print(np.mean(mean_npy[0]))
print(np.mean(mean_npy[1]))
print(np.mean(mean_npy[2]))

np.save(MEAN_NPY_PATH ,mean_npy)
