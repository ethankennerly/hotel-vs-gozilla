Hotel vs Gozilla

This is an animated adaptation of the ancient Chinese game of Go.
I hope to teach videogamers the rules and tactics of my favorite boardgame.
This my personal experiment with several new game mechanics and UI:

 * Bonuses for combo moves.
 * Animations of risk and reward.
 * Animated groups and fights.
 * Single-player levels 1 to 30.
 * Multiplayer from 5x5 to 9x9.

License

You are free to copy and modify my code.
Except you are not free to copy files that are authored made by others 
(the included decorator.py, GnuGo, pindent.py, PyAMF, sgflib.py, typelib.py, t.as) 
unless their licenses say you can.

Please credit Ethan Kennerly as the author of my modules.
If you host a server, I hope you invite me to play:
kennerly at finegamedesign dot com



Install the server

Install the networking engine:
Python 2.5
Twisted 9 for Python 2.5
Twisted-9.0.0.win32-py2.5.exe

See that the client-server messaging framework is included:
PyAMF 0.4 for Python 2.5.
(Copies of these files are already included)

See that the Go bot is included:
GnuGo 3.8
gnugo3.8.exe
(A copy of this file is already included)

Flash will not let you connect the client to the server on your machine.
Edit Flash security settings to allow connection to your installation directory.

Trust the directory of the server.
http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager04.html
Add location:
Your server location.  Example:
C:\archive\hotel-vs-gozilla

Otherwise the client will receive an error:
securityErrorHandler: Error #2048
Connecting to socket server on localhost:5900

Run the server:

python embassy.py

Run the client, which uses Flash 9 or higher:

lifeanddeath.swf


If you run the server remotely (not localhost):

Open the port at the firewall:

# /sbin/iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 5900 -j ACCEPT
# service iptables save

are you listening to port 5900?

# netstat -nat | grep LISTEN

Use at your own risk.  Advice from:
http://www.cyberciti.biz/faq/linux-unix-open-ports/


Software development kit

While building this experimental software, I lightly applied a philosophy of:

 * Design by example
     * Agile test-driven development.
     * Hundreds of automatically tested examples from real players.
     * Server records sessions to files, formatted as automated tests.
     * High-level automated sessions replay games and user clickthroughs.
     * Low-level functional unit tests.
     * Easy decomposition from high-level to low-level.
     * Live coding, also known as runtime programming to explore live games.

To reprogram the server, and script the client during runtime, install PythonCard 0.8, and run code_explorer.py.

Many of the files contain extensive tests, which will verify the module is working correctly.  If no errors are reported, then it is error-free.

The server and client share the same model, and some of the same code.  There is a partial Python to ActionScript converter, which makes this more convenient.

Credits

Except for the included decorator.py, GnuGo, pindent.py, PyAMF, sgflib.py, typelib.py, t.as ...
I made this experimental game.
I had a lot of feedback from several players, who are credited in the code.
When I edited some code based on a player's experience, I wrote their names in the code.

Enjoy!

-- Ethan Kennerly
kennerly at finegamedesign dot com

