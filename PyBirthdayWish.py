'''
Issue 1: playsound module:
    Error (on MacOSX): 
        from AppKit     import NSSound  
        ImportError: No module named 'AppKit'
    
    Solution : 
        pip install -U PyObjC #or
        pip3 install -U PyObjC

Issue 2: playsound module:
    Error (copied from stackoverflow, had the same error):
        raise IOError('Unable to load sound named: ' + sound)
        OSError: Unable to load sound named: file:///Users/rhett/Desktop/Python Projects/Sound Test/test.wav

    Solution (copied from stackoverflow, worked for me):
        I have found where the problem is. In the python3.7/site-packages/playsound.py file The developer has not checked for " " spaces in file path, so spaces character in the file path is creating trouble.
        A quick fix without changing playsound.py 's code. replace your folder name ~/Desktop/Python Projects/Sound Test/test.wav with ~/Desktop/PythonProjects/SoundTest/test.wav
        (i.e, remove spaces from folder names)
        This will fix your error.
'''











#!/usr/bin/python3

import os,random
from threading import Thread
from time import sleep

from playsound import playsound
from termcolor import colored

from config import *

# Importing module specified in the config file
art = __import__(f'arts.{artFile}', globals(), locals(), ['*'])

def replaceMultiple(mainString, toBeReplace, newString):
    """[Replace a set of multiple sub strings with a new string]

    Args:
        mainString ([string]): [String in which the replacement will be done]
        toBeReplace ([list]): [A list which elements will be replaced by a newString]
        newString ([string]): [A string which will be replaced in place of elements of toBeReplace]

    Returns:
        [string]: [Return the main string where the element of toBeReplace is replaced by newString]
    """

    # Iterate over the list to be replaced
    for elem in toBeReplace :
        # Check if the element is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString

def pprint(art,time):
    color_used = [random.choice(color)]
    colorAttribute = []
    for i in range(len(art)):
        if art[i] in colorCodes:
        	# Color attr set to blink if 9
            if art[i] == '⑨':
                colorAttribute = [colorCodes[art[i]]]
            # color attr none if 10
            elif art[i] == '⑩':
                colorAttribute = []
            # Random color if R
            elif art[i] == '®':
            	color_used = color
            else:
                color_used = [colorCodes[art[i]]]
                
        print(colored(replaceMultiple(art[i],colorCodes,''),random.choice(color_used),attrs=colorAttribute),sep='', end='',flush= True);sleep(time)

def pAudio():
    if playAudio:
        playsound(audio)
        
def pcode():
    # Print the code before wishing 
    if codePrint:
        for i in range(len(art.code)):
            print(art.code[i],sep='', end='',flush= True);sleep(codingSpeed)
        input('\n\n'+colored('python3','blue')+colored(' PyBirthdayWish.py','yellow'))
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        input()

# Clearing terminal
os.system('cls' if os.name == 'nt' else 'clear')
#pcode()
Thread(target = pAudio).start()
Thread(target = pprint, args=(art.mainArt,speed)).start()
input()
