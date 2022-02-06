import os
import shutil
from pydub import AudioSegment
from pydub.silence import split_on_silence
from google.cloud import speech_v1 as speech
import base64

def split_audio_transcript_to_words(audio_path, cleandir=False):
    config = dict(language_code="en-US", sample_rate_hertz=44100, enable_word_time_offsets=True)

    audio_data = AudioSegment.from_wav(audio_path)
    sentences_audio = split_on_silence(audio_segment=audio_data, min_silence_len=500, silence_thresh=-35, keep_silence=1000)
    
    sentences_folder = "sentences"
    if not os.path.isdir(sentences_folder):
        os.mkdir(sentences_folder)
    else:
        if cleandir:
            shutil.rmtree(sentences_folder)
            os.mkdir(sentences_folder)
    
    words_folder = "words"
    if not os.path.isdir(words_folder):
        os.mkdir(words_folder)
    else:
        if cleandir:
            shutil.rmtree(words_folder)
            os.mkdir(words_folder)
    
    for i, sentence_audio in enumerate(sentences_audio):
        print(i)
        sentence_audio_filepath = os.path.join(sentences_folder, f"sentence{i}.wav")
        sentence_audio.export(sentence_audio_filepath, format="wav")

        enc = base64.b64encode(open(sentence_audio_filepath, "rb").read())
        sentence_heard = dict(content=enc)
        word_list = speech_to_word_list(config, sentence_heard)
        
        for word, starttime, endtime in word_list:
            starttime=starttime*1000
            endtime=endtime*1000
            word_audio = sentence_audio[starttime:endtime]
            word_audio_filepath = os.path.join(words_folder, f"{word}.wav")
            if not os.path.isfile(word_audio_filepath):
                word_audio.export(word_audio_filepath, format="wav")

def speech_to_word_list(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    word_list = []
    print(response.results)
    for result in response.results:
        best_alternative = result.alternatives[0]
        print(best_alternative.transcript)
        for word in best_alternative.words:
            start_s = word.start_time.total_seconds()
            end_s = word.end_time.total_seconds()
            word = word.word
            word_list.append(word, start_s, end_s) 
        return word_list
    return word_list

def main():
    audio_path = "obamashort.wav"
    split_audio_transcript_to_words(audio_path, cleandir=True)
    
if __name__ == "__main__":
    main()