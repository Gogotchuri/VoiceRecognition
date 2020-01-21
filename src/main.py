import glob
import numpy as np
import os
import random
import librosa


VALIDATION_SET_SIZE = 0.2


def bool_random(prob):
    r = random.random()
    if r <= prob:
        return True
    else:
        return False


def read_voice_files(dir_path):
    filenames = glob.glob(dir_path + "*.wav")
    name_to_files = dict()
    for i in range(len(filenames)):
        filepath = filenames[i]
        person_name = filepath.split("\\")[-1].split(".")[0].split("-")[:2]
        person_name = person_name[0] + " " + person_name[1]
        if person_name in name_to_files.keys():
            name_to_files[person_name].append(filepath)
        else:
            name_to_files[person_name] = [filepath]
    return name_to_files


def train_validation_split(validation_size, name_to_files):
    X_t = dict()
    X_v = dict()
    for k, v in name_to_files.items():
        for f in v:
            belongs_to_validation = bool_random(validation_size)
            if belongs_to_validation:
                if k in X_v:
                    X_v[k].append(f)
                else:
                    X_v[k] = [f]
            else:
                if k in X_t:
                    X_t[k].append(f)
                else:
                    X_t[k] = [f]

    return X_t, X_v


files_dict = read_voice_files("data/")
X_train, X_validation = train_validation_split(VALIDATION_SET_SIZE, files_dict)
print(X_train)
print(X_validation)

