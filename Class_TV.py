class TV:
    def __init__(self, channel=0, volume=0, status=True):
        self.channel=channel
        self.volume=volume
        self.status=status
    
    #Sets the condition for turning TV on
    def tv_on(self):
        self.status=True
    #Sets the condition for turning TV off
    def tv_off(self):
        self.status=False
    #Sets the volume of the TV
    def tv_volume(self, volume):
        self.volume=volume
    #Sets the channel of the TV
    def tv_channel(self, channel):
        self.channel=channel
    #Tells us what the current volume and the channel of the TV set
    def know_tv_volume(self):
        return self.volume
    def know_tv_channel(self):
        return self.channel