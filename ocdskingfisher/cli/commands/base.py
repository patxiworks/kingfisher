import ocdskingfisher.sources_util
import ocdskingfisher.database


class CLICommand:
    command = ''

    def __init__(self, app=None):
        self.app = app

    def configure_subparser(self, subparser):
        pass

    def run_command(self, args):
        pass

    def configure_subparser_for_selecting_existing_collection(self, subparser):
        subparser.add_argument("--databaseid", help="Database ID")
        subparser.add_argument("--run", help="source")
        subparser.add_argument("--dataversion", help="Specify a data version")
        subparser.add_argument("--sample", help="Sample source only", action="store_true")

    def run_command_for_selecting_existing_collection(self, args):

        sources = ocdskingfisher.sources_util.gather_sources()

        if args.databaseid:
            data = ocdskingfisher.database.get_collection_by_id(args.databaseid)
            if not data:
                print("We can not find the collection that you requested!")
                quit(-1)

            self.collection_instance = sources[data['source_id']](self.app.data_dir,
                                                                  remove_dir=False,
                                                                  sample=data['sample'],
                                                                  data_version=data['data_version'],
                                                                  new_version=False
                                                                  )
        else:

            sample_mode = args.sample
            data_version = args.dataversion

            if args.run not in sources:
                print("We can not find the source that you requested!")
                quit(-1)

            self.collection_instance = sources[args.run](self.app.data_dir,
                                                         remove_dir=False,
                                                         sample=sample_mode,
                                                         data_version=data_version,
                                                         new_version=False
                                                         )