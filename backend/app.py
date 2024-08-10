from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize the Flask app
app = Flask(__name__)

# Load the model and tokenizer
model_name = "distilgpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Define the blog generation function
def generate_blog(prompt, max_length=100):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, do_sample=True, top_k=50, top_p=0.95)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# Define the endpoint for blog generation
@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    max_length = data.get('max_length', 100)
    
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Generate blog content
    try:
        blog_content = generate_blog(prompt, max_length)
        return jsonify({'blog_content': blog_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
