from setuptools import setup, find_packages

setup(
    name='Mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='python package example',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/ngezler/Mypackage',
    author='Mongezi',
    author_email='xhalanga2@gmail.com'
)