# Audio_Classifier_with_python
This is a project for a model trained to detect a specific beep sound in pre-loaded audio files or through microphone input from the external environment.

## Setting up dependecies
- pip install sounddevice
- pip install librosa
- pip install matplotlib
- pip install numpy
- pip install pandas
- pip install tensorflow
- pip install sklearn
- pip install pyttsx3
- pip install playsound==1.2.2

Install any other required dependecies on raspberry pi.

## Other Instructions
Follow instructions on this link to install FFmpeg to the root directory of your computer if you are on windows OS.
https://www.wikihow.com/Install-FFmpeg-on-Windows

If Linux OS: run this command "apt install ffmpeg"


## Follow this sequence to build your own model
- Collect sample data and background data using PreparingData.py
- Preprocess the collected data using Preprocessing.py
- Train the model on the collected data
- Run test.py to test trained model with pre-loaded wav files in the Audio_database_dataset csv file. The program will first play the audio file to an output and then determine whether it has detected the beep sound or not.
- Run main.py when you want to test the model with inputs from a microphone connected to your PC or to your Raspberry pi.

Happy Coding!
