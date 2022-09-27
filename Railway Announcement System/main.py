import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename): 
    '''it will change text into text.mp3 file name and this
    mp3 will play and it contain given text in audio format.'''
    mytext= str(text)
    myobj=gTTS(text=mytext,lang='hi',slow=False)
    myobj.save(filename)

    
def mergeAudios(audios):#This functions returns pydub audio segment.
    combined=AudioSegment.empty()
    for audio in audios:
        combined+= AudioSegment.from_mp3(audio)
    return combined




def generateSkeleton():
    audio=AudioSegment.from_mp3('railway.mp3') 
#1.Generate kripya dhyan dijiye.
    start=500
    finish=3650
    audio.Processed=audio[start:finish]
    audio.Processed.export("1_hindi.mp3",format="mp3")
#2. is train no and name
#3. is via city
#4. ke raste
    start=8900
    finish=9600
    audio.Processed=audio[start:finish]
    audio.Processed.export("4_hindi.mp3",format="mp3")

     
#5. is from city
#6.se anne wali
    start=10500
    finish=11600
    audio.Processed=audio[start:finish]
    audio.Processed.export("6_hindi.mp3",format="mp3")
#7. to city
#8. ko jaane wali
    start=42650
    finish=43500
    audio.Processed=audio[start:finish]
    audio.Processed.export("8_hindi.mp3",format="mp3")
#9. platform number
    start=11500
    finish=12500
    audio.Processed=audio[start:finish]
    audio.Processed.export("9_hindi.mp3",format="mp3")
#10. platform no.
#11. per aa rhi hai
    start=13500
    finish=16500
    audio.Processed=audio[start:finish]
    audio.Processed.export("11_hindi.mp3",format="mp3")
#12. ham aapke safal sukhad yatra ki kamana karte hai
    start=48000
    finish=54500
    audio.Processed=audio[start:finish]
    audio.Processed.export("12_hindi.mp3",format="mp3")

def generateAnnouncement(filename):
    df=pd.read_excel(filename)#df=dataframe

    for index,item in df.iterrows(): #iterate rows 
        '''
2. Generate- train no and name
3. Generate- via city
4. Generate- from city
5. Generate-to city
8. Generate-platform no.
        '''
        textToSpeech(str(item['train_no']) + ' ' + str(item["name"]),"2_hindi.mp3")
        textToSpeech(item["via"] ,"3_hindi.mp3")
        textToSpeech(item["from"] ,"5_hindi.mp3")
        textToSpeech(item["to"] ,"7_hindi.mp3")
        textToSpeech(item["platform"] ,"10_hindi.mp3")
        
        audios=[f"{i}_hindi.mp3" for i in range(1,13)]
        announcement= mergeAudios(audios)# list accept and return pydub object jisko export kar skte hai.
        announcement.export(f'announcement_{item["train_no"]}_{index+1}.mp3',format="mp3")
if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement('announce_hindi.xlsx')