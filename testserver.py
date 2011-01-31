#!/usr/bin/env python2

import pygst
import gst
from Receiver import Receiver

if __name__ == "__main__":

  player = gst.Pipeline("rtpserver")

  videosink = gst.element_factory_make("sdlvideosink")
  mixer = gst.element_factory_make("videomixer")
  player.add(mixer, videosink)

  r1 = Receiver(player, mixer, 5001)
  mixer.link(videosink)


  player.set_state(gst.STATE_PLAYING)

  while True:
    pass

