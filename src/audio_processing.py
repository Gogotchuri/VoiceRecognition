import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import scipy
# from python_speech_features import mfcc


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

    # matrix = mfcc(signal, sampling_rate, nfft=551)          #WE MIGHT USE THIS OR ANOTHER ALGORITHM TO CREATE MATRIX (python_speech_features library)
    # print(wav_file)
    # librosa.display.specshow(matrix, y_axis='linear')    #TO PLOT CREATED SPECTOGRAM IMAGE
    # plt.show()
    
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



def shift_audio(samples):
    sampling=samples[(samples > 200) | (samples < -200)]
    shifted_silent =sampling.tolist()+np.zeros((samples.shape[0]-sampling.shape[0])).tolist()
    return shifted_silent

# Adds random noise to audio
def add_noise(samples):
    y_noise = samples.copy()
    noise_amp = 0.005*np.random.uniform()*np.amax(y_noise)
    y_noise = y_noise.astype('float64') + noise_amp * np.random.normal(size=y_noise.shape[0])
    return y_noise

# Display audio  as image
def display_audio_diagram(samples, sample_rate):
    plt.figure(figsize=(12, 4))
    librosa.display.waveplot(samples.astype('float'), sr=sample_rate)
    plt.show()