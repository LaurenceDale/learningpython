#!/bin/bash

for ip in $(cat subnet.txt); do nmap $ip -sn | grep 10 | cut -d " " -f 5; done

#this reads a file named subnet.txt and nmap host discovers the contents. Need to create the subnet file prior to scan
