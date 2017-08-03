#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os


def getCpuTemp():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=", "")).replace("'C\n", "")


def getRamInfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:4])


def getCpuUse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))


def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:5])


cpu_temp = getCpuTemp()
cpu_use = getCpuUse()
ram_stat = getRamInfo()
ram_total = round(int(ram_stat[0]) / 1000, 1)
ram_used = round(int(ram_stat[1]) / 1000, 1)
ram_free = round(int(ram_stat[2]) / 1000, 1)

disk_stat = getDiskSpace()
disk_total = disk_stat[0]
disk_used = disk_stat[1]
disk_perc = disk_stat[3]

print("CPU temperature\t" + str(cpu_temp) + " C")
print("CPU usage\t" + str(cpu_use) + "%")
print("RAM total\t" + str(ram_total) + "MB")
print("RAM used\t" + str(ram_used) + "MB")
print("RAM free\t" + str(ram_free) + "MB")
print("Disk total\t" + str(disk_total))
print("Disk used\t" + str(disk_used))
print("Disk used per\t" + str(disk_perc))
input("OKay, I got it!")
