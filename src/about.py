# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2013 ianaré sévi <ianare@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import platform

import app
import classes
import utils
import wx
import wx.lib.buttons
import wx.lib.agw.hyperlink as hl


def create(parent):
    return About(parent)

[wxID_ABOUT, wxID_ABOUTCLOSE, wxID_ABOUTCOPYRIGHT, wxID_PANELDONATEBUTTON,
    wxID_ABOUTGREET, wxID_ABOUTVERSION, wxID_ABOUTLINK, wxID_ABOUTDONATE,
    wxID_ABOUTWXVERSION, wxID_PANELCREDITSBUTTON, wxID_PANELLICENSEBUTTON
 ] = [wx.NewId() for __init_ctrls in range(11)]


class About(wx.Dialog):
    """The about dialog."""

    def _get_wxversion(self):
        """Get the wxPython Version."""
        wxVer = ""
        for x in wx.VERSION:
            wxVer = wxVer + str(x) + "."
        wxVer = wxVer.rstrip(".")
        return wxVer
  
    def __init_sizer(self):
        bottomRow = wx.BoxSizer(wx.HORIZONTAL)
        bottomRow.Add(self.bugReport, 0, wx.ALIGN_CENTER | wx.RIGHT)

        buttonsRow = wx.BoxSizer(wx.HORIZONTAL)
        buttonsRow.Add(self.creditsButton, 0, wx.RIGHT, 15)
        buttonsRow.Add(self.licenseButton, 0)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(self.CLOSE, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        mainSizer.Add(self.greet, 0, wx.ALIGN_CENTER | wx.TOP, 5)
        mainSizer.Add(self.copyright, 0, wx.ALIGN_CENTER | wx.RIGHT | wx.LEFT, 7)
        mainSizer.Add(self.version, 0, wx.ALIGN_CENTER | wx.ALL, 2)
        mainSizer.Add(self.wxVersion, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT | wx.RIGHT, 8)
        mainSizer.Add(self.donateButton, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.TOP, 15)
        mainSizer.Add(self.link, 0, wx.ALIGN_CENTER | wx.BOTTOM, 15)
        mainSizer.Add(bottomRow, 0, wx.ALIGN_CENTER | wx.BOTTOM, 15)
        mainSizer.Add(buttonsRow, 0, wx.ALIGN_CENTER | wx.BOTTOM, 15)
        self.SetSizerAndFit(mainSizer)

    def __init_ctrls(self, parent):
        wx.Dialog.__init__(self, id=wxID_ABOUT, name=u'About', parent=parent,
                style=wx.DEFAULT_DIALOG_STYLE,
                title=_(u"About Metamorphose"))
        self.SetIcon(wx.Icon(utils.icon_path(u'about.ico'), wx.BITMAP_TYPE_ICO))

        fontParams = app.fontParams
        fontSize = fontParams['size']
        fontFamily = fontParams['family']
        fontStyle = fontParams['style']

        self.SetFont(wx.Font(fontSize + 1, fontFamily, fontStyle, wx.NORMAL, False, u'Times New Roman'))
        self.Center(wx.HORIZONTAL | wx.VERTICAL)
        self.SetThemeEnabled(True)

        self.greet = wx.StaticText(id=wxID_ABOUTGREET,
                                   label=u"Métamorphose 2", name=u'greet', parent=self)
        self.greet.SetFont(wx.Font(fontSize + 4, fontFamily, fontStyle, wx.BOLD, False))

        self.CLOSE = wx.BitmapButton(id=wxID_ABOUTCLOSE,
                                     bitmap=wx.Bitmap(utils.icon_path(u'metamorphose128.png'), wx.BITMAP_TYPE_PNG),
                                     name=u'CLOSE', parent=self, style=wx.BU_AUTODRAW)
        self.CLOSE.SetToolTipString(_(u"Click here to exit"))
        self.CLOSE.Bind(wx.EVT_BUTTON, self.on_close_button, id=wxID_ABOUTCLOSE)

        self.copyright = wx.StaticText(id=wxID_ABOUTCOPYRIGHT,
                                       label=u"Copyright © 2006-2015 Ianaré Sévi", name=u'copyright',
                                       parent=self)
        self.copyright.SetFont(wx.Font(fontSize + 2, fontFamily, fontStyle, wx.BOLD, False))

        self.version = wx.StaticText(id=wxID_ABOUTVERSION,
                                     label=_(u"Version: %s") % app.version,
                                     name=u'version', parent=self)
        self.version.SetFont(wx.Font(fontSize + 2, fontFamily, fontStyle, wx.BOLD, False))

        self.wxVersion = wx.StaticText(id=wxID_ABOUTWXVERSION,
                                       label=_(u"Using Python %s, wxPython %s") % (
                                           platform.python_version(),
                                           self._get_wxversion()
                                       ),
                                       name=u'version', parent=self)
        self.wxVersion.SetFont(wx.Font(fontSize + 1, fontFamily, fontStyle, wx.NORMAL, False))

        self.link = hl.HyperLinkCtrl(self, wxID_ABOUTLINK, _(u"Metamorphose Home Page"),
                                     URL=u'http://file-folder-ren.sourceforge.net/', style=0)

        self.bugReport = hl.HyperLinkCtrl(self, wxID_ABOUTLINK, _(u"GitHub Project Page"),
                                          URL=u'https://github.com/metamorphose/metamorphose2')
        self.bugReport.Show(True)

        self.donateButton = wx.Button(id=wxID_PANELDONATEBUTTON,
                                      label=_(u"Donate"), name=u'donateButton', parent=self)
        self.donateButton.SetFont(wx.Font(fontSize + 4, fontFamily, fontStyle, wx.BOLD, False,
                                          u'Times New Roman'))
        self.donateButton.Bind(wx.EVT_BUTTON, self.on_donate_button,
                               id=wxID_PANELDONATEBUTTON)

        self.donate = hl.HyperLinkCtrl(self, wxID_ABOUTDONATE, _(u"Donate"),
                                       URL=u'http://sourceforge.net/donate/index.php?group_id=146403')
        self.donate.Show(False)

        self.licenseButton = wx.Button(id=wxID_PANELLICENSEBUTTON,
                                       label=_(u"License"), name=u'licenseButton', parent=self)
        self.licenseButton.Bind(wx.EVT_BUTTON, self.show_small_help,id=wxID_PANELLICENSEBUTTON)

        self.creditsButton = wx.Button(id=wxID_PANELCREDITSBUTTON,
                                       label=_(u"Credits"), name=u'licenseButton', parent=self)
        self.creditsButton.Bind(wx.EVT_BUTTON, self.show_small_help,id=wxID_PANELCREDITSBUTTON)

    def __init__(self, parent):
        self.__init_ctrls(parent)
        self.__init_sizer()

    def on_close_button(self, event):
        self.Close()

    def show_small_help(self, event):
        if event.GetId() == wxID_PANELCREDITSBUTTON:
            helpFile = u'credits.html'
            title = _(u"Credits")
            icon = u'examples'
            size = wx.Size(410, 475)
        elif event.GetId() == wxID_PANELLICENSEBUTTON:
            helpFile = u'license.html'
            title = _(u"License")
            icon = u'examples'
            size = False
        return classes.SmallHelp(self, helpFile, title, icon, size).ShowModal()

    def on_donate_button(self, event):
        self.donate.GotoURL("http://sourceforge.net/donate/index.php?group_id=146403")
