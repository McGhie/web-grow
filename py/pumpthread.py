
import threading
import time
import water


class pumpthread(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        r = True
        while r:
            # Do something
            print('Doing something important in the background')
            water.basic()
            time.sleep(self.interval)
            r = False
            print('important in the background is done')



"""if state:
   print('on')
else:
   print('off')"""
