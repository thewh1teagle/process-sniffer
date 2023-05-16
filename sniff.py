from scapy.all import *
from scapy.layers.inet import IP
import sys
import psutil
import contextlib
import argparse

parser = argparse.ArgumentParser(prog='Packet sniffer')
parser.add_argument('-p', type=str, required=True, help='Process name to capture')
args = parser.parse_args()
process_name: str = args.p
writer = PcapWriter(sys.stdout.buffer) # write into stdout


def get_pids(proc_name):
    pids = []
    for i in psutil.process_iter(['name', 'pid']):
        if i.name().lower() == proc_name.lower():
            pids.append(i.pid)
    return pids


def on_arrive(pkt: Packet):
    ip_layer = pkt.getlayer(IP)
    if not ip_layer:
        return
    src_port = ip_layer.sport
    dst_port = ip_layer.dport
    pids = get_pids(process_name)
    for c in psutil.net_connections(kind='inet'):
        if not c.pid in pids:
            continue
        if not len(c.raddr) or not len(c.laddr):
            continue
        if not c.raddr.port == src_port and c.laddr.port == dst_port: # compare netstat ports with packet ports
            continue
        # sys.stderr.write(c.raddr.ip)
        sys.stderr.flush()
        writer.write(pkt)
        writer.flush()
    

if __name__ == '__main__':    
    with contextlib.closing(writer): # auto close stdout writer in the end
        sniff(prn=on_arrive)
