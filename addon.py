import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "Hello World!"
line2 = "I can write"
line3 = "I think i am retarded"

xbmcgui.Dialog().ok(addonname, line1, line2, line3)