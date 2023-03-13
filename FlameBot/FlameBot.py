# How to use:
# 1. set up keybinds how u want (↓)
# 2. start the script whenever you want
# 3. press `startFlameKey` (preferably at the start of game)
# 4. your flame is ready just press `flameKey` and enjoy (¬‿¬)

# ==================== OPTIONS ====================
startFlameKey = '='
flameKey = '*'
ultiFlameKey = 'R'
# =================================================

from pynput import keyboard
import keyboard as flame
import time
import random


insults = []
Rinsults = []

kys1 = False
kys2 = False
Rflame = False


def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k in [flameKey]: # default insults
        global kys1
        kys1 = True
        return False
    if k in [ultiFlameKey]: # insults when ulting
        global kys2
        global Rflame
        kys1 = True
        Rflame = True
        return False
    elif k in [startFlameKey]:  # reset insults
        global kys2
        kys2 = True
        return False

def init():
    global insults
    global Rinsults

    flame.press_and_release('Shift + Enter')
    time.sleep(0.05)
    flame.write("Good fun. Have luck. <3")
    time.sleep(0.05)
    flame.press_and_release('Enter')

    insults = ["my team is so bad they can't even win a surrender vote",
               "not even noah can carry these animals gg",
               "Ethiopia could eat for a month the way i am feeding",
               "you’re the reason God created the middle finger",
               "you’re like my dog. He also chases his tail for entertainment.",
               "you have an entire life to be an idiot. Why not take today off?",
               "don’t worry, the first 40 years of childhood are always the hardest.",
               "if you have a problem with me, write the problem on a piece of paper, fold it, and shove it up your ass.",
               "I thought of you today. It reminded me to take out the trash.",
               "you bring everyone so much joy when you leave the room",
               "did the mental hospital test too many drugs on you today?",
               "when you look in the mirror, say hi to the clown you see in there for me, would you?",
               "you are proof God has a sense of humor",
               "you must have been born on a highway. That’s where most accidents happen.",
               "grab a straw, because you suck",
               "mirrors can’t talk. Lucky for you, they can’t laugh, either.",
               "if I wanted to kill myself, I would climb to your ego and jump to your IQ.",
               "your only chance of getting laid is to crawl up a chicken butt and wait",
               "don’t be ashamed of who you are. That’s your parent’s job.",
               "I told my therapist about you",
               "you’re my favorite person… besides every other person I’ve ever met",
               "you’re about as useful as a screen door on a submarine",
               "I believed in evolution until I met you",
               "I bet your parents change the subject when their friends ask about you",
               "Were you born this stupid or did you take lessons?",
               "the people who tolerate you on a daily basis are the real heroes",
               "don’t feel bad. A lot of people have no talent.",
               "don’t try to think too hard. You’re so stupid it might sprain your brain.",
               "you’re living proof it’s possible to live without a brain",
               "if I said anything to offend you it was purely intentional",
               "I hope your next blowjob is from a shark",
               "You are so full of crap, the toilet’s jealous",
               "imagine if ur parents weren't siblings",
               "only thing u carry is an extra chromosome",
               "You're as useless as a white crayon",
               "You're the reason birth control exists",
               "almost penta (¬_¬)",
               "jg more diff than my K/D",
               "you play like if a hemorrhoid was brought to life",
               "Your family tree is a circle",
               "go 0/1 irl",
               "You should get a personal tree just to replace the oxygen you wasted breathing",
               "You are so ugly your birth certificate is a restraining order from mirrors"]

    Rinsults = ["Taste my juices",
                "You are so bad",
                "I will penetrate you like your mother",
                "catch my enormous pp",
                "my strategy is beyond your understanding",
                "mad cuz bad",
                "EMOTIONAL DAMAGE",
                "your team left you just like your dad when he went to buy milk"]

def write():
    global Rflame

    if not Rflame:
        flame.press_and_release('Shift + Enter')
        time.sleep(0.05)

        if len(insults) > 0:
            rand = random.randint(0, len(insults) - 1)
            flame.write(insults[rand])
            time.sleep(0.05)
            insults.pop(rand)

        flame.press_and_release('Enter')
    else:
        flame.press_and_release('Shift + Enter')
        time.sleep(0.05)

        if len(Rinsults) > 0:
            rand = random.randint(0, len(Rinsults) - 1)
            flame.write(Rinsults[rand])
            time.sleep(0.05)
            Rinsults.pop(rand)

        flame.press_and_release('Enter')
        Rflame = False

def listen():
    global listener

    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys


listener = keyboard.Listener(on_press=on_press)
listen()

while True:
    if kys1:
        write()
        kys1 = False
    elif kys2:
        init()
        kys2 = False
    elif listener.running == False:
        listen()
