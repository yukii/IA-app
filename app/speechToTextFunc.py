# regroupement des fonctions relatives au speech to text
import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment

# speech to text à partir du micro
def stt_Mic(speech_key, speech_region):

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    speech_config.speech_recognition_language="fr-FR"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    
    text = ""
    error = ""

    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
       text = speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        error += "No speech could be recognized: {}".format(speech_recognition_result.no_match_details)
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        error += "Speech Recognition canceled: {}".format(cancellation_details.reason)
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            error += "Error details: {}".format(cancellation_details.error_details)

    return text, error


def stt_Audio(path_audio, speech_key, speech_region):
    # si le fichier est trop long le couper en plusieurs partie de 15 sec
    song = AudioSegment.from_wav(path_audio)
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    text = ""
    error = ""
    if song.duration_seconds > 15:
        # couper en plusieurs partie le fichier audio
        sec = 0
        sec_tot = song.duration_seconds
        delay = 15 * 1000
        nb = 1
        while (sec/1000) < sec_tot:
            if sec == 0:
                new_file = song[:delay]
            else:
                new_file = song[sec:(delay + sec)]
            path_newFile = 'new_' + str(nb) + '.wav'
            new_file.export(path_newFile, format="wav")

            audio_config = speechsdk.audio.AudioConfig(filename=path_newFile)

            # Creates a speech recognizer using a file as audio input, also specify the speech language
            speech_recognizer = speechsdk.SpeechRecognizer(
                speech_config=speech_config, language="fr-FR", audio_config=audio_config)
            
            result = speech_recognizer.recognize_once()
            
            # Check the result
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                text += result.text
            elif result.reason == speechsdk.ResultReason.NoMatch:
                error += "No speech could be recognized: {} \n".format(result.no_match_details)
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                error += "Speech Recognition canceled: {} \n".format(cancellation_details.reason)
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    error = "Error details: {} \n".format(cancellation_details.error_details)
            sec += delay
            nb += 1
            #print(sec)
    else:
        audio_config = speechsdk.audio.AudioConfig(filename=path_audio)

        # Creates a speech recognizer using a file as audio input, also specify the speech language
        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=speech_config, language="fr-FR", audio_config=audio_config)
            
        result = speech_recognizer.recognize_once()
            
        # Check the result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            text += result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            error += "No speech could be recognized: {} \n".format(result.no_match_details)
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            error += "Speech Recognition canceled: {} \n".format(cancellation_details.reason)
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                error += "Error details: {} \n".format(cancellation_details.error_details)

    return text, error

