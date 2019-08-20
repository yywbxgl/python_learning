import onnx
from onnx import helper, shape_inference
from onnx import TensorProto


# Preprocessing: create a model with two nodes, Y's shape is unknown
node1 = helper.make_node('Transpose', ['X'], ['Y'], perm=[0, 1, 3, 2])
node2 = helper.make_node('Transpose', ['Y'], ['Z'], perm=[0, 1, 3, 2])

graph = helper.make_graph(
    [node1, node2],
    'two-transposes',
    [helper.make_tensor_value_info('X', TensorProto.FLOAT, (2, 3, 224, 224))],
    [helper.make_tensor_value_info('Z', TensorProto.FLOAT, (2, 3, 224, 224))],
)

original_model = helper.make_model(graph, producer_name='onnx-examples')

# Check the model and print Y's shape information
onnx.checker.check_model(original_model)
print('Before shape inference, the shape info of Y is:\n{}'\
    .format(original_model.graph.value_info))
onnx.save(original_model, './shape1.onnx')

# Apply shape inference on the model
inferred_model = shape_inference.infer_shapes(original_model)

# Check the model and print Y's shape information
onnx.checker.check_model(inferred_model)
print('After shape inference, the shape info of Y is:\n{}'\
    .format(inferred_model.graph.value_info))
onnx.save(inferred_model, './shape2.onnx')