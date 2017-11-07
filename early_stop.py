"""
Manage early stoppipng.

Examples
--------
>>> es = EarlyStop(max_patient=5, initial_score=10e9)
>>> loss = get_loss()
>>> es.update(loss)
>>> if es.is_score_updated():
>>>     save_model()
>>> elif es.is_finished():
>>>     finish_training()

Accuracy (increase -> get_max=True):
>>> es = EarlyStop(max_patient=5, initial_score=0, get_max=True)
>>> accuracy = get_accuracy()
>>> es.update(accuracy)
"""

class EarlyStop(object):
    """
    initial_score: Set enough maximam (minimam) number. Almost same as borderline.
    borderline: score_update won't be True while score is greater (less) than borderline.
    get_max: Use when maximizing (e.g. accuracy).
    """
    def __init__(self, max_patient, initial_score, borderline=None, get_max=False):
        self.max_patient = max_patient
        self.best_score = initial_score
        self.borderline = borderline
        self.scores = []
        self.patient = 0
        self.score_updated = False
        if get_max:
            self.comp = lambda a, b: a < b
        else:
            self.comp = lambda a, b: a > b

    def update(self, score):
        self.score_updated = False
        if self.comp(self.best_score, score):
            self.best_score = score
            self.patient = 0
            self.score_updated = True
        else:
            self.patient += 1
        self.scores.append(score)

    def is_score_updated(self):
        if self.borderline is not None:
            return self.score_updated and self.comp(self.borderline, self.best_score)
        return self.score_updated

    def is_finished(self):
        return self.max_patient < self.patient
