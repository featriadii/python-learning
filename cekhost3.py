import os

fname = "ip.txt"
fd = open(fname)

fname2 = "host.csv"
fd2 = open(fname2, "a")

pattern = "Recieved = 3"

for ip in fd.readlines():
    status = "down"
    outx = None
    ipx = ip.strip()

    cmd = "ping %s" %(ipx)
    fp = os.popen(cmd)
    outx = fp.read()

    if outx.find(pattern) > -1 :
        status = "Up"
    
    cmd2 = "date +'%F %X'"    
    fp1 = os.popen(cmd2)
    outx2 = fp1.read()
    outx2 = outx2.strip()
    
    print("Host %s is %s" %(ipx, status))
    fd1.write("%s;%s;%s\n" %(outx2, ipx, status))