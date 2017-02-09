#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #pisitools.flags.add("-pthread -I/usr/include/OpenEXR -I/usr/include/libdrm")
   # pisitools.ldflags.add("-lImath -lHalf -lIex -lIexMath -lIlmThread -lpthread")
    #shelltools.system("./bootstrap")
    autotools.configure()
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s docdir=%s examplesdir=%s" % (get.installDIR(), docdir, examplesdir))

    pisitools.dodoc("AUTHORS", "ChangeLog","NEWS", "README","LICENSE")
