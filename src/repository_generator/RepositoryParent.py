from parent_class import ParentClass
import dir_ops.dir_ops as do
import py_starter.py_starter as ps

class RepositoryParent( ParentClass ):

    DEFAULT_KWARGS = {
        'Dir' : None,
    }

    def __init__( self, **kwargs ):

        ParentClass.__init__( self )

        joined_kwargs = ps.merge_dicts( RepositoryParent.DEFAULT_KWARGS, **kwargs )
        self.set_atts( joined_kwargs )

        # Set the required attributes
        assert do.Dir.is_Dir( self.Dir )
        self.name = self.Dir.dirs[-1]
        self.url_github = self.URL_BASES[ 'github' ] + '/' + self.name
        self.url_pages = self.URL_BASES[ 'pages' ] + '/' + self.name
        self.url_clone = self.url_github + '.git'

    def print_imp_atts(self, **kwargs):

        return self.print_imp_atts( atts = ['name','Dir','url_github','url_pages'], **kwargs )

    def print_one_line_atts(self, **kwargs):
         
        return self.print_one_line_atts( atts = ['Dir','name'] **kwargs )

