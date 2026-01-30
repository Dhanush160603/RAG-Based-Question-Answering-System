import time

def start_timer():
    return time.time()

def end_timer(start_time: float) -> float:
    return round(time.time() - start_time, 3)
