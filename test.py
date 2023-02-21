######## IMPORTS ##########
import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np
import pandas as pd
from playsound import playsound
from tensorflow.keras.models import load_model

####DATABASE
data = pd.read_csv("Audio_database_dataset.csv", header=None)
df = pd.DataFrame(data)


####### ALL CONSTANTS #####
fs = 44100
seconds = 2
filename1 = df.iat[0,0] #Beep.wav file in database
filename2 = df.iat[1,0] #Sample wav file with beep sound and noise in background
filename3 = df.iat[3,0] #Just a noise wav file

class_names = ["Tone NOT Detected", "Tone Detected"]

##### LOADING OUR SAVED MODEL and PREDICTING ###
model = load_model("saved_model/WWD.h5")

i = 0
while True:
    
    key = input("Choose audio file in database by pressing 1, 2 or 3: ")
    print(key)
    
    try:
        if (key == '1'):
            audio, sample_rate = librosa.load(filename1)
            mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
            mfcc_processed = np.mean(mfcc.T, axis=0)
            playsound(filename1)

            prediction = model.predict(np.expand_dims(mfcc_processed, axis=0))
            if prediction[:, 1] > 0.99:
                print(f"Tone Detected for ({i})")
                print("Confidence:", prediction[:, 1])
                print("Rotate servo motor by 10 degrees")
                i += 1
    
            else:
                print(f"NOT Detected")
                print("Confidence:", prediction[:, 0])

        if (key == '2'):
            
            audio, sample_rate = librosa.load(filename2)
            mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
            mfcc_processed = np.mean(mfcc.T, axis=0)
            playsound(filename2)

            prediction = model.predict(np.expand_dims(mfcc_processed, axis=0))
            if prediction[:, 1] > 0.99:
                print(f"Tone Detected for ({i})")
                print("Confidence:", prediction[:, 1])
                print("Rotate servo motor by 10 degrees")
                i += 1
    
            else:
                print(f"NOT Detected")
                print("Confidence:", prediction[:, 0])

        if (key == '3'):
            audio, sample_rate = librosa.load(filename3)
            mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
            mfcc_processed = np.mean(mfcc.T, axis=0)
            playsound(filename3)

            prediction = model.predict(np.expand_dims(mfcc_processed, axis=0))
            if prediction[:, 1] > 0.99:
                print(f"Tone Detected for ({i})")
                print("Confidence:", prediction[:, 1])
                print("Rotate servo motor by 10 degrees")
                i += 1
    
            else:
                print(f"NOT Detected")
                print("Confidence:", prediction[:, 0])
    except:
        continue
