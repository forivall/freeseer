import pygst
pygst.require("0.10")
import gst

from freeseer.framework.plugin import IVideoInput

class DesktopWinSrc(IVideoInput):
    name = "Desktop-Windows Source"
    
    def get_videoinput_bin(self):
        bin = gst.Bin(self.name)
        
        videosrc = gst.element_factory_make("dx9screencapsrc", "videosrc")
        bin.add(videosrc)
        
        # Setup ghost pad
        pad = videosrc.get_pad("src")
        ghostpad = gst.GhostPad("videosrc", pad)
        bin.add_pad(ghostpad)
        
        return bin
