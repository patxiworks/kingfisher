import ocdskingfisher.sources_util


class CLICommand:
    command = ''

    def __init__(self, app=None):
        self.app = app

    def configure_subparser(self, subparser):
        pass

    def run_command(self, args):
        pass

    def configure_subparser_for_selecting_existing_collection(self, subparser):
        subparser.add_argument("--run", help="source")
        subparser.add_argument("--dataversion", help="Specify a data version")
        subparser.add_argument("--sample", help="Sample source only", action="store_true")

    def run_command_for_selecting_existing_collection(self, args):

        sources = ocdskingfisher.sources_util.gather_sources()

        sample_mode = args.sample
        data_version = args.dataversion

        if args.run not in sources:
            print("We can not find a source that you requested!")
            quit(-1)

        self.collection_instance = sources[args.run](self.app.data_dir,
                                                          remove_dir=False,
                                                          sample=sample_mode,
                                                          data_version=data_version,
                                                          new_version=False
                                                          )