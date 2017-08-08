# Uses Python 2.7
# Made by James Mete. Jamesmete.com, @JMete

import os
import pyHook
import pythoncom
import threading
import time
import datetime

# Requires pyHook: http://sourceforge.net/apps/mediawiki/pyhook/
# Requires pyWin32: http://sourceforge.net/projects/pywin32/


# Intro and Display the program's instructions.
print('Timestamper')
print('Made by: James Mete')
print('Jamesmete.com')
print('-----------------------')
print('Press ENTER to begin. Afterwards, press \ for Timestamps. Press ESC to quit.')
raw_input()                    # press Enter to begin
print('Started.')
startTime = time.time()    	   # get the first lap's start time
now = datetime.datetime.now()      # gets program start date for timestamp log file name
nowTime = str(now.month) + '-' + str(now.day) + '-' + str(now.year) + '---' + str(now.hour) + '-' + str(now.minute) # Saves current date and time to string
lapNum = 1                     #Sets lap number to 1. This will get incremented to index timestamps easily. 
L = [ ]                        #Creates an empty list to store timestamps

#Function to calculate the Timestamps, then writes them to a local text file.

def timelogger():
	global lapNum												 # Tells the functin it is global.
	lapTime = round(time.time() - startTime,)					 # Calculate the lap time for Timestamp.
	m, s = divmod(lapTime, 60)	
	h, m = divmod(m, 60)
	tstamp = "Timestamp #%s: %02d:%02d:%02d" % (lapNum, h, m, s) # Writes out formatted Timestamp and saves to variable.
	L.append(tstamp)											 # Appends each new Timestamp to a list.
	print("Timestamp #%s: %02d:%02d:%02d" % (lapNum, h, m, s))   # Prints out the Timestamp locally for quick reference.

	# This section creates a new txt file with the current date to save the timestamps in the Timestamps folder
	
	global nowTime
	completeName = 'Timestamps/' + nowTime + '.txt'
	fileDir = os.path.dirname(os.path.realpath('__file__'))
	filename = os.path.join(fileDir, completeName)
	fileObj = open(filename, 'w')
	for item in L:						   # Iterates through the list of Timestamps and writes them to file.
		fileObj.write(item + '\n' + '\n')  # Write them with line breaks for clarity.
	fileObj.close()                        # Close the file.
        
	lapNum += 1	 # Increases the lap number by 1. This helps act like an easy index of the Timestamps.

# Handles key listening with \ for Timestamps.
# Kills the process if ESCAPE is pressed.
class EscapeToKill(threading.Thread):
	
#Define Keyboard Event Checker
    
	def run(self):
        
		def onKeyboardEvent(event):
			asciiEscapeKey = 27 				# For ESCAPE key
			asciiKeyListen = 92 				# For \ Key
			if event.Ascii == asciiEscapeKey:   # If ESCAPE is pressed, print out a message and end process.
				print("Done. Check log file in Timestamps folder for Timestamps.")
				os._exit(0)
			elif event.Ascii == asciiKeyListen: # If \ is pressed, trigger timelogger function, and repeat.
				timelogger()
			return True
			
		# These next lines are for listening for key presses.

		hm = pyHook.HookManager()
		hm.KeyDown = onKeyboardEvent
		hm.HookKeyboard()
		pythoncom.PumpMessages()

   

if __name__ == "__main__":   
    
    
	print "Press \ key for new Timestamp. Press ESCAPE Key to Kill Process: "
	t2 = EscapeToKill()
	t2.start()
