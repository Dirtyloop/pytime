import datetime

start_time = datetime.datetime.now()
file = open("time2log", "w")
file.write("started "+str(start_time))
file.close()

user_input = input("Press any key to stop the counter...")

current_time = datetime.datetime.now()

print("Time from app start: " + str(current_time - start_time))