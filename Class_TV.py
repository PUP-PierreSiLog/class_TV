class TV:
    def __init__(tv_set, channel=1, volume=25, status=True):
        tv_set.channel=channel
        tv_set.volume=volume
        tv_set.status=status
    
    def tv_on(tv_set):
        tv_set.status=True
    
    def tv_off(tv_set):
        tv_set.status=False

    def tv_volume(tv_set, volume):
        tv_set.volume=volume

    def tv_channel(tv_set, channel):
        tv_set.channel=channel
        