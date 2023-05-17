class TV:
    def __init__(tv_set, channel=int, volume=int, status=bool):
        tv_set.channel=channel
        tv_set.volume=volume
        tv_set.status=status
    
    #Sets the condition for turning TV on
    def tv_on(tv_set):
        tv_set.status=True
    #Sets the condition for turning TV off
    def tv_off(tv_set):
        tv_set.status=False
    #Sets the volume of the TV
    def tv_volume(tv_set, volume):
        tv_set.volume=volume
    #Sets the channel of the TV
    def tv_channel(tv_set, channel):
        tv_set.channel=channel
    #Tells us what the current volume and the channel of the TV set
    def know_tv_volume(tv_set):
        return tv_set.volume
    def know_tv_channel(tv_set):
        return tv_set.channel