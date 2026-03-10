import os, sys, psutil

def is_already_running() -> bool:
    current_proc = os.path.basename(sys.argv[0])
    count = 0
    for process in psutil.process_iter(['name']):
        if process.info['name'] == current_proc:
            count += 1
    return count > 2