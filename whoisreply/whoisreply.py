# whoisreply.py
# https://github.com/Deathspawn/xchat-stuff/whoisreply
#
#    Replies back with a random phrase when someone does a /whois on you.
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
# This script has been tested with XChat 2.8.8 and Inspircd 2.5.
#### This only works if you are an oper with the +W usermode. (/mode <yournick> +W)
#
# CHANGELOG
#
# 0.1
# Initial version. Made for personal use.
#
# 1.0
# Just spiffed up the script to make it easier to config.
# Made the reply selection all one line for sanity sake.
#
# 1.0.1
# Fixed a little bug that would not parse both tags if you used different ones.
#
#TODO: Make config file.

# import the necessary modules.
import xchat
import random

# set xchat plugin info.
__module_name__ = "Whois Reply" 
__module_version__ = "1.0.1" 
__module_description__ = "Replies with random replies to /whois."

#This only works on Inspircd for now.

##########
# Config #
##########
#
# You can use tags in the replies. Enclose them with 2 ~.
# Example: ~nickname~
# Will insert their nickname into the reply.
#
# Tags:
# ~nickname~ = Nickname of the person who did the /whois.
# ~mynick~ = Your nick... not mine. :P
#
# Replies should be seperated by commas and enclosed in quotes. Also keep the outer brackets.
# Example: ["This is reply number 1", "This is reply number 2", "And so on...", "And so on..."]
replies = ["I am ~mynick~, what more do you need to know, stalker.", "Will you please stop hitting the big red button?!"]

def whois(word, word_eol, userdata):
     try:
          if word[6] == "did" and word[7] == "a" and word[8] == "/whois": 
               nick = word[4]
               mynick = word[2]
               replynumber = random.randint(1,8)
               randomreply = random.choice(replies)
               # Replace tags with the appropriate info...
               if randomreply.find("~mynick~") != -1:
                    randomreply2 = randomreply.replace("~mynick~", mynick)
               else:
                    randomreply2 = randomreply
               if randomreply2.find("~nickname~") != -1:
                    randomreply3 = randomreply2.replace("~nickname~", nick)
               else:
                    randomreply3 = randomreply2
               xchat.command("NOTICE "+nick+" "+randomreply3)
          else:
               pass
     except IndexError:
          pass
     return xchat.EAT_NONE

def unload(userdata):
     print __module_name__+" "+__module_version__+" unloaded."

print __module_name__+" "+__module_version__+" loaded."
xchat.hook_unload(unload)
xchat.hook_server("NOTICE", whois)