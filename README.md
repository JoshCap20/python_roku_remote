# GUI Roku Remote with PyQt6
This program is a graphical user interface that connects with and controls your Roku.

Run with `python gui.py`.

INTRODUCTION
------------
This bot uses a Python package 'tweepy' to connect with Twitter's APIs. While this bot could be ran extremely fast by removing all sleep commands from the 'time' package, these are in place to slow down the program in order to avoid being banned from Twitter by making a large amount of follow requests to its API. Please proceed with caution changing these settings as this is what I have found to be most effective, especially when ran continously on a cloud server. This program first gathers a list of the user IDs of a given account in accounts and follows their followers by this ID.

REQUIREMENTS
------------
All requirements for this package are included in the file 'requirements.txt' in this directory.

Installation with pip. Must be in twitter_follow_bot/requirements.txt.  
`pip install -r requirements.txt`

USAGE
-------------
This file is a normal python file with minimal required packages.

Install folder into desired directory.  
`git clone https://github.com/JoshCap20/python_roku_remote.git`  
Install required dependencies using pip.  
`pip install -r requirements.txt`  
Run the file with Python.  
`python gui.py`  

That's it. Make sure to configure the program to your own Roku IP address first or the GUI won't launch. Left it this way instead of taking input for optimal usage since this magic number only needs to be configured once.


CONFIGURATION
-------------

### Roku IP Configuration:  
**required**  
Configure the IP address of your Roku in rokutest.py with your Roku's IP.   
Edit rokutest.py's value `ROKU_IP_ADDRESS`  

Help: 
The easiest way to locate this is on your Roku device. If you know the name of your Roku device on the network, you may also look it up by viewing devices connected to your network on a computer.
On your Roku device, goto Settings -> Network.
On Mac, try 'ifconfig' and 'arp -a' in a terminal shell to locate your device's name and IP address on your network.  


TROUBLESHOOTING
---------------

Try using a virtual environment to install dependencies and run the program.  

If your IP address is not valid, the GUI may not appear. Test running commands manually using functions in rokutests.py and viewing their output.
