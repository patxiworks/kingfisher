import os
import configparser


"""This holds configuration information for Kingfisher.
Whatever tool is calling it - CLI or other code - should create one of these, set it up as required and pass it around.
"""


class App:

    def __init__(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.data_dir = os.path.join(this_dir, "..", "data")

    def load_user_config(self):
        config = configparser.ConfigParser()

        if os.path.isfile(os.path.expanduser('~/.config/ocdskingfisher/config.ini')):
            config.read(os.path.expanduser('~/.config/ocdskingfisher/config.ini'))
        elif os.path.isfile(os.path.expanduser('~/.config/ocdsdata/config.ini')):
            config.read(os.path.expanduser('~/.config/ocdsdata/config.ini'))
        else:
            return

        self.data_dir = config.get('DATA', 'DIR', fallback=self.data_dir)
