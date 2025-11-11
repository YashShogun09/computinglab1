import threading
import time
import os
def cpu_flood():
    while True:
        pass
def authorized_user_task():
    print("Authorized user is trying to access the resource...")
    start_time=time.time()
    for i in range(5):
        time.sleep(1)
        print(f"Authorized user accessing resource... {i+1}/5")
        end_time=time.time()
    print(f"Authorized user finished accessing resource in {end_time - start_time:.2f} seconds.")
if __name__ == "__main__":
    print("denial of service attack simulation started.")
    print("spawning CPU flood thread...")
    for i in range(5):
        t=threading.Thread(target=cpu_flood)
        t.daemon=True
        t.start()
        time.sleep(2)
        authorized_user_task()
        print("Simulation complete. Exiting.")    



