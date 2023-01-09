import repository_generator
import kabbes_user_client
import py_starter as ps

class Client( repository_generator.RepositoryGenerator ):

    BASE_CONFIG_DICT = {
        "_Dir": repository_generator._Dir,
    }

    def __init__( self, dict={}, **kwargs ):

        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        self.cfg = kabbes_user_client.Client( dict=dict, **kwargs ).cfg
        repository_generator.RepositoryGenerator.__init__( self )
