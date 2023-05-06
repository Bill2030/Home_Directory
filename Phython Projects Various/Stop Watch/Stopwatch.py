import time
while True:
    try:
        input("Press Enter to continue and press ctrl+c to exit stop watch")
        start_time = time.time()
        print("Stop watch has started")
        while True:
            print("Time elapsed:",round(time.time()-start_time,0),'secs', end='\n')
            time.sleep(1)
    except KeyboardInterrupt:
        print("Timer has stopped")


