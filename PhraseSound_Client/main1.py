#!/usr/bin/env python3
import argparse
from osc import osc_client as osc
from time import sleep
from words2midi import w2midi
import re


ASR_MODE = 2    
DEBUG = False
START = 1
STOP = 0


def setSentence(sentence, n_words_sound):
    
    n_words_sound = int(n_words_sound)
    #instatntiation of osc client class
    osc_client = osc.OSCClient()
        
    print("#########################")
    input_text = sentence

    #splitting the sentence into single words
    input_words = re.sub(r' +', ' ', input_text).strip().lower().split(' ')

    try:
        #sending starting trigger value
        #osc_client.client.send_message("/trigger", START)
        messages_list = []
        #sending distances
        for idx in range(len(input_words) - n_words_sound + 1):
                
            group_words = input_words[idx:idx+n_words_sound]  # Calculate the distance for every combination of n-consecutive words
            print("Words: ", group_words)
            #calculating the distance between the words
            dist = w2midi.difference_word(group_words, len(group_words))
            #sending distance values to osc server
            
            messages_list.append(dist)

    except Exception as e:

        print("Exception: ")
        print(str(e))
        print("Program continues...")
        return True
    else:

        osc_client.sendTriggerValue(START)
        for message in messages_list:
            osc_client.sendValues(message)
            sleep(0.2)
        osc_client.sendTriggerValue(STOP)
