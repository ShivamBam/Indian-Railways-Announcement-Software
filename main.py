import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combine = AudioSegment.empty()
    for audio in audios:
        combine += AudioSegment.from_mp3(audio)
    return combine

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1. generate Kirpya Dhyan Dijiye
    start = 87900
    finish = 90200
    audioAnnounce = audio[start:finish]
    audioAnnounce.export("1_hindi.mp3", format="mp3")

    # 2. from City

    # 3. generate se chal kar
    start = 91000
    finish = 92200
    audioAnnounce = audio[start:finish]
    audioAnnounce.export("3_hindi.mp3", format="mp3")

    # 4. via-City

    # 5. generate ke Raaste
    start = 94000
    finish = 95000
    audioAnnounce = audio[start:finish]
    audioAnnounce.export("5_hindi.mp3", format="mp3")

    # 6. to-City

    # 7. generate ko jaane wali gadi sankhya 
    start = 96000
    finish = 98800
    audioAnnounce = audio[start:finish]
    audioAnnounce.export("7_hindi.mp3", format="mp3")

    # 8. train_no and train_name

    # 9. generate kuch hi samya mai platform sankhya
    start = 105500
    finish = 108200
    audioAnnounce = audio[start:finish]
    audioAnnounce.export("9_hindi.mp3", format="mp3")

    # 10. platform_no.

    # 11. generate par aa rahi hai
    start = 109000
    finish = 112550
    audioAnnounce = audio[start:finish]
    audioAnnounce.export("11_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    rEx = pd.read_excel(filename)
    print(rEx)
    for index, item in rEx.iterrows():
        # 2. generate from City
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4. generate via-City
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6. generate to-City
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8. generate train_no and train_name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10. generate platform_no.
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format='mp3')

if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")