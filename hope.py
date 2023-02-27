import wave
import array

# open the input WAV file
with wave.open('samplewithnoise.wav', 'rb') as wave_file:
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
        print(f'slice_{i+1}.wav')

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
        print(f'slice_{num_slices+1}.wav')
