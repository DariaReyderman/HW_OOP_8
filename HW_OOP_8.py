import threading
import time
from concurrent.futures import ThreadPoolExecutor



# Step 1
def print_sequence(name, count):
    print(f"Thread <{name}>: i=<{count}>")
    time.sleep(0.3)


if __name__ == "__main__":
    t1 = threading.Thread(target=print_sequence("Alpha", 5))
    t2 = threading.Thread(target=print_sequence("Beta", 3))
    t3 = threading.Thread(target=print_sequence("Gama", 4))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


# Step 2
def print_sequence(name, count):
    for i in range(count):
        print(f"Thread: {name}: count={i}")
        time.sleep(0.3)


if __name__ == "__main__":
    tasks = [("Alpha", 5), ("Beta", 3), ("Gamma", 4)]

    with ThreadPoolExecutor(max_workers=2) as executor:
        for name, count in tasks:
            results = [executor.submit(print_sequence, name, count)]

print("All threads completed")
