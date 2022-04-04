from repository_generator.RepositoryParent import RepositoryParent


class Repository( RepositoryParent ):

    URL_BASES = {
        'github': 'https://github.com/jameskabbes',
        'pages': 'https://jameskabbes.github.io'
    }


    def __init__( self, **kwargs ):

        RepositoryParent.__init__( self, **kwargs )
        