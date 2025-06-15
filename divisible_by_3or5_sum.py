import os #to clear the screen
import platform  #to figure which OS user is using to run the correct clear screen command
import time  #to show how long the calculation took
import math #to do rounding for progress bar
from datetime import datetime #to make the time readable

#set up variables
objective = 10000 #how many digits you want to evaluate
system_name = platform.system() #to run the correct clear screen command
count = 0
progress = 0
answer = 0
summed_digits = 0
start_time = time.time()
end_time = 0
elapsed_time = 0

#set up proper time recording

def format_time(seconds):
    hours = seconds // 3600  # Get full hours
    minutes = (seconds % 3600) // 60  # Get remaining minutes
    remaining_seconds = round((seconds % 60),2)  # Get remaining seconds
    return f"{hours} hours {minutes} minutes {remaining_seconds} seconds"


good_start_time = datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")
print("starting loop at " + str(good_start_time))

#main loop
while count < objective:
    #set up progress bar
    if count <= 0:
        progress = 1
    else:
        progress = math.floor((count / objective) * 100) 
        print ("Progress: [" + str("|")*progress + str(" ")*(100 - progress) + "] " + str(progress) + "% complete")

    #the rest
    print ("evaluating " + str("{:,}".format(count)))
    if count % 3 == 0 or count % 5 == 0:
        print ("adding " + str("{:,}".format(count)))  
        answer += count
        count += 1 
        summed_digits += 1
    else:
        print ("not adding " + str("{:,}".format(count)))
        count += 1 


end_time = time.time()
good_end_time = datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
elapsed_time = end_time - start_time

#elapsed_time = round(((end_time - start_time) / 60),2)
print("")
print ("Progress: [" + str("|")*100 + "] 100 % complete")
print ("Completed at: " + str(good_end_time))
print ("Elapsed time: " + str(format_time(elapsed_time)))
print ("Total Digits Summed: " + str("{:,}".format(summed_digits)))
print("The answer is: " + str("{:,}".format(answer)))

