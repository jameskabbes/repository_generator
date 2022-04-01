import py_starter as ps
import dir_ops as do
from dir_ops import Path, Dir
from parent_class import ParentClass

import os

file_Path = os.path.abspath( __file__ )
template_Dir = Dir( file_Path.ascend().join( 'Template' ) )


class Repo( ParentClass ):

    DEAFULT_KWARGS = {
    }

    FILENAMES_TO_SKIP = []

    def __init__( self, repo_Dir = None ):

        ParentClass.__init__( self )

        if repo_Dir == None:
            repo_Dir = Dir( do.get_cwd() )

        self.Dir = repo_Dir

    def generate( self ):

        template_Dir.copy( self.Dir )

