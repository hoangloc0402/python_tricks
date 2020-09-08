import time


def measure_exe_time(func, *args, **kwargs):
    start_time = time.time()

    func(*args, **kwargs)

    end_time = time.time()
    execute_time = end_time - start_time
    print(f'EXECUTION TIME (second): {execute_time}')

    
def measure():
    pass
    
    
    
    
    