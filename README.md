# AIChatBot
This was an intednded  chatbot workshop. The json file can be provided or you can type one yourself following the code in the repository. I made two files of the same project, so it is easier if people need the Python file version of it
 



## JSON file
![aibotsmissaslides](https://github.com/FrancoRamirezz/AIChatBot/assets/96508706/0c0a2dff-1d15-4207-995d-788f82496785)



## Neural Network
Learned the basics of how activation layers work. Also, we discussed what an epoch is and how it work as well

<img width="800" alt="Screenshot 2023-11-12 at 1 45 05 AM" src="https://github.com/FrancoRamirezz/AIChatBot/assets/96508706/cab9b950-d5dc-4e67-9ecd-5c0e76526261">






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
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
import random
import numpy as np
lementizer = WordNetLemmatizer()
