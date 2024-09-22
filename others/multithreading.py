import threading


def print_numbers():
    for i in range(1, 6):
        print(i)


def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)


# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Joining threads to wait for them to complete
thread1.join()
thread2.join()
