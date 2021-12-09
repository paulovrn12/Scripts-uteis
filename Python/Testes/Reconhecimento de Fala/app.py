import speech_recognition as sr

rec = sr.Recognizer() # reconhecimento de audio
print(sr.Microphone().list_microphone_names())

#with sr.Microphone() as mic:


