import os

fname = "ip.txt"
fd = open(fname)

pattern = "Recieved = 3"

for ip in fd.readlines():
    status = "Down"
    outx = None
    ipx = ip.strip()
    cmd = "ping %s" %(ipx)
    fp = os.popen(cmd)
    outx = fp.read()

    if outx.find(pattern) > -1:
        status = "Up"
    print("Host %s is %s" %(ipx,status))