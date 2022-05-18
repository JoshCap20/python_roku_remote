# GUI Roku Remote with PyQt6
This program is a graphical user interface that connects with and controls your Roku. The interface is completely customizable to your preferences. I leave included sample buttons that demonstrate the ability to automate tasks.

Run with `python gui.py`.

INTRODUCTION
------------

REQUIREMENTS
------------
All requirements for this package are included in the file 'requirements.txt.'

Installation with pip. Must be in /python_roku_remote/    
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
**Required**  
  
Configure the IP address of your Roku in rokutest.py with your Roku's IP.   
Edit rokutest.py's value `ROKU_IP_ADDRESS`  
  
Help:  
The easiest way to locate this is on your Roku device. If you know the name of your Roku device on the network, you may also look it up by viewing devices connected to your network on a computer.  
On your Roku device, navigate to Settings -> Networking -> About. The IP address assigned to the Roku should be displayed underneath the network name. If you have the Roku app, you can also access this by tapping the gear icon and then viewing 'System Info.'   
On Mac, try 'ifconfig' and 'arp -a' in a terminal shell to locate your device's name and IP address on your network.  

SUGGESTIONS
---------------
I suggest using pyinstaller to install this python program as a stand-alone, executable app on your desktop for easiest usage. I would publish the app this way, but I figured it was better to publish the python file to allow customization and improvement.    
  
Install pyinstaller with Pip:  
’pip install pyinstaller’  
  
Run pyinstaller:  
For singe-file executable with hidden console:  
’pyinstaller --onefile --windowed gui.py’  
For simple use:  
’pyinstaller gui.py’  



TROUBLESHOOTING
---------------

Try using a virtual environment to install dependencies and run the program.  

If your IP address is not valid, the GUI may not appear. Test running commands manually using functions in rokutests.py and viewing their output.
