#make a class and name it TV
class TV:
#Make a constructor with the television's functions
    def __init__(self):
        
        #Set the volume and channel to 1
        self.channel=1
        self.volume=1
        self.turn_on=True

        #Initiate the tv on and off of the tv
        def turn_on(self):
            self.turn_on=True

        def turn_off(self):
            self.turn_on=False

        #get the channel of the TV
        def get_channel(self):
            return self.channel
        
        #setting a new channel of the TV
        def set_channel(self, Channel):
            if Channel>=1 and Channel<=120:
                self.channel=Channel
        
        #Getting the volume 
        def get_volume(self):
            return self.Volume
        
        #Set the volume(1-7 only)
        def set_volume(self, volume):
            if volume>=1 and volume<=7:
                self.Volume=volume
        
        #If the user wants to change the channel up
        def channel_up(self):
            if self.channel<120:
                self.channel += 1
            else:
                self.channel = 1
        
        #if the user wants to change the channel down
        def channel_down(self):
            if self.channel>1:
                self.channel -= 1
            else:
                self.channel = 1

        # If the user want to up the volume
        def volume_up(self):
            if self.volume<=7:
                self.volume+=1
            else:
                self.volume=1
        
        #if the user want to turn the volume down
        def volume_down(self):
            if self.volume>1:
                self.volume-=1
            else:
                self.volume=7

        #Output what the class TV does
        def volume_channel(self):
            if self.turn_on:
                print("The TV's channel is:", self.channel)
                print("The TV's volume is:", self.volume)