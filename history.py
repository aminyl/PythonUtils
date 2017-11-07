"""
Hold histories.
Examples
--------
>>> hist = History()
>>> hist.push({"loss":0.1, "accuracy":0.5})
"""

class History(object):
    def __init__(self, name="hist"):
        self.hist = {}
        self.name = name
        self.debug_print = True

    def push(self, res, ignore_none=True):
        for k, v in res.items():
            if (v is not None and ignore_none) or not ignore_none:
                if k in self.hist:
                    self.hist[k].append(v)
                else:
                    self.hist[k] = [v]

    def save(self):
        np.save(self.name, self.hist)
        if debug_print:
            print "saved: " + self.name + ".npy"
