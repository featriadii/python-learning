import os

ipx = input("IP Address : ")
pattern = "Recieved = 3"

status = "Down"
cmd = "ping %s" %(ipx)
fp = os.popen(cmd)
outx = fp.read()

if outx.find(pattern) > -1:
    status = "Up"

print("Host %s is %s" %(ipx,status))