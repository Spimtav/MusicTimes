Earlier this evening, my lovely girlfriend asked me to burn her some CDs so she could have something to listen to while driving. The problem is that the CDs have a limited length, and any files burned after that duration are wasted/unaccessible. The solution: write python to figure out how many CDs we would need to burn given the durations of a bunch of songs! The program will output the number of CDs needed to hold all of the songs based on the input CD size, and (eventually) the sets of songs to put on each CD so you don't have to calculate it by hand.

Usage: python music_times.py [cd_length] time1, ... , timeN
Preconditions:
  cd_length is an int > 0.
  times are positive floats, where the decimal value must be < 0.60.
