class TV:
    def __init__(tv_set, channel=int, volume=int, status=bool):
        tv_set.channel=channel
        tv_set.volume=volume
        tv_set.status=status
    
    def tv_on(tv_set):
        status=True
    
    def tv_off(tv_set):
        status=False

    def tv_volume(tv_set, volume):
        volume=volume
    
    