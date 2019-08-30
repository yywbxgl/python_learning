import onnx
from onnx import helper
from onnx import AttributeProto, TensorProto, GraphProto
import numpy as np
import cv2
import onnxruntime.backend as backend


# 进行convlution操作
def run_bn_op(x, sacle, b, mean, var, conv_attribute, output_shape):
    # Create inputs (ValueInfoProto)
    X = helper.make_tensor_value_info('X', TensorProto.FLOAT, list(x.shape))
    input_sacle = helper.make_tensor_value_info('scale_scale', TensorProto.FLOAT, list(sacle.shape))
    input_b = helper.make_tensor_value_info('scale_b', TensorProto.FLOAT, list(b.shape))
    input_mean = helper.make_tensor_value_info('bn_mean', TensorProto.FLOAT, list(mean.shape))
    input_var = helper.make_tensor_value_info('bn_var', TensorProto.FLOAT, list(var.shape))

    # Create output (ValueInfoProto)
    Y = helper.make_tensor_value_info('Y', TensorProto.FLOAT, output_shape)

    # Create initializer
    sacle_data = sacle.flatten()
    sacle_data = list(sacle_data)
    init_scale = helper.make_tensor(
        name = "scale_scale",
        data_type = TensorProto.FLOAT,
        dims = list(sacle.shape),
        vals = sacle_data, 
        raw = False
    )

    b_data = b.flatten()
    b_data = list(b_data)
    init_b = helper.make_tensor(
        name = "scale_b",
        data_type = TensorProto.FLOAT,
        dims = list(b.shape),
        vals = b_data, 
        raw = False
    )

    mean_data = mean.flatten()
    mean_data = list(mean_data)
    init_mean = helper.make_tensor(
        name = "bn_mean",
        data_type = TensorProto.FLOAT,
        dims = list(sacle.shape),
        vals = mean_data, 
        raw = False
    )

    var_data = sacle.flatten()
    var_data = list(var_data)
    init_var = helper.make_tensor(
        name = "bn_var",
        data_type = TensorProto.FLOAT,
        dims = list(var.shape),
        vals = var_data, 
        raw = False
    )

    # create node
    node = onnx.helper.make_node(
        op_type = 'BatchNormalization',
        inputs=['X', 'scale_scale', 'scale_b', 'bn_mean', 'bn_var'],
        outputs=['Y'],
        epsilon=conv_attribute["epsilon"],
        momentum=conv_attribute["momentum"],
    )

    # create graph
    graph_def = helper.make_graph(
        nodes = [node],
        name = 'test-model',
        inputs = [X, input_sacle, input_b, input_mean, input_var],
        outputs = [Y],
        initializer = [init_scale, init_b, init_mean, init_var]
    )

    # create model
    model_def = helper.make_model(graph_def, producer_name='sun')
    onnx.checker.check_model(model_def)

    # model = onnx.load(onnx_file)
    session = backend.prepare(model_def)
    output = session.run(x)
    output = np.array(output[0])
    print(output)
    print(output.shape)

    #save onnx model
    onnx.save(model_def, 'signle_op_test/BatchNormalization.onnx')
    output = np.array(output)
    np.save('signle_op_test/BatchNormalization', output)

    return output


if __name__ == "__main__":

    # 指定input
    X = np.load("signle_op_test/convlution.npy")
    sacle = np.load("weights/conv1.scale_scale.npy")
    B = np.load("weights/conv1.scale_b.npy")
    mean = np.load("weights/conv1.bn_mean.npy")
    var = np.load("weights/conv1.bn_var.npy")

    # 指定参数
    conv_attribute = {}
    conv_attribute["epsilon"] =  0.000009999999747378752
    conv_attribute['momentum'] = 0.8999999761581421

    # 指定output形状
    output_shape = [1,32,112,112]

    # 进行单步推理
    run_bn_op(X, sacle, B, mean, var, conv_attribute, output_shape)

