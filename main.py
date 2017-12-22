#!/usr/bin/env python3

import callUSB;
import connect;

import os, sys;

def main():
	while True:
		if connect.check() == False:
			if callUSB.callUSB() != 0:	
				conf = callUSB.confFile();
				connect.connect(conf[0], conf[1]);
				print("Connected.");
			else:
				pass;
		else:
			print("connected already.");

if __name__ == '__main__':
	main();