import datetime, getopt, sys

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
            start_time = datetime.datetime.now()
            file = open("time2log", "w")
            file.write("started "+str(start_time))
            file.close()
            print("Time measurement started at " + str(start_time))
             
        elif currentArgument in ("-e", "--Stop"):
            current_time = datetime.datetime.now()
            file = open("time2log", "r")
            time_from_file = file.read()
            file.close()
            print("Time measurement started at " + str(time_from_file))
            print("and stopped at " + str(current_time))
        
    if not argumentList:
        print("Pytime")
        print("")
        print("For help: -h or --Help")

except getopt.error as err:
    # output error, and return with an error code
    print (str(err))


