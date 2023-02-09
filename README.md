# Audio_Classifier_with_python
This is a project for a model trained to detect a specific beep sound in pre-loaded audio files or through microphone input from the external environment.

## Setting up dependecies
pip install sounddevice
pip install os
pip install librosa
pip install matplotlib
pip install numpy
pip install pandas
pip install tensorflow
pip install sklearn
pip install pyttsx3

Install any other required dependecies on raspberry pi.

## Sequence
- Collect sample data and background data using PreparingData.py
- Preprocess the collected data using Preprocessing.py
- Train the model on the collected data
- Run test.py to test trained model with pre-loaded wav files.
- Run main.py when you want to test the model with inputs from a microphone connected to your PC or to your Raspberry pi.

Happy Coding!
