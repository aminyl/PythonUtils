"""
Manage timers.

Examples
--------
>>> timers = Timer()

>>> timers.start()
>>> timers.start(0)
>>> timers.start("build")

After 1 sec:
>>> timers.end()
1
>>> timers.show(0, printing=True)
1 sec
1
>>> timers.end("build")
1

After another 1 sec:
>>> timers.end()
1
>>> timers.end(0, printing=True)
2 sec
>>> timers.show("build", printing=True)
build: 2 sec
"""

from time import time

class Timer(object):
    """
    start: Start timer. Idx can be set as timer's name.
    show: Return currend duration.
    end: Stop timer and return ended time.
        After this was called, "show" shows the ended time forever.
    """
    class SubTimer(object):
        def __init__(self):
            self.time = time()
            self.is_running = True

    def __init__(self):
        self.timer = 0
        self.timers = {}

    def start(self, idx=None):
        t = self.SubTimer()
        if idx is None:
            self.timer = t
        self.timers[idx] = t

    def __show(self, timer):
        if timer.is_running:
            return time() - timer.time
        return timer.time

    def print_time(self, t, idx=None):
        s = "%s sec" % t
        if idx is not None:
            s = str(idx) + ": " + s
        print s

    def show(self, idx=None, printing=False):
        if idx is None:
            t = self.__show(self.timer)
        else:
            t = self.__show(self.timers[idx])
        if printing:
            self.print_time(t, idx)
        return t

    def __end(self, timer):
        timer.time = self.__show(timer)
        timer.is_running = False
        return timer

    def end(self, idx=None, printing=False):
        if idx is None:
            self.__end(self.timer)
            t = self.timer.time
        else:
            self.__end(self.timers[idx])
            t = self.timers[idx].time
        if printing:
            self.print_time(t, idx)
        return t

    def print_timers(self, sep=" "):
        s = [k + sep + str(v.time) for k, v in sorted(self.timers.items())]
        print "\n".join(s)
