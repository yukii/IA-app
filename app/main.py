# app console
# main

import speechToTextFunc as speech
import translateFunc as translate
import os


speech_key = "b7db8e5888da4c24a6bd59da48e0ee88"
speech_region = "francecentral"

inGame = True

while(inGame):
    print("What do you want to do ?")
    print("Speech to text with mic : press 1")
    print("Audio to text : press 2")
    print("Translate some text : press 3")
    print("Quit : press 4")
    user = input()

    if(user == "1"):
        text, error = speech.stt_Mic(speech_key, speech_region)
        print(text)
        if(error != ""):
            print("Some error : \n" + error)
        print("What do you want with that ?")
        print("Translate : press 1")
        print("Save in file : press 2")
        print("Quit : press 3")
        choice = input()
        if(choice == "1"):
            lang_from = input("Langage of text : ")
            lang_to = input("Langage of translate (use contry code) : ")
            translate_text = translate.translate_text(text, lang_from, lang_to)
            print(translate_text)
        elif(choice == "2"):
            if(os.path.exists("translate.txt")):
                f = open("translate.txt", "w")
            else:
                f = open("translate.txt", "x")
            f.write(text)
            f.close()
            print("Save in translate.txt")
        elif(choice == "3"):
            inGame = False

    elif(user == "2"):
        path = input("Path file : ")
        text, error = speech.stt_Audio(path, speech_key, speech_region)
        print(text)
        if(error != ""):
            print("Some error : \n" + error)
        print("What do you want with that ?")
        print("Translate : press 1")
        print("Save in file : press 2")
        print("Quit : press 3")
        choice = input()
        if(choice == "1"):
            lang_from = input("Langage of text (use contry code) : ")
            lang_to = input("Langage of translate (use contry code) : ")
            translate_text = translate.translate_text(text, lang_from, lang_to)
            print(translate_text)
        elif(choice == "2"):
            if(os.path.exists("translate_audio.txt")):
                f = open("translate_audio.txt", "w")
            else:
                f = open("translate_audio.txt", "x")
            f.write(text)
            f.close()
            print("Save in translate_audio.txt")
        elif(choice == "3"):
            inGame = False

    elif(user == "3"):
        # file ou text
        print("Translate file : press 1")
        print("Translate text : press 2")
        choice = input()
        if(choice == "1"):
            path = input("File path : ")
            f = open(path, "r")
            text = f.read()
        elif(choice == "2"):
            text = input("Your text : ")

        lang_from = input("Langage of text : ")
        lang_to = input("Langage of translate (use contry code) : ")
        # print(text)
        translate_text = translate.translate_text(text, lang_from, lang_to)
        print(translate_text)
        print("What do you want with that ?")
        print("Save in file : press 1")
        print("Quit : press 2")
        choice = input()
        if(choice == "1"):
            if(os.path.exists("translate_text.txt")):
                f = open("translate_text.txt", "w")
            else:
                f = open("translate_text.txt", "x")
            f.write(text)
            f.close()
            print("Save in translate_text.txt")
        elif(choice == "2"):
            inGame = False


