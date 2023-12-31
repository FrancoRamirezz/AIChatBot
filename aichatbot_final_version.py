# -*- coding: utf-8 -*-
"""AIChatbot_final_version

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1msU-EKuH3IQYk_V6WjpGak7tq3nDFnAg

# **Getting Started**
"""



import json
# make a new file bot.json
{
    "intents":[
    {
        "tag": "greetings",
        "patterns": [
         "Hello",
         "Hi",
         "How are you",
         "Good morning",
         "Top of the morning",
         "Can I get some help?"
        ],
        "responses":[
        "Hello! Thanks for visting",
        "Hi there, how can I help?",
        "Nice to meet you, how can I help you?",
        "Good to see you again"

        ]

    },

        {"tag":"goodbyes",
        "patterns":[
            "Thanks for the help",
            "Goodbye!",
            "I'm leaving",
            "See you later!",
            "Have a good day!"]
            ,
            "responses":[
                "Take care!",
                "Thanks for shopping at @franco",
                "Hope I helped.",
                "Glad I was able to help "

            ]
        },
        {
            "tag":"shop",
            "patterns":["What products do you sell?",
                "I like to buy something",
                "Is there any special deals?",
                "What do you recommend"],

                "responses":[
               "We sell coffee, books, and provide free WIFI",
                "Buy one product and get fiffty percent off your next purchase"
                ,
                "we recommend buying a book alongside a coffee",
                ""

            ]
            },
            {
            "tag":"payments",
            "patterns":[
                "What form of payment do you accept?",
                "Do you take credit card?", "Do you accept cash"
            ],
            "responses":[
                "We take cash",
                "We take master card as well",
                "We accept VISA, Mastercard, and AMEX",
                "We accept most major credit cards"
            ]



            },
            {
                "tag": "hours",
                "patterns":[
                "What hours are you open ",
                "What are the hours of operations",
                "What is the best time to order stuff"
                ],
                "responses":[
                   "We are open nine to five",
                   "Our hours are 9 AM to 5 PM",
                   "The best time would be from the ours of operations"
                ]

            }
















    ]

}

"""**Uninstalling** **Tensorflow** **for educational Purposes**"""

!pip uninstall tensorflow
# it will ask if you want to procced, in which you should say yea

"""***Installing the right tensorflow***"""

#https://stackoverflow.com/questions/71316443/google-colab-error-import-tensorflow-keras-models-could-not-be-resolvedrepor
!pip install tensorflow==2.7.0.



"""# Importing all the libaries


> Would recomend that you use google collab for gpu purposes


"""

import tensorflow as tf
from tensorflow.keras.layers import Dense,Activation, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import Sequential
import pickle

import nltk # this is used for the toolkit fo
nltk.download('punkt') # make sure to download this part for the tokenzaton part
nltk.download('all') # use this for the lementazier for all the nlkt downloads
#import nltk
#nltk.download('all')
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
import random
import numpy as np
lementizer = WordNetLemmatizer()

"""***Reading the Json file***"""

import json
intents =json.loads(open("practicebot-2.json").read())

# if the one above does not work
#with open("practicebot.json") as json_data:
 #      intents = json.load(json_data)

with open('ai.json')as json_data:
  intents = json.load(json_data)

# tp check if the json file did work
print(intents)

"""# Setting up the json file"""

#When reffering to json files we use a key:vale pair assesment

# making empty list to make your
words = []
classes = []
documents = []
ignore_words = ["?","!",",","@"] # anything that is not found on intents
# really check on the json file
for intent in intents["intents"]:
    for pattern in intent['patterns']:
        new_char = nltk.word_tokenize(pattern)
        words.extend(new_char)
        # now add the other lists
        documents.append((new_char, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(documents)
print(new_char)
# keep the tag consisted because if the json file says tags then u will get a key error

"""**Setting the Data Up and removing duplicates**"""

new_words = [lementizer.lemmatize(word) for word in words if word not in ignore_words]
new_words = sorted( set(new_words))  # the sorted will make the words into a list, and set removes duplicate
print(new_words)

classses = sorted(set(classes))
print(classes)

"""**Removing the Unwanted** **words**"""

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl','wb'))

"""**Preprocessing the Nerual network**"""

training = []
output_empty = [0] * len(classes) # states how 0 there are in classes
for doucment in documents:
  bag = []  # the bag of words
  pattern_words = doucment[0]
  # tokenzing each word into binary
  pattern_words = [lementizer.lemmatize(word.lower()) for word in pattern_words]
  for word in words:
    bag.append(1)if word in pattern_words else bag.append(0)
  # output for 0 is used for each tag and 1 is used for the current tag
  output_row = list(output_empty)
  output_row[classes.index(doucment[1])] = 1
  training.append([bag,output_row ])
# time to randomize all of our numbers
random.shuffle(training)
training = np.array(training)

# create train and test lists
# if it gives you an warning, you can ignore it because it just google colab restrictions

train_x = list(training[: ,0])
train_y = list(training[: ,1])

""""rember nerual networks can't take strings so make it to numbers

**The Neural Network Theory**

SGD = the optimizer used for each layer
"""

model = Sequential()
model.add(Dense(128, input_shape =(len(train_x[0]),), activation ='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation = 'softmax'))

sgd = SGD(lr= 00.1, decay = 1e-6, momentum=0.9, nesterov = True)
model.compile(loss = 'categorical_crossentropy', optimizer=sgd, metrics = ['accuracy'])
mlai = model.fit(np.array(train_x), np.array(train_y),epochs  =200, batch_size=5, verbose= 1)
model.save('chatbot_model.h5',mlai)
print("chatbot is ready")

"""**Interacting with the ChatBot**"""

from tensorflow.keras.models import load_model

words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('chatbot_model.h5')

"""**Converting the numbers into strings**"""

def clean_up_sentance(sentence):
  sentence_words  =nltk.word_tokenize(sentence)
  # break the numbers back into string for
  sentence_words = [lementizer.lemmatize(word) for word in sentence_words]
  return sentence_words

def bag_of_words(sentence):
  sentence_words = clean_up_sentance(sentence)
  bag = [0] * len(words)
  # time to iterate through each one
  for w in sentence_words:
    for i, word in enumerate(words):
      if word == w:
        bag[i] = 1
  return np.array(bag)
print(bag)

"""**Making Prediction for the bot**"""

def predict_class(sentence):
  bow = bag_of_words(sentence)
  rez = model.predict(np.array([bow]))[0]
  # looking for threshold
  Error_threshold = 0.25
  result = [[i, r] for i, r in enumerate(rez) if r > Error_threshold]
  result.sort(key = lambda x:x[1], reverse = True) # have the highest proabillty first
  return_list = []
  for r in result:
    return_list.append({'intent': classes[r[0]], 'probability':str(r[1])})
    return return_list

def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bag(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>Error_threshold]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list

def get_response(intents_list, intents_json):
  tag = intents_list[0]['intent']
  list_of_intents = intents_json['intents']
  for i in list_of_intents:
    if i['tag'] == tag:
      result = random.choice[i['responses']]
      break
    return result

print(" our bot is running: congrats")

print('chatbot_model.h5')

