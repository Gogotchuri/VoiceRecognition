# Voice Recognition Software #

## Dependencies ##
- python modules:
    + [Numpy](https://numpy.org/)
    + [Keras](https://keras.io/)
    + [Pandas](https://pandas.pydata.org/)
    + [Librosa](https://librosa.github.io/librosa/)
    + [SKLearn](https://scikit-learn.org/stable/)
- Linux packages for preprocessing:
    + [FFMPEG](https://www.ffmpeg.org/)
## Cloning/Compilation/Usage ##
- Clone repo with command: *git clone https://github.com/Gogotchuri/VoiceRecognition.git*
- Make preprocessing script executable:
    + Go to repo root directory
    + Make script executable and grant permissions:
        - *sudo chmod +x cut_voices.sh && sudo chmod 777 cut_voices.sh*
 ## Preprocessing Test data ##
 - *Preprocessing script is compiled for linux and only works there. Also script Requires software **[ffmpeg](https://www.ffmpeg.org/)** *
 - *Test data should be placed in a single folder (flattened) and should have extension .wav*
 - If you want to test given models, you should first preprocess test data:
    + Preprocessing script takes one argument from terminal, absolute path to test folder.
    + Executing script (path_to_test - is absolute path to test directory):
        - *./cut_voices.sh **path_to_test** *
    + This script creates new folder "test_cut" in the root directory of repository where it copies preprocessed audio file.
    + Script first converts all audio to 16KHz, Mono channel and then runs [cut_loudest_section](https://github.com/petewarden/extract_loudest_section) program, which returns loudest sections of each file. Which simplifies identification process and makes it more consistent.
 ## Key Files in the repository ##
 - **cut_voices.sh** - script to preprocess the data
 - **Speech Recognition Without Library.ipynb** - contains code, to import already trained custom model and make a prediction on a preprocessed test data.
 - **Speech Recognition With Library.ipynb** - contains code, to import already  trained keras model and make a prediction on a preprocessed test data.
 - **Train.ipynb** - Creates custom and keras models, trains them and exports trained models as separate files.
 ### Notes ###
 - For now there is some redundant code that needs to be removed from repository.
 - Also code duplication is a problem, which should be handled.
 - Average accuracy on train-test split for custom CNN model is: 72% +-4% and for Keras model is: 93% +-4%
 
