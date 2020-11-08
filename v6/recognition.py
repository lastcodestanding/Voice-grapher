# import the module
import speech_recognition as sr
# create the recognizer

def rec():
    r = sr.Recognizer()

    # define the microphone
    mic = sr.Microphone(device_index=0)
    # record your speech
    with mic as source:
       audio = r.listen(source)
       sleep(5)
       break
    # speech recognition
    result = r.recognize_google(audio)
    # export the result
    with open('my_result.txt',mode ='w') as file:
       #file.write("Recognized text:")
       #file.write("\n")
       file.write(result)
    print("Exporting process completed!")

rec()
