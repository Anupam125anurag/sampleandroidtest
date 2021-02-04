import os
import time


# path for the adb.
#path = "D:\SDK\platform-tools"

# checking for connected devices
device = os.popen("adb devices").read()
print(device)

# connect to the selected device 172.0.0.1:62001
#print("Waiting for connection ...")
connect = os.popen("adb connect "+device).read()
#print(connect)

# gradle build apk
os.system("gradlew installDebug ")

#installing apk
#os.system("adb install F://TrainTicketing1//app//build//outputs//apk//debug//app-debug.apk")

#testing and collecting logcat
print("Monkey is testing the app...")
os.system("adb shell monkey -v --throttle 100 -p com.example.anupamanurag.trainticketing1 1000 > test11log.txt")
time.sleep((1000*100)/1000)

#kernel log
os.popen("adb shell dmesg >kernel3log.txt")

mydir = "F:\Mytcs1"
for subdir,dirs,files in os.walk(mydir):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".txt"):
            if filename=="kernel3log.txt":
                file=open(filepath,'r').read().splitlines()
                for elements in range(0,len(file)):
                    if "Wakeup pending" in file[elements]:
                       print(file[elements])
                       print(file[elements+1])
                       print(file[elements+2])
            elif filename=="test11log.txt":
                file=open(filepath,'r').read().splitlines()
                for elements in range(0,len(file)):
                    if "Caused by" in file[elements]:
                       print(file[elements])
                       print(file[elements+1])
                       print(file[elements+2])
