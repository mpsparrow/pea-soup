# logs stuff
import datetime

mainLog = "output.txt"

# writes to log
def write(filename: str, msg: str, timestamp = True):
    log = open(f'logs/{filename}','a+')
    if timestamp:
        log.write(f"[{datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] {msg}\n")
    else:
        log.write(f"{msg}\n")
    log.close()

# wipes log
def wipe(filename: str):
    log = open(f'logs/{filename}','w+')
    log.close()

# returns log
def output(filename: str):
    with open(f'logs/{filename}') as log:
        return log.read()

# write message to main log
def log(msg: str):
    write("output.txt", msg)