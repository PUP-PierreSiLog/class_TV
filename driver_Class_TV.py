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

        #second TV's properties
        second_TV.tv_on()
        second_TV.know_tv_channel()
        second_TV.tv_channel(3)
        second_TV.tv_volume(2)

        #Print TV 2's properties
        print("TV 2's channel is ", second_TV.know_tv_channel(), "and the volume is", second_TV.know_tv_volume())

driver=TVDriver()
driver.TVTest()
