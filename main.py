#!/usr/bin/env python3

import callUSB;
import connect;


if __name__ == '__main__':
	status = 0;
	while status == 0:
		if callUSB.callUSB() != 0:	
			conf = callUSB.confFile();
			connect.connect(conf[0], conf[1]);
			status = 1;
		else:
			continue;