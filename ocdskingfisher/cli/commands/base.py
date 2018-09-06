

class CLICommand:
    command = ''

    def __init__(self, app=None):
        self.app = app

    def configure_subparser(self, subparser):
        pass

    def run_command(self, args):
        pass
