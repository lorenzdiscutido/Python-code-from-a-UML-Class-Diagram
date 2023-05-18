#Import the television .py file
from Television import TV

#create a class for the TestTV
class TestTV:
    def test(self):
        #Initialize the two objects
        TV1 = TV()
        TV2 = TV()

        #Turn on both the TVs
        TV1.turn_on()
        TV2.turn_on()

        #Get the channel for TV1
        TV1.set_channel(30) 
        TV1.set_volume(3)

        #Get the channel for TV2
        TV2.set_channel(3)
        TV2.set_volume(2)

        #Print the results
        TV1.volume_channel()
        TV2.volume_channel()

#Create an instance of the test driver then run the code
test_run=TestTV()
test_run.test()