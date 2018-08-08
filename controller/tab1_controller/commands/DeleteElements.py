import controller.tab1_controller.commands as commands
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QInputDialog
from PyQt5.QtGui import QIcon, QPixmap

import model.container.createContainer as createConatiner
import model as model
import model.container.getContainer as getContainer

import os

class DeleteBookCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)

    def unexcute(self):
        print(self)

class DeleteChapterCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)

    def unexcute(self):
        print(self)

class DeletePageCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)

    def unexcute(self):
        print(self)

