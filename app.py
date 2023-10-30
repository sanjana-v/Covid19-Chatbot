import nltk
import pickle
import numpy
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from keras.models import load_model
model = load_model('model.h5')
import json
import random
import numpy as np
intents = pickle.load(open('intents.pkl','rb'))
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('categories.pkl','rb'))
nltk.download('punkt')
nltk.download('wordnet')
from flask import Flask, render_template, request, jsonify
app = Flask(__name__,template_folder='templates',static_url_path='/static')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/get')
def get_bot_response():
    sentence = request.args.get('msg')
    if len(sentence) <3:
        return "Invalid input."
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words] 
    # bag of words 
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current is present
                bag[i] = 1
                
    p = np.array(bag)
   
    results = model.predict(np.array([p]))[0]
    results_index = numpy.argmax(results) 
    tag = classes[results_index] 
    if results[results_index] > 0.72: 
        for tg in intents["intents"]: 
            if tg['tag'] == tag: 
                responses = tg['responses'] 
        res="COVID-BOT:"+random.choice(responses)
        return str(res)
    else: 
        res="COVID-BOT:I am sorry but I can't understand, Please contact the HELPLINE for this information"
        return str(res)
   
    return "Missing Data!"



if __name__ == "__main__":
	app.run()
