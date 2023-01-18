import repository_generator
import kabbes_client
import user_profile

class Client( repository_generator.RepositoryGenerator ):

    _BASE_DICT = {}

    def __init__( self, dict={} ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        self.Package = kabbes_client.Package( repository_generator._Dir, dict=d )
        self.cfg = self.Package.cfg

        repository_generator.RepositoryGenerator.__init__( self )
