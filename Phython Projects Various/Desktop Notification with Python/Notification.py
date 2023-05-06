import plyer as plyer
from plyer import notification
import time
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break it has been an hour",
            timeout = 10
        )
        time.sleep(3600)



