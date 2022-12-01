# This file will record audio 
import sounddevice as sd
from scipy.io.wavfile import write


def record_audio_and_save(save_path, sample_size=25):
    """
    This function will run as per given `sample_size` and captures hot word at every iteration.
    ----
    sample_size: int, default=25
        The function will run as per sample_size
    save_path: str
        Path to save the wav file generated in every iteration.
    """

    input("Start Hot word recording press Enter: ")
    for i in range(sample_size):
        fs = 44100
        seconds = 2
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(save_path + str(i) + ".wav", fs, myrecording)
        input(f"Press to record next or two stop press ctrl + C ({i + 1}/{sample_size}): ")

def record_sound_background(save_path, sample_size=25):
    """
    This function will record background sound as per `sample_size`.
    The recorded sound will not contain Hot word.
    Parameters
    ----
    The function will run as per sample_size
    save_path: str
        Path to save the wav file generated in every iteration.
        Note: The save path should not be same Hot word recorded audio files.
    """

    input("To start recording your background sounds press Enter: ")
    for i in range(sample_size):
        fs = 44100
        seconds = 2 
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(save_path + str(i) + ".wav", fs, myrecording)
        print(f"Currently on {i+1}/{sample_size}")

#1: Record Hot word
print("Recording the Hot Word:\n")
record_audio_and_save("hotword_sound/", sample_size=100) 

#2: Record your background sounds (Just let it run, it will automatically record)
print("Recording the Background sounds:\n")
record_sound_background("background_sound/", sample_size=100)