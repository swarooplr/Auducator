from PyQt5 import QtCore, QtGui, QtWidgets

import controller.tab3_controller.commands as commands
import controller.tab3_controller.commands.Tracker as tracker

import controller.tab3_controller.commands.ResetUI as reset_ui
import controller.tab3_controller.commands.track as track
import controller.tab3_controller.commands.speakout as speakout
import controller.Inspectors as inspector
import model.container.getContainer as getContainer
import controller.tab3_controller.commands.Tracker as tracker
import controller.tab3_controller.commands.PlayPage as play_page




class StopPageCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        try:
            print("stopping")
            tracker.cordinates = (-1000,-1000)
            # play_page.speakout_thread.stop()
            # play_page.tracking_thread.stop()
            print(self.context.speakout_thread.isAlive())
            print(self.context.tracking_thread.isAlive())

        except Exception as e:
            print("error",e)
            pass

    def unexcute(self):
        print(self)

