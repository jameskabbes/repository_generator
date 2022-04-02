from .RepositoryParent import RepositoryParent
from .repository_generator import run


import dir_ops.dir_ops as do
import os

Dir = do.Path( os.path.abspath( __file__ ) ).ascend()   #Dir that contains the package 
src_Dir = Dir.ascend()                                  #src Dir that is one above
repo_Dir = src_Dir.ascend()                    
templates_Dir = do.Dir( Dir.join( 'Templates' ) )

