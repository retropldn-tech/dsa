'''
    You are given a class MovingAverage that receives a stream of integers. 
    Initialize the object with an integer size, representing the size of a moving window. 
    Implement the next(val) method, which accepts an integer val and returns the moving average of 
    the last size values in the stream (including the current val). If the number of elements seen so 
    far is less than size, compute the average of all elements received so far.
    Return the moving average as a floating point number after each call to next(val).
'''

from collections import deque

class MovingAverage:

    def __init__(self, size):
        self.size = size
        self._window = deque([])
        self._cur_sum = 0

    def next(self, val):
        if len(self._window) < self.size:
            self._window.append(val)
            self._cur_sum += val


        elif len(self._window) == self.size:
            left_val = self._window.popleft()
            self._cur_sum -= left_val
            self._window.append(val)
            self._cur_sum += val

        return float(self._cur_sum / len(self._window))

class Solution(MovingAverage):
    ...