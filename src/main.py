import audio_processing
from get_data import get_data
import numpy as np
import random
import scipy

X_train, X_validation = get_data("data_cut/")

random_wav = random.choice(X_train[random.choice(list(X_train.keys()))])
sample_rate, samples = scipy.io.wavfile.read(random_wav)
# audio_processing.display_audio_diagram(samples, sample_rate)
audio_processing.display_audio_diagram(audio_processing.add_noise(samples), sample_rate)


X_train = audio_processing.process_data(X_train)
X_validation = audio_processing.process_data(X_validation)

# Dataset configuration for speech recognition
y_train = np.expand_dims([e[1] for e in X_train], -1)
y_validation = np.expand_dims([e[1] for e in X_validation], -1)

# Extract spectograms from processed data
def get_pure_spectogram(train_input):
    pure_spectograms = []
    # Extracting spectograms for every entry
    for entity in train_input:
        # Every spectogram should have third dimension the same
        if entity[2].shape[1] == 31:
            pure_spectograms.append(entity[2].copy())
        # Otherwise fill dimension with 0s
        # else:
        #     remaining = 31 - entity[2].shape[1]
        #     arr = np.append( entity[2].copy(), [0 for _ in range(remaining)])
        #     print(arr.shape)
        #     pure_spectograms.append( np.append( entity[2].copy(), [0 for _ in range(remaining)]))
    # Create and return numpy 3D matrix
    return np.array(pure_spectograms, copy=True)

X_train_pure = get_pure_spectogram(X_train)
X_validation_pure = get_pure_spectogram(X_validation)
print(X_validation_pure.shape)
print(X_train_pure.shape)