# How to run script:
To use console for input text:
```
python3 main.py
```

To use asr to recognize text:
```
python3 main.py --asr
```

# Setup libraries:

### MACOSX:

#### TTS:
```
brew install espeak
pip install pyttsx3
```

#### ASR:
```
pip3 install SpeechRecognition
pip3 install pyaudio
pip3 install google-api-python-client
pip3 install gcloud
pip3 install pocketsphinx
pip3 install PyAudio
```

#### SPACY:
```
pip install -U spacy
python -m spacy download en_core_web_sm
```



Setup your Google Cloud Account and set the environment variable GOOGLE_APPLICATION_CREDENTIALS (add it on bash_profile!!) to the file path of the JSON file that contains your service account key:
https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries

Modify the file asr/keypath.txt with your JSON path



Troubleshooting ```pip3 install pocketsphinx```:
https://github.com/bambocher/pocketsphinx-python/issues/28
#this is a test

### QUICK START SPACY:
https://spacy.io/usage


# Documentation:

### Google drive folder:
https://drive.google.com/open?id=1YAXUxJB9JZ3LmcVz-amh_N1jnGcECgld
