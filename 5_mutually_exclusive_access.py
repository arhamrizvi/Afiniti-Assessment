import threading
import concurrent.futures

last_by = 0
the_count = 0
lock = False


def increment_count(by):
    global last_by
    global the_count
    global lock

    #if the function is being used
    if lock == True:
        return
    else:
        lock = True #Set lock = True to use the function
        the_count += by #add by to the_count
        last_by = by #assign by to last_by
        lock = False #put lock back to false
        return last_by, the_count


print(increment_count(5))