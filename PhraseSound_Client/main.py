#!/usr/bin/env python3
import argparse
from osc import osc_client as osc
from time import sleep
from words2midi import w2midi
import re


ASR_MODE = 2    
DEBUG = False
#trigger values
START = 1
STOP = 0


def setSentence(sentence, n_words_sound):
    """
    The function receives a sentence as input and calculates the distance for every combination of n_words_sound consecutive words
    Input:
    ----------
    :sentence: sentence to process
    :n_words_sound: number of consecutive words for which the distance will be calculated
    """
    
    n_words_sound = int(n_words_sound)
    #OSC client instance
    osc_client = osc.OSCClient()
        
    print("#########################")
    input_text = sentence

    #splitting the sentence into single words
    input_words = re.sub(r' +', ' ', input_text).strip().lower().split(' ')

    try:
       
        messages_list = []
        for idx in range(len(input_words) - n_words_sound + 1):
            #creating sub-sequence of words of length n_words_sound    
            group_words = input_words[idx:idx+n_words_sound]  
            print("Words: ", group_words)
            #calculating the distance between the wordss
            dist = w2midi.difference_word(group_words, len(group_words))
            #appending the distance value to the list to be sent to the server
            messages_list.append(dist)

    except Exception as e:

        print("Exception: ")
        print(str(e))
        print("Program continues...")
        return True
    else:
        #sending starting trigeer to server
        osc_client.sendTriggerValue(START)
        for message in messages_list:
            #sending distance values list every 0.2 s
            osc_client.sendValues(message)
            sleep(0.2)
        #sending trigger stop to server
        osc_client.sendTriggerValue(STOP)
