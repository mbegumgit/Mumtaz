import pyttsx3
import fileread
class Speak():
    def __init__(self):
        self.engine = pyttsx3.init() # object creation
        """ RATE"""
        rate = self.engine.getProperty('rate')   # getting details of current speaking rate
        #printing current voice rate
        self.engine.setProperty('rate', 125)     # setting up new voice rate
        """VOICE"""
        voices = self.engine.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        self.engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
        """VOLUME"""
        volume = self.engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1
        #printing current volume level
        self.engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
    def CallEngine(self,text):
        """Speak words"""
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()

    def CheckWord(self,text,typ_word):
        
        if text == typ_word:
            new_text =text +"You are correct"
            self.CallEngine(new_text)
            return True   
        else:
            new_text =text+"You are wrong"
            self.CallEngine(new_text)
            return False 

    def SpeakWord(self,diff_level='ONE'):
        """Speak words"""
        text = fileread.Pick_Word(diff_level)
        self.CallEngine(text)     
        return text