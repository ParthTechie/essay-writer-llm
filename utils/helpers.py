import time

def timed_execution(func, *args, **kwargs):
    """Utility function to time how long a function takes to execute"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    
    execution_time = end_time - start_time
    return result, execution_time