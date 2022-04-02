from parent_class import ParentClass
import dir_ops.dir_ops as do
import py_starter.py_starter as ps

class RepositoryParent( ParentClass ):

    DEFAULT_KWARGS = {
        'Dir' : None,
        'name' : None,
        'url_github' : None,
        'url_pages' : None,
        'url_clone' : None
    }

    def __init__( self, **kwargs ):

        ParentClass.__init__( self )

        joined_kwargs = ps.merge_dicts( RepositoryParent.DEFAULT_KWARGS, **kwargs )
        self.set_atts( joined_kwargs )
