import datetime

start_time = datetime.datetime.now()
file = open("time2log", "w")
file.write("started "+str(start_time))
file.close()

print("Time measurement started.")
user_input = input("Press enter to stop the counter...")

current_time = datetime.datetime.now()

print("Time from app start: " + str(current_time - start_time))