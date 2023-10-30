# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:58:50 2020

@author: Rahul Raman R
"""
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random


words=[]
categories = []
documents = []
passoverwords = ['?', '!']
intent_file = open("covid1.json", encoding="utf-8").read()
intents = json.loads(intent_file)


for intent in intents['intents']:
    for pattern in intent['patterns']:

        #To tokenise each word.
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        # appending to the doc
        documents.append((word, intent['tag']))

        # adding the class to classes
        if intent['tag'] not in categories:
            categories.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in passoverwords]
words = sorted(list(set(words)))

categories = sorted(list(set(categories)))

print (len(documents), "documents")

print (len(categories), "TAGS", categories)

print (len(words), "unique words after lematization", words)


pickle.dump(words,open('words.pkl','wb'))
pickle.dump(categories,open('categories.pkl','wb'))

# preparing data for training
training = []
output_empty = [0] * len(categories)
for doc in documents:
    # bag of words is initialised
    bag = []
    # tockenised words for pattern
    pattern_words = doc[0]
    # we are lemmatizing each word here to get its related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # in bag of words we insert 1 when a word is present or 0 when not found in pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[categories.index(doc[1])] = 1

    training.append([bag, output_row])
# we first shuffle the features and turn it into a np.array
random.shuffle(training)
training = np.array(training)
# create train and test lists. X - patterns, Y - intents
train_x = list(training[:,0])
train_y = list(training[:,1])
print("Training data created")

# Here we create a sequential model with 3 layers(1st-128 nuerons, 2nd-64 neurons and 3rd-no. of intents to predict)
# we use softmax to predict the output intent.
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))


#To prevent gradient descent we use Stochastic gradient descent with Nesterov accelerated gradient.
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#we fit the model and then save it.
final_model = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

model.save('model.h5', final_model)
# we pickle our intents to ease working with them in the app.py
pickle.dump(intents,open('intents.pkl','wb'))

print("model created")
# -*- coding: utf-8 -*-

