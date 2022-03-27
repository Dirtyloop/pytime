import getopt, sys
from datetime import datetime

def show_help():
    print("")
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
    print("")

def timer_start():
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    writeFile(start_time)
    print("")
    print("Time measurement started at " + str(start_time))
    print("")

def timer_stop():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fileCheck("time3log")
    time_from_file_str = readFile("time3log")
    time_from_file = datetime.strptime(time_from_file_str, "%Y-%m-%d %H:%M:%S")
    print("")
    print("Time measurement started at " + time_from_file_str)
    print("and stopped at " + str(current_time))
    print("after ", str(datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S") - time_from_file))
    print("")

def fileCheck(logFile):
    try:
      open(logFile, "r")
    except IOError:
      sys.exit("Error: First you should start the counter.")

def writeFile(start_time):
    file = open("time3log", "w")
    file.write(str(start_time))
    file.close()

def readFile(logFile):
    file = open(logFile, "r")
    time_from_file_str = file.read()
    file.close()
    return time_from_file_str

def main():
    argumentList = sys.argv[1:]

    options = "hse"

    long_options = ["Help", "Start", "Stop"]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
     
        # checking each argument
        for currentArgument, currentValue in arguments:
 
            if currentArgument in ("-h", "--Help"):
                show_help()
             
            elif currentArgument in ("-s", "--Start"):
                timer_start()
             
            elif currentArgument in ("-e", "--Stop"):
                timer_stop()
        
        if not argumentList:
            print("")
            print("Pytime")
            print("")
            print("For help: -h or --Help")
            print("")

    except getopt.error as err:
        print (str(err))
  
main()




