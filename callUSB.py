#!/usr/bin/env python3

import os;
import subprocess;

def runCommand(cmd):
	subprocess.Popen(cmd, shell=True, executable='/bin/bash');

def callUSB():
	usbNo = 0;
	os.chdir('/media/{}/'.format(os.environ['USER']));
	mountPoint = os.listdir();
	for i in range(0, len(mountPoint)):		
		os.chdir('/media/' + os.environ['USER'] + '/' + mountPoint[i]);
		files = os.listdir();
		if files.count('wifi.txt') == 1:
			usbNo = i;
			usbName = os.getcwd();
			return usbName;
		else:
			i = i+1;
	return 0;

def confFile():
	if callUSB() != 0:
		os.chdir(callUSB());
		wifiConf = open('wifi.txt', 'r');
		info = wifiConf.read();
		info = info.split('\n');
		return info;
	else:
		return '\n';
if __name__ == '__main__':
	
	print(confFile());
