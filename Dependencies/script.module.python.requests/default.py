#!/usr/bin/python

import os,shutil,xbmc
import xbmcaddon,xbmcgui,xbmcplugin

addon_id = 'script.module.python.requests'
AddonID	 = 'script.module.python.requests'
ADDON	 = xbmcaddon.Addon(id=AddonID)

def RemovePythonRequestMalware():
    ############################################################################
    # do NOT use Gaia's fake 2.16(.?) version: 'script.module.python.requests' #
    # includes Gaia's Cryptocurrency-mining malware, see: 'connectionpool.py'! #
    ############################################################################
    # +fake: <import addon="script.module.python.requests" version="2.16.0" /> #
    # ...in: "system dependency" ; 'script.module.simplejson' version 3.4.1    #
    ############################################################################
    CryptoCMlwr = os.listdir(xbmc.translatePath(os.path.join('special://home/addons/')))
    addonfolder = xbmc.translatePath(os.path.join('special://home/addons/'))
    for item in CryptoCMlwr:
        if (addon_id) in item:
            print str(CryptoCMlwr)+" CryptoCMlwr="+str(item)
            xbmc.log("CryptoCMlwr="+'\''+str(item)+'\'',level=xbmc.LOGNOTICE)
            try:
                shutil.rmtree(addonfolder+item, ignore_errors=True)
            except:
                pass
            try:
                os.unlink(addonfolder+item)
            except:
                pass;
            try:
                os.rmdir(addonfolder+item)
            except:
                pass;
        else:
            pass
    xbmc.executebuiltin("Container.Refresh")
    xbmc.sleep(30)
    xbmc.executebuiltin("XBMC.ActivateWindow(home)")
    xbmc.sleep(60)
    xbmc.executebuiltin('ReloadSkin()')
    xbmc.sleep(90)
    xbmc.executebuiltin('XBMC.UpdateLocalAddons()')
    return

RemovePythonRequestMalware()
