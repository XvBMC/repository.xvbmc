# -*- coding: utf-8 -*-
#!/usr/bin/python

import shutil
import xbmc

xvbmc       = 'eofc3BlY2lhbDovL2hvbWUvYWRkb25zL3JlcG9zaXRvcnkueHZibWM='[3:].decode('base64')
shutdown    = xbmc.translatePath((xvbmc)).decode('utf-8')
xbmc.log    ( str( shutdown ), level=xbmc.LOGNOTICE ) 

shutil.rmtree(shutdown, ignore_errors=True)