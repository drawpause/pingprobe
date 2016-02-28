import os, subprocess, time, argparse, ipaddress

#parser = argparse.ArgumentParser(description='Description here')
#parser.add_argument('-n', '--network', dest='network', type=str, required=True,help='IP Network')

subnet = "10.0.1"
max = 255

#tissi = ipaddress.ip_network('192.168.0.0/28')

# Init the process list. To be populated later
running_processes = set()

# Go through the subnet range and create a process for each
for i in range(1,max):
    ip = subnet + "." + str(i)
    ping = ["ping", "-c", "1", ip]
    process = (subprocess.Popen(ping, stdout=open(os.devnull, 'wb')), ip)
    running_processes.add(process)    
    
# Loop until all processes are done
while running_processes:
    # Keep running through the list of processes until getting result
    for proc in running_processes:
        retcode = proc[0].poll()
        
        # Are you ready yet?
        if retcode is not None:
            # Ready, print the ip address and remove the process from the process list
            # Do not print if host unreachable
            if retcode == 0:
                print proc[1]
            running_processes.remove(proc)
            break
        else:
            # Not ready, let's wait
            time.sleep(.1)
            continue
