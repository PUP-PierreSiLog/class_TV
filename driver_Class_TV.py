from Class_TV import TV
class TVDriver:
    def TVTest(self):
        #Imports two TV sets
        first_tv=TV()
        second_TV=TV()
        #TV 1's properties
        first_tv.tv_on()
        first_tv.know_tv_channel()
        first_tv.tv_channel(30)
        first_tv.tv_volume(3)
        
        #Print TV 1's properties
        print("TV 1's channel is ", first_tv.know_tv_channel(), "and the volume is", first_tv.know_tv_volume())

driver=TVDriver()
driver.TVTest()
