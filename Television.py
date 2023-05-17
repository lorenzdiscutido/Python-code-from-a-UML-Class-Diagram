#make a class and name it TV
class TV:
#Make a constructor with the television's functions
    def __init__(self):
        
        #Set the volume and channel to 1
        self.channel=1
        self.volume=1
        self.turnOn=False

        #Initiate the tv on and off of the tv
        def turnOn(self):
            self.turnOn=True
        def turnOff(self):
            self.turnOn=False

        #get the channel of the TV
        def getChannel(self):
            return self.channel
        
        #setting a new channel of the TV
        def setChannel(self, Channel):
            if Channel>=1 and Channel<=120:
                self.channel=Channel
        
        #Getting the volume 
        def getVolume(self):
            return self.Volume
        
        #Set the volume(1-7 only)
        def setVolume(self, volume):
            if volume>=1 and volume<=7:
                self.Volume=volume
        
        #If the user wants to change the channel up
        def channelUp(self):
            if self.channel<120:
                self.channel += 1
            else:
                self.channel = 1
        
        #if the user wants to change the channel down
        def channelDown(self):
            if self.channel>1:
                self.channel -= 1
            else:
                self.channel = 1

        # If the user want to up the volume
        def volumeUp(self):
            if self.volume<=7:
                self.volume+=1
            else:
                self.volume=1
        
        #if the user want to turn the volume down
        def volumeDown(self):
            if self.volume>1:
                self.volume-=1
            else:
                self.volume=7

#Output what the class TV does
if __name__=="__init__":
    TV1=TV()
    TV2=TV()
    TV1.getChannel(30) 
    TV1.setVolume(3)
    TV2.setChannel(3)
    TV2.setVolume(2)
    print("TV1's channel is:", TV1.getChannel(), "and the volume is:", TV1.setVolume())
    print("TV2's channel is:", TV2.getChannel(), "and the volume is:", TV2.setVolume())