import controller.tab2_controller.commands as commands
import controller.Inspectors as inspector
class SaveLabelCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)


    def unexcute(self):
        print(self)
