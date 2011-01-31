
import pygst
import gst

class Receiver:

  def __init__(self, player, out, port):

    udpsource = gst.element_factory_make("udpsrc")
    udpsource.set_property("port", port)

    rtpdepay = gst.element_factory_make("rtpjpegdepay");
    jpegdec = gst.element_factory_make("jpegdec");
    videobox = gst.element_factory_make("videobox");
    videobox.set_property("top", -200)

    yuvcap = gst.Caps("application/x-rtp,payload=96")
    yuvcapfilter = gst.element_factory_make("capsfilter");
    yuvcapfilter.set_property("caps", yuvcap)
    jpegcap = gst.Caps("image/jpeg")
    jpegcapfilter = gst.element_factory_make("capsfilter");
    jpegcapfilter.set_property("caps", jpegcap)

    player.add(udpsource, yuvcapfilter, rtpdepay, jpegcapfilter, jpegdec,
        videobox)
    gst.element_link_many(udpsource, yuvcapfilter, rtpdepay, jpegcapfilter,
        jpegdec, videobox, out)
