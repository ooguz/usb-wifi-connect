#!/bin/bash

echo "Dependencies installing...";
pip install urllib &> /dev/null;
pip install subprocess &> /dev/null;


echo "Installing...";
sudo mkdir /usr/share/usb-wifi-connect
sudo cp -R * /usr/share/usb-wifi-connect

echo "Installing daemon...";
sudo cp -R usb-wifi-connect /etc/init.d/usb-wifi-connect
sudo chmod a+x /etc/init.d/usb-wifi-connect

echo "Starting daemon...";
/etc/init.d/usb-wifi-connect start

echo "Installation successful!";

sudo systemctl enable usb-wifi-connect