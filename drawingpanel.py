import atexit
import sys
import time

# python3.0 uses "tkinter," python2.x uses "Tkinter."
# detect version info and import appropriate graphics
# code added by TA Steve Geluso
if (sys.version_info >= (3, 0)):
    from tkinter import *
else:
    from Tkinter import *

'''
A DrawingPanel object represents a simple interface for creating
graphical windows in Python.

Author : Marty Stepp (stepp AT cs.washington)
Version: 2009/10/21
'''


class DrawingPanel(Tk):
    '''
    Constructs a panel of a given width, height, and optional background color.

    Keyword arguments:
    width -- width of the DrawingPanel in pixels (default 500)
    height -- height of the DrawingPanel in pixels (default 500)
    background -- background color of the DrawingPanel (default "white")
    '''

    def __init__(self, width=500, height=500, background="white"):
        Tk.__init__(self)
        self.width = width
        self.height = height
        self.title("DrawingPanel")
        self.canvas = Canvas(self, width=width + 1, height=height + 1)
        self.canvas["bg"] = background
        self.canvas.pack({"side": "top"})
        self.wm_resizable(0, 0)
        self.update()

        # hack - runs mainloop on exit if not interactive
        if not hasattr(sys, 'ps1'):
            self.install_mainloop_hack()

    def install_mainloop_hack(self):
        # for everything but idle
        atexit.register(self.mainloop)

        # hack just for idle:
        # flush_stdout is called immediately after code execution - intercept
        # this call, and use it to call mainloop
        try:
            import idlelib.run
            def mainloop_wrap(orig_func):
                def newfunc(*a, **kw):
                    self.mainloop()
                    idlelib.run.flush_stdout = orig_func
                    return orig_func(*a, **kw)

                return newfunc

            idlelib.run.flush_stdout = mainloop_wrap(idlelib.run.flush_stdout)
        except ImportError:
            pass

    '''
    Erases all shapes from the panel and fills it with its background color.
    '''

    def clear(self):
        self.canvas.create_rectangle(0, 0, self.width + 2, self.height + 2, \
                                     outline=self.canvas["bg"], fill=self.canvas["bg"])

    '''
    Sets the panel's background color to be the given color.

    Keyword arguments:
    color -- the color to set, as a string such as "yellow" or "black"
    '''

    def set_background(self, color):
        self.canvas["bg"] = color

    '''
    Causes the DrawingPanel to pause for the given number of milliseconds.
    Useful for creating simple animations.

    Keyword arguments:
    ms -- number of milliseconds to pause
    '''

    def sleep(self, ms):
        try:
            self.update()
            time.sleep(ms / 1000.0)
            self.update()
        except Exception:
            pass