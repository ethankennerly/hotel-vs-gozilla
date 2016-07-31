hotel-vs-gozilla
================

Animated adaptation of the Chinese Game of Go with a Flash client and a Python server.

Play:  <http://finegamedesign.com/hotel-vs-gozilla>



Install the server
==================

Install the networking engine:
Twisted 9 for Python 2.5
Twisted-9.0.0.win32-py2.5.exe

Install the Go bot:
GnuGo 3.8
gnugo3.8.exe

Install the client-server messaging framework:
PyAMF

Edit Flash security settings to allow connection.

Trust the directory of the server.
<http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager04.html>
Add location:
Your server location.  Example:
C:\archive\hotel-vs-gozilla

securityErrorHandler: Error #2048
Connecting to socket server on localhost:5900
log



Run the server
==============

The crontab file has a crude example of running this on a dedicated Unix server.

	crontab

Running to restart the server:

	bash restart.sh

After the go bot has started and the server is listening to traffic, then the client may connect.

Example of client file is:

	index.html
	lifeanddeath.swf

The client connects to IP address.

To edit the IP address, open lifeanddeath.fla in Adobe Flash.  
This file was made in Flash CS4.  
The IP address is in the configurations page.



If you want to improve or extend anything, be my guest.
