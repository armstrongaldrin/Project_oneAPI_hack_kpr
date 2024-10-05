from transformers import GPT2Model

# Load the GPT-2 model
model = GPT2Model.from_pretrained("gpt2")

# Save it to disk (ONNX format is recommended for conversion to OpenVINO)
model.save_pretrained("./models/original_model")
