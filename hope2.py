import wave
import array

def slice_wav_file(filename):
    # Open the WAV file
    wav_file = wave.open(filename, 'rb')

    # Get the frame rate and number of channels
    frame_rate = wav_file.getframerate()
    num_channels = wav_file.getnchannels()

    # Calculate the number of frames in 2 seconds
    frames_per_segment = frame_rate * num_channels * 2

    # Create an array to hold the sliced WAV files
    sliced_wavs = []

    # Loop through the WAV file, slicing it into 2-second segments
    while True:
        # Read in the next 2 seconds of audio
        frames = wav_file.readframes(frames_per_segment)

        # If there are no more frames, break out of the loop
        if not frames:
            break

        # Convert the frames to an array
        sliced_wav = array.array('h', frames)

        # Append the sliced WAV file to the array
        sliced_wavs.append(sliced_wav)

    # Close the WAV file
    wav_file.close()

    return sliced_wavs


if __name__ == '__main__':
    sliced_wavs = slice_wav_file('samplewithnoise.wav')
    print(len(sliced_wavs))
