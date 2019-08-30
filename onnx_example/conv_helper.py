import onnx
from onnx import helper
from onnx import AttributeProto, TensorProto, GraphProto
import numpy as np
import cv2
import onnxruntime.backend as backend


# 进行convlution操作
def run_convlution_op(x, w, conv_attribute, output_shape):
    # Create inputs (ValueInfoProto)
    X = helper.make_tensor_value_info('X', TensorProto.FLOAT, list(x.shape))
    input_w = helper.make_tensor_value_info('conv_w', TensorProto.FLOAT, list(w.shape) )

    # Create output (ValueInfoProto)
    Y = helper.make_tensor_value_info('Y', TensorProto.FLOAT, output_shape)

    # Create initializer
    conv_weight = w.flatten()
    conv_weight = list(conv_weight)
    conv_w = helper.make_tensor(
        name = "conv_w",
        data_type = TensorProto.FLOAT,
        dims = list(w.shape),
        vals = conv_weight, 
        raw = False
    )

    # create node
    node = onnx.helper.make_node(
        op_type = 'Conv',
        inputs=['X', 'conv_w'],
        outputs=['Y'],
        kernel_shape=conv_attribute["kernel_shape"],
        pads=conv_attribute["pads"],
        strides = conv_attribute["strides"],
        group = conv_attribute['group'],
        dilations = conv_attribute['dilations']
    )


    # create graph
    graph_def = helper.make_graph(
        nodes = [node],
        name = 'test-model',
        inputs = [X, input_w],
        outputs = [Y],
        initializer = [conv_w]
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
    onnx.save(model_def, 'signle_op_test/convlution.onnx')
    output = np.array(output)
    np.save('signle_op_test/convlution', output)

    return output


if __name__ == "__main__":

    # 输入 X 与 W
    x = np.load("cat.npy")
    print(x.shape)
    w = np.load("weights/conv1_W.npy")
    print(w.shape)

    # 指定convlution参数
    conv_attribute = {}
    conv_attribute["dilations"] = [1,1]
    conv_attribute['group'] = 1
    conv_attribute['kernel_shape'] = [3,3]
    conv_attribute['pads'] = [1, 1, 1, 1]
    conv_attribute['strides'] = [2, 2]

    # 指定output形状
    output_shape = [1,32,112,112]

    # 进行单步推理
    run_convlution_op(x, w, conv_attribute, output_shape)

