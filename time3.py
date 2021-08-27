import getopt, sys
from datetime import datetime

argumentList = sys.argv[1:]

options = "hse"

long_options = ["Help", "Start", "Stop"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print("Pytime Help")
            print("")
            print("-h or --Help:")
            print(" show help")
            print("")
            print("-s or --Start:")
            print(" start time measurement")
            print("")
            print("-e or --Stop:")
            print(" stop time measurement")
             
        elif currentArgument in ("-s", "--Start"):
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file = open("time2log", "w")
            file.write(str(start_time))
            file.close()
            print("Time measurement started at " + str(start_time))
             
        elif currentArgument in ("-e", "--Stop"):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file = open("time2log", "r")
            #time_from_file = datetime.fromisoformat(file.read(), "%Y-%m-%d %H:%M:%S")
            time_from_file_str = file.read()
            time_from_file = datetime.strptime(time_from_file_str, "%Y-%m-%d %H:%M:%S")
            file.close()
            print("Time measurement started at " + time_from_file_str)
            print("and stopped at " + str(current_time))
            print("after ", str(datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S") - time_from_file))
        
    if not argumentList:
        print("Pytime")
        print("")
        print("For help: -h or --Help")

except getopt.error as err:
    # output error, and return with an error code
    print (str(err))


