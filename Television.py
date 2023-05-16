#make a class and name it TV
class TV:
#Make a constructor with the television's functions
    def __init__(self, turnOn, turnOff, getChannel, setChannel, getVolume, setVolume, channelUp, channelDown, volumeUp, VolumeDown):

        #Initiate the tv on and off of the tv
        self.turnOn=True
        self.turnOff=False

        #Set the volume and channel to 1
        self.channel=1
        self.volume=1

        #get the channel of the TV
        def getChannel():
            return self.channel
        
        #setting a new channel of the TV
        def setChannel(channel):
            if channel>=1 and channel<=120:
                self.channel=channel
        
        #Getting the volume 
        def getVolume():
            return self.Volume
        
        #Set the volume(1-7 only)
        def setVolume(volume):
            if volume>=1 and volume<=7:
                self.volume=volume
        
        #If the user wants to change the channel up
        def channelUp():
            if self.channel<120:
                self.channel += 1
            else:
                self.channel = 1
        
        #if the user wants to change the channel down
        def channelDown():
            if self.channel>1:
                self.channel -= 1
            else:
                self.channel = 1

        # If the user want to up the volume
            if self.volume<=7:
                self.volume+=1
            else:
                self.volume=1
#Create the first object
#Create the second object
#Output the two object