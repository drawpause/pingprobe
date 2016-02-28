import os, subprocess, time, argparse, ipaddress

# Get the args
parser = argparse.ArgumentParser(description='Description here')
parser.add_argument('-n', '--network', dest='network', type=str, required=True,help='IP Network')
args = parser.parse_args()

try:
    network = ipaddress.IPv4Network(unicode(args.network))
except ValueError:
    print 'address/netmask is invalid for IPv4: ' + args.network
    exit()

# Init the process list. To be populated later
running_processes = set()

# Go through the subnet range and create a process for each
for ip in network.hosts():
    ping = ["ping", "-c", "1", str(ip)]
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
            # Not ready, move on
            continue
