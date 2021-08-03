import time

start_time_object = time.localtime();
start_time = time.strftime("%H:%M:%S", start_time_object)

print("Time measurement started.")
user_input = input("Press any key...")

current_time_object = time.localtime();
current_time = time.strftime("%H:%M:%S", current_time_object)

print("from " + str(start_time) + " to " + str(current_time))
