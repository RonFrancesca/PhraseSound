
from pythonosc.udp_client import SimpleUDPClient
import random


class OSCClient:


    def __init__(self, ip='127.0.0.1', port='1337'):
        '''
        Parameters:
        ------------
            :ip: ip adress, default = 127.0.0.1
            :port: port, default = 1337
        '''

        #initialization of values
        self.ip = ip
        self.port = int(port)
        
        try:
            #initialization of client
            self.client = SimpleUDPClient(self.ip, self.port)  
        except Exception as e:
            print('Client could not be created \n {}'.format(e))  


    #function to send values to the pure data server 
    def sendValues(self, distance):
        '''
        Parameters:
        ------------
            :distance: distance between words to be sent to the osc server (Pure Data)
        '''

        # Send distances OSC messages
        try:
            self.client.send_message("/distance", distance)  
        except Exception as e:
            print('Distances could not be sent: \n {}'.format(e))  

        return

    #function to send trigger to the pure data server
    def sendTriggerValue(self, trigger):
        '''
        Parameters:
        ------------
            :trigger: trigger to be sent to server. 1 (start conversation, the OSC messaages will start to be sent), 0 (stop conversation, all the OSC messages have been sent) 
        '''
        #send trigger message
        try:
            self.client.send_message("/trigger", trigger)
        except Exception as e:
            print('Trigger message could not be sent: \n {}'.format(e))    

        return
    

