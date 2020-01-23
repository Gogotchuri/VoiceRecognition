### Voice Recognition Software ###

## Cloning/Compilation/Usage ##
- Clone repo with command: *git clone https://github.com/Gogotchuri/VoiceRecognition.git*
- Generate data:
    + Go to repo root directory
    + Make script executable and grant permissions:
        - *sudo chmod +x cut_voices.sh && sudo chmod 777 cut_voices.sh*
    + Generate pre-processed data: *./cut_voices.sh*
- Run program from root dir.: *python3 src/main.py*