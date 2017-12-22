#!/usr/bin/env python3

import callUSB;

import os;
import urllib.request;

def connect(ssid, passwd):
	os.system('nmcli dev wifi connect {0} password {1}'.format(ssid, passwd));

def check():
    try:
        urllib.request.urlopen('http://www.ozcanoguz.com', timeout=1);
        return True;
    except urllib.request.URLError:
        return False;

if __name__ == '__main__':

	print('please use main.py');