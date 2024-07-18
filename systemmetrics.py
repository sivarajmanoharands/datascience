# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:33:31 2023

@author: user
"""

import psutil
import platform
from datetime import datetime
from tabulate import tabulate
import time
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"(bytes:.2f) (unit)(suffix)"
        bytes /= factor
        
        
#Collect system information
uname = platform.uname()
boot_time_timestamp = psutil.boot_time()
cpufreq = psutil.cpu_freq()
cpus = psutil.cpu_percent(percpu=True, interval=1)
sumem = psutil.virtual_memory()
swap = psutil.swap_memory()
partitions = psutil.disk_partitions()
disk_io = psutil.disk_io_counters()
if_addrs = psutil.net_if_addrs()
net_io = psutil.net_io_counters()
#Create tables for each resource
system_info = [
    ["System", uname.system],
    ["Node Name", uname.node],
    ["Release", uname.release],
    ["Version", uname.version],
    ["Machine", uname.machine],
    ["Processor", uname.processor],
]
boot_time_info = [
    ["Boot Time", datetime.fromtimestamp(boot_time_timestamp)],
]
cpu_info = [
    ["Physical cores", psutil.cpu_count(logical=False)],
    ["Total cores", psutil.cpu_count(logical=True)],
    ["Max Frequency (Mhz)", f"(cpufreq.max:.2f)"],
    ["Min Frequency (Mhz)", f"(cpufreq.min:.2f)"],
    ["Current Frequency (Mhz)", f"(cpufreq.current:.2f)"],
]
memory_info = [
    ["Total Memory", get_size(sumem.total)],
    ["Available Memory", get_size(sumem.available)],
    ["Total SWAP", get_size(swap.total)],
]
disk_info = []
for partition in partitions:
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    disk_info.append([
    f"Device: {partition.device}",
    f"Mountpoint: {partition.mountpoint}",
    f"File system type: {partition.fstype}",
    f"Total Size", get_size(partition_usage.total),
    f"Used", get_size(partition_usage.used),
    f"Free", get_size(partition_usage.free),
    f"Percentage", f"{partition_usage.percent}%",])
network_info = [] 
for interface_name, interface_addresses in if_addrs.items(): 
    for address in interface_addresses: 
        if str(address.family) == 'AddressFamily.AF_INET': 
            network_info.append([
            f"Interface: {interface_name}",
            f"IP Address: {address.address}",
            f"Netmask: {address.netmask}",
            f"Broadcast IP: {address.broadcast}",
        ])
        elif str(address.family) == 'AddressFamily.AF_PACKET': 
            network_info.append([
            f"Interface: {interface_name}",
            f"MAC Address: {address.address}",
            f"Netmask: {address.netmask}",
            f"Broadcast MAC: {address.broadcast}",
        ])
# Define a tabular format
system_table = tabulate(system_info, tablefmt="grid")
boot_time_table = tabulate(boot_time_info, tablefmt="grid")
cpu_table = tabulate(cpu_info, tablefmt="grid")
memory_table = tabulate(memory_info, tablefmt="grid")
disk_table=tabulate(disk_info, headers=["Disk Info"], tablefmt="grid") 
network_table = tabulate(network_info, headers=["Network Info"], tablefmt="grid")
# Print the tabulated output print("System Information:") print(system_table)

current_time = time.time()
difference = current_time - boot_time_timestamp
days = difference/(60*60)
months = days // 30
years = months // 12
hours = days/(60)
timestamp = f"{years} years, {months % 12} months, {days % 30} days,{hours%24} hours"

print("\nBoot Time:") 
print(boot_time_table)
print("\nCPU Information:") 
print(cpu_table)
print("\nMemory Information:") 
print(memory_table)
print("\nDisk Information:") 
print(disk_table)
print("\nNetwork Information:") 
print(network_table)
print("Total Active hours")
print(timestamp)

