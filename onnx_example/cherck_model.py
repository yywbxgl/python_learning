import onnx
import sys
from onnx import helper, shape_inference

if len(sys.argv) != 2:
    print ("Usage:", sys.argv[0], " ONNX Model")
    sys.exit(-1)

# Preprocessing: load the ONNX model
model_path = sys.argv[1]
onnx_model = onnx.load(model_path)
# print('The model is:', onnx_model)

# Check the model
onnx.checker.check_model(onnx_model)
print('The model is checked!')


inferred_model = shape_inference.infer_shapes(onnx_model)
onnx.checker.check_model(inferred_model)
print('The model inferred!')

onnx.save(inferred_model, './shape2.onnx')