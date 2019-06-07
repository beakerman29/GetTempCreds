import setuptools

setuptools.setup(
    name='GoOktaBoto',
    version='0.0.7',
    packages=setuptools.find_packages(),
    url='https://github.com/beakerman29/GetTempCreds',
    license='MIT',
    author='Matthew Ramsey',
    author_email='matthew.ramsey@live.com',
    description='a package to make using the GO okta integration and python testing with boto easier',
    install_requires=[
        'keyring'
    ],
    python_requires='==3.7.*'
)
