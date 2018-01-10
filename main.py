#!/usr/bin/env python3

import callUSB;
import connect;
from time import sleep as wait;

import os, sys;

def main():
	while True:
		wait(5);
		if connect.check() == False:
			if callUSB.callUSB() != 0:	
				wait(10);
				conf = callUSB.confFile();
				connect.connect(conf[0], conf[1]);
#				print("Connected.");
				wait(30);
			else:
				pass;
		else:
#			print("connected already.");

if __name__ == '__main__':
	main();
