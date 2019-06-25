# Program klien 
# Mengirim pesan secara broadcast 
# contoh penggunaan: 
#  $ python bclient.py "checkin:1616:Tuti"
#  $ python bclient.py "checkout:1616:Tuti"

from socket import *
import sys

if len(sys.argv) < 2:
	print("Missing 1 argument message")
	sys.exit()

msg = sys.argv[1]

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
maxsize = 1024
BADDRESS = ("10.0.3.255",10000)
s.sendto(msg.encode(), BADDRESS )
s.close()