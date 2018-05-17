import datetime
import time

class Timestamp:
    def __init__(self):
        pass
    
    def create(self):
        return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d @ %H:%M:%S')


################
"""  Tests  """
################
debug = False

if debug is True:
    # Instantiate
    ts = Timestamp()

    # Print
    print(ts.create())