import time

seconds=input("enter the time in number of seconds")

def countdown_timer(seconds):
    while seconds>0:

        mins=int(seconds/60)
        secs=int(seconds%60)

        timer=f'{mins}:{secs}'

        print(timer,end='\r')
        time.sleep(1)
        seconds-=1
    print("time is up")
countdown_timer(int(seconds))
