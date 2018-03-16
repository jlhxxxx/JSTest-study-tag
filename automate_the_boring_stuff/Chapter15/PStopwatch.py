#! python3
# PStopwatch.py - A pretty stopwatch program.

import time

# Display the program's instructions.
print('Press enter to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #' + str(lapNum).rjust(3) + ': ' + str(totalTime).rjust(6) + ' (' + str(lapTime).rjust(5) + ')')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('Done.')
