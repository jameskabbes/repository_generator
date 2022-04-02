import dir_ops.dir_ops as do
import repository_generator

def run():

    calling_Dir = do.Dir( do.get_cwd() )
    print ( repository_generator.template_Dir.copy( calling_Dir ) )

if __name__ == '__main__':

    run()