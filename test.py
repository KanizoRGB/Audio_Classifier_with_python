######## IMPORTS ##########
import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import os
import numpy as np
import pandas as pd
from playsound import playsound
from tensorflow.keras.models import load_model
import wave
import array

####DATABASE
data = pd.read_csv("Audio_database_dataset.csv", header=None)
df = pd.DataFrame(data)


####### ALL CONSTANTS #####
fs = 44100
seconds = 2

class_names = ["Tone NOT Detected", "Tone Detected"]

##### LOADING OUR SAVED MODEL and PREDICTING ###
model = load_model("saved_model/WWD.h5")

i = 0
while True:
    
    j = input("Choose audio file in database by pressing a digit between 0 and 3: ")
    j = int (j)
    print(j)
    
    try:
        with wave.open(df.iat[j,0], 'rb') as wave_file:
            # get the frame rate, sample width, and number of channels
            frame_rate = wave_file.getframerate()
            sample_width = wave_file.getsampwidth()
            num_channels = wave_file.getnchannels()

            # calculate the number of frames in each slice (2 second)
            slice_frames = frame_rate * num_channels * 2

            # read the entire WAV file into an array
            audio_array = array.array('h', wave_file.readframes(wave_file.getnframes()))

            # calculate the number of slices needed
            num_slices = len(audio_array) // slice_frames

            # slice the audio into smaller WAV files and store them in an array
            audio_slices = []
            for i in range(num_slices):
                start_frame = i * slice_frames
                end_frame = start_frame + slice_frames
                slice_array = audio_array[start_frame:end_frame]
                slice_wav = wave.open(f'slice_{i+1}.wav', 'wb')
                slice_wav.setnchannels(num_channels)
                slice_wav.setsampwidth(sample_width)
                slice_wav.setframerate(frame_rate)
                slice_wav.writeframes(slice_array.tobytes())
                slice_wav.close()
                audio_slices.append(slice_array)

            # if there are any remaining frames, slice them into a final WAV file
            remaining_frames = len(audio_array) % slice_frames
            if remaining_frames > 0:
                start_frame = num_slices * slice_frames
                end_frame = start_frame + remaining_frames
                slice_array = audio_array[start_frame:end_frame]
                slice_wav = wave.open(f'slice_{num_slices+1}.wav', 'wb')
                slice_wav.setnchannels(num_channels)
                slice_wav.setsampwidth(sample_width)
                slice_wav.setframerate(frame_rate)
                slice_wav.writeframes(slice_array.tobytes())
                slice_wav.close()
                audio_slices.append(slice_array)

            
            for i in range(len(audio_slices)):
                audio, sample_rate = librosa.load(f'slice_{i+1}.wav')
                mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
                mfcc_processed = np.mean(mfcc.T, axis=0)

                prediction = model.predict(np.expand_dims(mfcc_processed, axis=0))
                if prediction[:, 1] > 0.99:
                    print(f"Tone Detected for ({i})")
                    print("Confidence:", prediction[:, 1])
                    print("Rotate servo motor by 10 degrees")
                    i += 1
    
                else:
                    print(f"NOT Detected")
                    print("Confidence:", prediction[:, 0])

        for file in os.listdir('.'):
            if file.endswith('.wav'):
                os.remove(file)

    except:
        continue
