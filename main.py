#!/usr/bin/env python3

import callUSB;
import connect;


if __name__ == '__main__':
	conf = callUSB.confFile();
	connect.connect(conf[0], conf[1]);