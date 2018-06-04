import shutil, os, sys,glob
from time import sleep

dir = os.path.abspath(os.path.dirname(sys.argv[0])) # SCRIPT LOCATION
ADC = "C:\\ADC\\SOURCE\\"
counter = 0
def checkTrigger():
    global counter
    for file in glob.glob("C:\\logpoll\\*.ini"):
        if "1.ini" in file:
            cond = mov()
            if not os.path.exists(file) and  cond == True:
                shutil.move(file,"C:\\logpoll\\0.ini")
            elif cond == False:
                shutil.move(file,"C:\\logpoll\\0 - MISSING_LOG_FILES.ini")
        elif "0.ini" in file:
            print("[%s]WAITING TRIGGER" % (counter))
        elif "0 - DB_ACCESS_ERORR.ini" in file:
            print("[%s]DATABASE ACCESS ERROR" % (counter))
        elif "desktop.ini" in file:
            pass
        else:
            print("[%s]CHECK TRIGGER" % (counter))

def mov():
    if len(fn) == 2:
        print("[%s]NO LOGS FOUND" % (counter))
        return False
    else:
        os.system("C:/ADC/adc.py")
        for file in log:
                for f in fn:
                    if f in file:
                        shutil.move(file, ADC + f) ## TO SPECIFIED DIRECTORY ##
        print("FILE TRANSFERED")
        return True

while True:
    fn = os.listdir("C:\\logpoll\\")
    log = glob.glob("C:\\logpoll\\*.log")
    checkTrigger()
    counter += 1
    sleep(1)
