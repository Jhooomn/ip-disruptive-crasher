import socket
import subprocess
import threading

def current():
    try:    
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        bash_command = "explorer ."
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        bash_command = "ping " + local_ip
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)

        output, error = process.communicate()

        while error != None or error != "":
            t = threading.Thread(target=current)
            t.start()
            print(f'Active Threads: {threading.active_count()}')
            t.join()
    except Exception:
        print("There was an unexpected error.")

current()