from scapy.all import *
from datetime import datetime
import time
import datetime
import sys

############# MODIFY THIS PART IF NECESSARY ###############
interface = 'enp0s3'
filter_bpf = 'udp and port 53'

# ------ SELECT/FILTER MSGS
def select_DNS(pkt):
    pkt_time = pkt.sprintf('%sent.time%')
# ------ SELECT/FILTER DNS MSGS
    try:
        if DNSQR in pkt and pkt.dport == 53:
            print(pkt[DNSQR].qname.decode())
            print (f'Detected DNS QR Message at: {pkt_time} and ip')
           # 
        # elif DNSRR in pkt and pkt.sport == 53:
        # # responses
        #     print (f'Detected DNS QR Message at: {pkt_time} and ip')
        #     print(pkt[DNSQR].qname)
 # 
    except:
        pass
# ------ START SNIFFER 
sniff(iface=interface, filter=filter_bpf, store=0, prn=select_DNS)