import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from python_speech_features import mfcc


# Returns list of lists: [correct number, student's name, matrix of a spectogram]
def process_data(X_train):
    ls = parse_features(X_train)
    for features in ls:
        features[2] = create_spectogram(features[2])
    return ls


# Creates matrix of a spectogram 
def create_spectogram(wav_file):
    signal, sampling_rate = librosa.load(wav_file)
    matrix = librosa.amplitude_to_db(np.abs(librosa.stft(signal)), ref=np.max)

    #matrix = mfcc(signal, sampling_rate, nfft=551)          WE MIGHT USE THIS OR ANOTHER ALGORITHM TO CREATE MATRIX (python_speech_features library)
    #librosa.display.specshow(mfcc_feat, y_axis='linear')    TO PLOT CREATED SPECTOGRAM IMAGE
    #plt.show()
    
    return matrix


# Returns list of lists: [correct number, student's name, path to audio file]
def parse_features(X_train) :
    ls = []
    for wav_name, wav_files in X_train.items():
        name = wav_name[wav_name.index('/') + 1:]
        
        for audio_file in wav_files:
            number = int(''.join(ch for ch in list(audio_file) if ch.isdigit()))
            ls.append([name, number, audio_file])
    
    return ls