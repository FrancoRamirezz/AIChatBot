# AIChatBot
AI chatbot workshop. The json file can be provided or you can type one yourself following the code in the repository. I made two files of the same project, so it is easier if people need the Python file version of it
 



## JSON file
![aibotsmissaslides](https://github.com/FrancoRamirezz/AIChatBot/assets/96508706/0c0a2dff-1d15-4207-995d-788f82496785)

## Installations
```bash
!pip install tensorflow==2.7.0.
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
