
class Invoker:

    def __init__(self, gui):
        self.gui = gui


    ##set commands

    def set_choose_colour_setting(self, choose_colour):
        self.choose_colour_setting = choose_colour

    def set_custom_colour_setting(self, custom_colour_setting):
        self.custom_colour_setting = custom_colour_setting

    def set_default_path_setting(self, dp):
        self.default_path_setting = dp

    def set_picture_size_setting(self,sps):
        self.picture_size_setting = sps

    def set_tracking_rate_setting(self,trs):
        self.tracking_rate_setting = trs

    def set_choose_camera_setting(self,sccs):
        self.choose_camera_setting = sccs

    def set_test_page_detection_setting(self,tpds):
        self.test_page_detection_setting = tpds

    def set_test_tracking_setting(self,tts):
        self.test_tracking_setting = tts

    ##call commands
    def choose_color(self):
        self.choose_colour_setting.execute()

    def custom_colour(self):
        self.custom_colour_setting.execute()

    def default_path(self):
        self.default_path_setting.execute()

    def picture_size(self):
        self.picture_size_setting.execute()

    def tracking_rate(self):
        self.tracking_rate_setting.execute()

    def choose_camera(self):
        self.choose_camera_setting.execute()

    def test_page_detection(self):
        self.test_page_detection_setting.execute()

    def test_tracking(self):
        self.test_tracking_setting.execute()

    """
    ##help
    def set_help(self,hh):
        self.help = hh

    def help(self,type):
        self.help.execute(type)
    """