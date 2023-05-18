#Import the television .py file
from Television import TV

#create a class for the TestTV
class TestTV:
    def __init__(self):
        #Initialize the two objects
        self.TV1 = TV()
        self.TV2 = TV()

        #Turn on both the TVs
        self.TV1.turn_on()
        self.TV2.turn_on()

        #Get the channel for TV1
        self.TV1.set_channel(30) 
        self.TV1.set_volume(3)

        #Get the channel for TV2
        self.TV2.set_channel(3)
        self.TV2.set_volume(2)

        #Print the results
        self.TV1.volume_channel()
        self.TV2.volume_channel()

#Create an instance of the test driver then run the code
TestTV()