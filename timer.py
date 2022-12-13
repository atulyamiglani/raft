# represents a timer that operates for a determined interval.
import time


class Timer:
    def __init__(self, duration: float):
        # print("TIMER INITED")
        self.start_time = time.time()
        self.duration = duration

    # determines if the timer has been done.
    def is_done(self) -> bool:
        # print("IS DONE", time.time(), self.start_time +
        #       self.duration, self.duration)
        return time.time() >= self.start_time + self.duration


class Stopwatch:
    def __init__(self):
        self.start_time = time.time()

    def time_elapsed(self) -> float:
        return time.time() - self.start_time
