import numpy as np
from openvino.runtime import Core
from transformers import GPT2Tokenizer

# Initialize the tokenizer globally
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Initialize OpenVINO core and load the model
ie = Core()
# Update this line to reflect the actual path where your model files are stored
compiled_model = ie.compile_model("E:/projects/Project_oneAPI_hack_kpr/Algowhiz-Demo/models/ir_model/gpt2.xml", "CPU")


def infer_openvino(question):
    # Tokenize the input question
    encoded_input = tokenizer(question, return_tensors='np')
    input_ids = encoded_input['input_ids']

    # Reshape input_ids to ensure it is in the expected format
    input_ids = input_ids.reshape(1, 1)  # Ensure shape is (1, 1)

    # Check the final shape of input_ids
    print(f"Reshaped input_ids shape: {input_ids.shape}")

    # Run inference using the compiled OpenVINO model
    output = compiled_model([input_ids])

    return output

