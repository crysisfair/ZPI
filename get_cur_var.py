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

print('')
print(cpu_temp)
print(cpu_use)
print(ram_total)
print(ram_used)
print(ram_free)
print(disk_total)
print(disk_used)
print(disk_perc)
