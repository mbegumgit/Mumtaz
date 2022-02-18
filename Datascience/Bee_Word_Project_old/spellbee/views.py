from django.shortcuts import render
from .models import BeeWord, Score
from random import randint
from . import beewordpick 

# Create your views here.
chk =None
def index(request):
    if request.method == 'POST':
        level = request.POST["level"]
        #word = request.POST["word"]
        print('Index check')
        beeword_obj = random_pick(level)
        print('level value', level)
        
        if beeword_obj is not None: 
            beewordpick.SpeakWord(beeword_obj.word)
            print('Inside obj check')
            return render(request, "Bee/check.html",{"spellbee": beeword_obj})

    
    print('No Post request')
    return render(request, "Bee/index.html")

def beeword(request, beeword_key):
    if request.method == 'POST':
        word_typed = request.POST["word"]
        spellbee = get_beeword(beeword_key)
        chk=beewordpick.CheckWord(spellbee.word,word_typed)
        
        try:
            score_new = Score.objects.get(pickword=spellbee)
            temp = score_new.pickidx
            temp += 1 
        except Exception as err:
            print(" Score table retrieve error", err)
        if chk:

            score_new.pickidx = temp
            score_new.lastscore=True
            score_new.scoreboard_pass=1
            score_new.scoreboard_fail=0
        else: 
            score_new.pickidx = temp
            score_new.lastscore=False
            score_new.scoreboard_pass=0
            score_new.scoreboard_fail=1
        spellbee.word = word_typed 
        return render(request, "Bee/beeword.html", {"spellbee": spellbee, "chk": chk})
    print('No Post request in beeword function')
    return render(request, "Bee/index.html")
    
    
def beeword_id(request,beeword_id):
    fkey = BeeWord.objects.get(id=beeword_id)
    score_data = Score.objects.get(pickword=fkey)
    return render(request, "Bee/score_view.html", {"score_tb": score_data})

def get_beeword(beeword_id):
    return BeeWord.objects.get(id=beeword_id)
    
def scoretb_update(request):
    Bee_fkey = BeeWord.objects.all()
    for i in Bee_fkey:
        score_new = Score(pickword=i,pickidx=0,lastscore="False",scoreboard_pass=0,scoreboard_fail=0)
        score_new.save()
    return render(request, "Bee/index.html")
    
def random_pick(df_level):
    
    if df_level in [None,""]:
        dummy = "No words picked! Please choose level"
        beewordpick.SpeakWord(dummy)
        return None   
    else: 
        lvl_count=BeeWord.objects.filter(level=df_level).count()
        return BeeWord.objects.filter(level=df_level)[randint(0, lvl_count - 1)]
