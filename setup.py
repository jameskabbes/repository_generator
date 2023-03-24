from setuptools import setup

if __name__ == '__main__':
    setup(
        package_data={'kabbes_repository_generator': 
            [ 
                'Templates/default/Template/.gitignore',
                'Templates/default/Template/README.md', 
                'CONFIG.json'
            ]
            }
    )