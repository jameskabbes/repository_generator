from repository_generator.RepositoryParent import RepositoryParent


class Repository( RepositoryParent ):

    URL_BASES = {
        'github': 'https://github.com/jameskabbes/',
        'pages': 'https://jameskabbes.github.io/'
    }

    def __init__( self, Dir, **kwargs ):

        name = Dir.dirs[-1]
        url_github = Repository.URL_BASES[ 'github' ] + name
        url_pages = Repository.URL_BASES[ 'pages' ] + name
        url_clone = url_github + '.git'


