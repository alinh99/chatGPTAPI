from flask import Flask, request, jsonify
from transformers import  GPT2Tokenizer, set_seed, pipeline, OPTModel, GPT2LMHeadModel, OPTForCausalLM, AutoTokenizer

app = Flask(__name__)

app.secret_key = 'Pss@2023'

MODEL_NAME = "./model/step_4/" 
model = OPTForCausalLM.from_pretrained(MODEL_NAME)
model = model.eval()
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
generator = pipeline('text-generation', model=f"{MODEL_NAME}", do_sample=True)

# # Define the chatbot logic
def chatbot_response(input_text):
    set_seed(32)
    response_text = generator(input_text, max_length=1024, num_beams=1, num_return_sequences=1)[0]['generated_text']
    return response_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        response_text = chatbot_response(input_text)
    else:
        input_text = ''
        response_text = ''
    return jsonify({'input_text': input_text, 'response': response_text})

if __name__ == "__main__":
    app.run(debug=True)