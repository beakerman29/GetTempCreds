import setuptools

setuptools.setup(
    name='GetTempCreds',
    version='0.0.1',
    packages=setuptools.find_packages(),
    url='',
    license='MIT',
    author='mramsey',
    author_email='matthew.ramsey@live.com',
    description='a package to make using the GO okta integration and python testing with boto easier',
    install_requires=[
        'keyring',
        'argparse',
    ]
)
