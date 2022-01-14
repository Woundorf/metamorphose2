# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2015 ianaré sévi <ianare@gmail.com>
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

import os.path

from . import directoryTools
from .notebook import Notebook
from .operation import Operation
import utils
import wx


class OpPanel(Operation):
    """This is the main panel for directory manipulations.

    It holds the notebook holding all directory panels.
    """

    def __init_sizer(self, parent):
        #smallestSize = parent.rightSizer.GetSize() - parent.rightTopSizer.GetSize() - (10,10)
        superSizer = wx.BoxSizer(wx.VERTICAL)
        #superSizer.SetMinSize(smallestSize)
        superSizer.Add(self.notebook, 0, wx.EXPAND)
        self.SetSizerAndFit(superSizer)

    def __init_ctrls(self, prnt):
        wx.Panel.__init__(self, id=-1, name=u'Panel', parent=prnt,
                          style=wx.TAB_TRAVERSAL)
        self.notebook = Notebook(self, main)
        self.directoryToolsPanel = directoryTools.Panel(self.notebook, main)
        self.notebook.init_pages(self.directoryToolsPanel,
                                 _(u"Directory settings"), u'directory.ico')
        self.numberingPanel = self.notebook.numbering
        self.dateTimePanel = self.notebook.dateTime


    def __init__(self, parent, main_window, params={}):
        Operation.__init__(self, params)
        global main
        main = main_window
        self.set_as_path_only()
        self.__init_ctrls(parent)
        self.__init_sizer(parent)
        self.update_parameters(self.directoryToolsPanel.params)

    def on_config_load(self):
        """Update GUI elements, settings after config load."""
        self.numberingPanel.on_config_load()
        self.dateTimePanel.get_from_item_checkbox(False)

    def __add_path(self, newPath, path):
        """Extra operation for absolute paths."""
        recurPath = ''
        recur = self.directoryToolsPanel.pathRecur.GetValue()
        path = path.split(os.sep)
        # remove drive letter
        if wx.Platform == '__WXMSW__':
            path = path[1:]

        # inverse the selection or not
        if not self.directoryToolsPanel.inverse.GetValue():
            if recur <= 0:
                recur -= 1
            path = path[-recur:]
        else:
            path = path[:-recur]

        # reassemble path
        for segment in path:
            recurPath = os.path.join(recurPath, segment)
        newPath = newPath.replace(self.params['pathStructTxt'], recurPath)
        return newPath

    def __add_file_name(self, newPath, name, ext):
        if self.directoryToolsPanel.useFileExt.GetValue() and self.directoryToolsPanel.useFileName.GetValue():
            if ext:
                ext = '.' + ext
            parsedName = name + ext
        elif self.directoryToolsPanel.useFileName.GetValue():
            parsedName = name
        elif self.directoryToolsPanel.useFileExt.GetValue():
            parsedName = ext
        else:
            parsedName = ''

        newPath = newPath.replace(self.params['nameTxt'], parsedName)
        return newPath

    def reset_counter(self, c):
        """Reset the numbering counter for the operation."""
        utils.reset_counter(self, self.directoryToolsPanel, c)

    def rename_item(self, path, name, ext, original):
        """Create the new path."""
        rejoin = False
        operations = self.directoryToolsPanel.opButtonsPanel
        newPath = self.directoryToolsPanel.directoryText.GetValue()
        params = self.params

        # absolute path
        if os.path.isabs(newPath):
            split = os.path.splitdrive(newPath)
            newPath = split[1]
            rejoin = True

        # add path structure
        if params['pathStructTxt'] in newPath:
            newPath = self.__add_path(newPath, path)

        # add filename
        if params['nameTxt'] in newPath:
            newPath = self.__add_file_name(newPath, name, ext)

        newPath = operations.parse_input(newPath, original, self)

        if rejoin:
            newPath = os.path.join(split[0], newPath)
        else:
            newPath = os.path.join(path, newPath)

        return (newPath, name, ext)
