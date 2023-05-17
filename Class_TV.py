class TV:
    def __init__(tv_set, channel, volume, status):
        tv_set.channel=channel
        tv_set.volume=volume
        tv_set.status=status
    
    def tv_on(tv_self):
        status=True
    
    def tv_off(tv_self):
        status=False
    
    