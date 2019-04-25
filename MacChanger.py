#!/usr/bin/env python

# Usage: python MacChanger.py
import subprocess
interface = raw_input("What interface are you using? ") # pick interface found in ifconfig
new_mac = raw_input("New MAC address, ie '00:11:22:33:44:55' ") # pick desired new mac address to change to
print("[+] Changing MAC address for " + interface + " to " + new_mac + " [+]")
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

