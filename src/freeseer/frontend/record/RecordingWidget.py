#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
freeseer - vga/presentation capture software

Copyright (C) 2011  Free and Open Source Software Learning Centre
http://fosslc.org

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For support, questions, suggestions or any other inquiries, visit:
http://wiki.github.com/fosslc/freeseer/

@author: Thanh Ha
'''

from PyQt4 import QtCore, QtGui

from freeseer.frontend.qtcommon.Resource import resource_rc

class RecordingWidget(QtGui.QWidget):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtGui.QWidget.__init__(self, parent)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/freeseer/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.resize(400, 400)
        
        self.mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.mainLayout)
        
        self.recordPushButton = QtGui.QPushButton("Record")
        self.recordPushButton.setMinimumSize(QtCore.QSize(0, 40))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/multimedia/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/multimedia/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.recordPushButton.setIcon(icon1)
        self.recordPushButton.setCheckable(True)
        self.recordPushButton.setObjectName("recordButton")
        self.mainLayout.addWidget(self.recordPushButton)
        
        # Filter bar
        self.filterBarLayout = QtGui.QVBoxLayout()
        self.mainLayout.addLayout(self.filterBarLayout)
        
        self.filterBarLayoutRow_1 = QtGui.QHBoxLayout()
        self.filterBarLayout.addLayout(self.filterBarLayoutRow_1)
        self.eventLabel = QtGui.QLabel("Event")
        self.eventLabel.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        self.eventComboBox = QtGui.QComboBox()
        self.eventLabel.setBuddy(self.eventComboBox)
        self.roomLabel = QtGui.QLabel("Room")
        self.roomLabel.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        self.roomComboBox = QtGui.QComboBox()
        self.roomLabel.setBuddy(self.roomComboBox)
        self.dateLabel = QtGui.QLabel("Date")
        self.dateLabel.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        self.dateComboBox = QtGui.QComboBox()
        self.dateLabel.setBuddy(self.dateComboBox)
        self.filterBarLayoutRow_1.addWidget(self.eventLabel)
        self.filterBarLayoutRow_1.addWidget(self.eventComboBox)
        self.filterBarLayoutRow_1.addWidget(self.roomLabel)
        self.filterBarLayoutRow_1.addWidget(self.roomComboBox)
        self.filterBarLayoutRow_1.addWidget(self.dateLabel)
        self.filterBarLayoutRow_1.addWidget(self.dateComboBox)
        
        self.filterBarLayoutRow_2 = QtGui.QHBoxLayout()
        self.filterBarLayout.addLayout(self.filterBarLayoutRow_2)
        self.talkLabel = QtGui.QLabel("Talk ")
        self.talkLabel.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        self.talkComboBox = QtGui.QComboBox()
        self.talkComboBox.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.talkComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.filterBarLayoutRow_2.addWidget(self.talkLabel)
        self.filterBarLayoutRow_2.addWidget(self.talkComboBox)
        
        # Preview Layout
        self.previewLayout = QtGui.QHBoxLayout()
        self.mainLayout.addLayout(self.previewLayout)
        
        self.previewWidget = QtGui.QWidget()
        self.audioSlider = QtGui.QSlider()
        self.audioSlider.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        self.audioSlider.setEnabled(False)
        self.previewLayout.addWidget(self.previewWidget)
        self.previewLayout.addWidget(self.audioSlider)
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    main = RecordingWidget()
    main.show()
    sys.exit(app.exec_())