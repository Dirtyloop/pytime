import time

start_time_object = time.localtime();
start_time = time.strftime("%H:%M:%S", start_time_object)

print("Time measurement started.")
user_input = input("Press enter to stop time measurement...")

current_time_object = time.localtime();
current_time = time.strftime("%H:%M:%S", current_time_object)

print("Measurement started at " + str(start_time) + " and ended at " + str(current_time))
