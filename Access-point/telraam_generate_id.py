import argparse
import os
import subprocess

parser=argparse.ArgumentParser()
parser.add_argument('--interface', default='eth0')

args=parser.parse_args()

print('Calculating id for', args.interface)
mac_if=subprocess.run(f"cat /sys/class/net/{args.interface}/address", shell=True, stdout=subprocess.PIPE)
int_mac=int(mac_if.stdout.replace(b':',b'').strip(b'\n'), base=16)
chunks=[int(str(int_mac)[:8]), int(str(int_mac)[8:])]
replacer=[chr(c) for c in range(ord('a'), ord('z')+1)]

check_mod=''.join([replacer[ch%23] for ch in chunks])

print('telraam ID:','-'.join([str(int_mac)[i*4:i*4+4] for i in range(len(str(int_mac))//4+1)])+check_mod.upper())
print('monitor service id:',int_mac)