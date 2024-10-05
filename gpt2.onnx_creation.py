from transformers import GPT2Model
import torch

# Load the GPT-2 model
model = GPT2Model.from_pretrained("gpt2")

# Dummy input for GPT-2
dummy_input = torch.tensor([[0]])

# Export to ONNX
torch.onnx.export(
    model, 
    dummy_input, 
    "./models/original_model/gpt2.onnx",
    input_names=["input_ids"], 
    output_names=["output"], 
    dynamic_axes={"input_ids": {0: "batch_size"}, "output": {0: "batch_size"}}
)
