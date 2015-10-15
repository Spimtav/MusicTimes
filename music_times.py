#music_times.py
#Maximillian Tinati
#October 14, 2015
"""Module/script to determine how many songs can fit on a cd of the
     specified length, and how many total cd's are necessary.
   Useage: python music_times.py [cd length] time1, time2, ..., timeN.i
     cd length is an int, and times are floats of MIN.SECS"""

import math
import sys


class MusicTime(object):
  """Class to represent a song duration:
       self.mins: the amt of minutes in the song; an int >= 0.
       self.secs: the amt of seconds in the song; an int >= 0 and < 60."""

  def __init__(self, mins, secs):
    assert (type(mins) == int and type(secs) == int), "Please enter integers only."
    assert (secs >= 0 and secs <= 59),"Please enter a valid seconds amount."
    assert (mins >= 0), "Please enter a nonnegative amount for minutes."
    self.mins= mins
    self.secs= secs

  def __add__(self, other):
    newMins= self.mins + other.mins
    newSecs= self.secs + other.secs
    if newSecs >= 60:
      newMins+= 1
      newSecs-= 60
    return MusicTime(newMins, newSecs)

  def __gt__(self, other):
    selfSecs= self.mins*60 + self.secs
    otherSecs= other.mins*60 + other.secs
    return selfSecs > otherSecs


def toMusic(num):
  """Returns: music object with num mins and seconds specified.
     Precondition: num is a nonnegative float with the decimal part < 60."""
  num= float(num)
  mins= int(num)
  secs= int(math.ceil((num % 1) * 100))
  if secs == 60:
    mins+= 1
    secs-= 60
  return MusicTime(mins, secs)


def numCDs(cdLength, timeObj):
  """Returns: int for the number of CDs necessary to hold all of the songs given.
     Precondition: timeObj is an object of type MusicTime. cdLength is a positive int."""
  cds= 1
  lengthTime= MusicTime(cdLength, 0)
  while timeObj > lengthTime:
    cds+= 1
    timeObj.mins-= lengthTime.mins
  return cds






if __name__ == "__main__":
  assert (len(sys.argv) >= 3), "Please enter the correct number of arguments. Useage is: python music_times.py [cd_length (int)] time1(float), ... , timeN(float)"
  assert (sys.argv[1].isdigit() and "." not in sys.argv[1] and int(sys.argv[1]) > 0), "Please enter a valid CD length."

  cdLength= int(sys.argv[1])
  timeList= sys.argv[2:]
  timeObjList= map(toMusic, timeList)
  timeSum= reduce(lambda x, y: x + y, timeObjList)
  print ""
  print "Total music duration: %i:%i" % (timeSum.mins, timeSum.secs)
  print "Number of %i minute CDs needed: %i" % (cdLength, numCDs(cdLength, timeSum))
