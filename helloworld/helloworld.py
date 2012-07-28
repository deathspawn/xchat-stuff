# helloworld.py
# https://github.com/Deathspawn/xchat-stuff/helloworld
#
#    Example layout for a python script.
#    Copyright (C) 2012  Stryker Blue // E-mail:deathspawn989@gmail.com // Website: http://deathspawn.net/
#########################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses.
########################################################################
#
# ABOUT
#
#  This implements a new idea for making python scripts (And other scripts) inside XChat.
# Configuration files are generated and put into the respective plugin folder.
# The location of the folder can be called with "command" location.
# 
# Hopefully more scripts will follow suit after this.
#
# CHANGELOG
#
# 0.1
# Released to public.
#

# Import the necessary modules.
import xchat
import os

# Set xchat plugin info.
__module_name__ = "Hello World"
__module_version__ = "0.1"
__module_description__ = "Example layout for a python script."

# Define working directory here.
hellofolder = xchat.get_info("xchatdir") + "/helloworld/"
readmefile = hellofolder+"README"
configfile = hellofolder+"helloworld.conf"

# Check to see if the folder exists.
if not os.path.exists(hellofolder):
    # Make the folder...
    os.makedirs(hellofolder)
    # Make the README...
    readmefilemake = open(readmefile, "w")
    readmelist = ["This is an example script for XChat. It implements a couple new ideas within it.\n",
    "The first idea is generating all necessary files within the script. While this method may seem a bit tedious to the scripter,\n",
    "it lets the user be able to easily load the script and get all of the necessary files on first run.\n",
    "It's simple without being simple!.\n",
    "\n",
    "The second idea is making folders within the XChat directory with the respective plugin name. An author can easily change the folder\n",
    "above and make their own files generate inside using this method. This prevents clutter in the XChat directory.\n",
    "\n",
    "This script can be kept loaded, it merely has some test commands for a general layout. You can choose to use all of it or some of it.\n",
    "I would hope that if you didn't use any of it that you would still take the idea into consideration and make your script easier to use."]
    for i in readmelist:
        readmefilemake.write(i)
    readmefilemake.close()
    # Make the config file...
    configfilemake = open(configfile, "w")
    exampleconfig = ["command = helloworld"]
    for i in exampleconfig:
        configfilemake.write(i)
    configfilemake.close()
    # Print out welcome message.
    print "=========="
    print "This is an example welcome message. It will only be shown when the configuration folder doesn't exist."
    print "This script has created a folder at "+hellofolder
    print "Inside, you will find a README (Please read, it actually is worth it.) and a simple config. The config only has one option, plenty more can be added easily."
    print " "
    print "Please report any issues at the GitHub page. See /helloworld gitinfo for git info."
    # Define this so that we have an ending ======= to make it look nice.
    firstrun = True

config = open(configfile, "r")
configlist = config.readlines()
config.close()
for i in configlist:
    if i.startswith("command") == True:
        rc = i.split(" = ")
        command = rc[1]
    else:
        pass

# The functions behind the script can go here.

# Internal commands can go here.
def commands(word, word_eol, userdata):
    try:
        # Sub commands can be defined this way. Prevents scripts from fighting over triggers.
        try:
            subcommand = word[1].lower()
        except IndexError:
            subcommand = None
        if subcommand == "help":
            print "This is an example help layout."
            print "=============================="
            print "/"+command+" help: Generates this help output."
            print "/"+command+" gitinfo: Outputs the git url. This can be changed to another source url."
            print "/"+command+" test: Outputs a test message."
        elif subcommand == "gitinfo":
            print "This script can be found at https://github.com/Deathspawn/xchat-stuff/helloworld"
        elif subcommand == "test":
            print "This is a test message. Testing 1, 2, 3."
        else:
            print "Error: please see \"/"+longcommand+" help\" for help."
        return xchat.EAT_ALL
    except IndexError:          
        pass
    return xchat.EAT_NONE

# Output an unload message.
def unload(userdata):
    print __module_name__+" "+__module_version__+" unloaded."

# Print load successful messages.
print __module_name__+" "+__module_version__+" loaded."
print "For help, see /"+command+" help. Also read the README!"
# The firstrun seperation line.
try:
    if firstrun == True:
        print "=========="
except NameError:
    pass
# All the hooks.
xchat.hook_unload(unload)
xchat.hook_command(command, commands)
