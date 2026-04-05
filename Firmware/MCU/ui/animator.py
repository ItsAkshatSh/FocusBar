import math

def _ease_out_cubic(t):
    return 1.0 - (1.0 - t) ** 3

def _ease_in_cubic(t):
    return 4*t*3 if t < 0.5 else 1 - (-2*t+2)**3/2

def _ease_out_back(t):
    c1, c3 = 1.70, 2.70
    return 1 + c3*(t-1)**3 + c1*(t-1)**2

EASINGS = {
    "ease_out": _ease_out_cubic,
    "ease_in": _ease_in_cubic,
    "ease_out_back": _ease_out_back
}

class AnimatedValue:
    def __init__(self, initial=0.0):
        self._v = self._start = self._target = float(initial)
        self._dur = self.elapsed = 0.0
        self._ease = _ease_out_cubic
        self.done = True