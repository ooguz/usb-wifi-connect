#!/usr/bin/env python3

import os;
import callUSB;

def connect(ssid, passwd):
	os.system('nmcli dev wifi connect {0} password {1}'.format(ssid, passwd));

if __name__ == '__main__':

	print('please use main.py');