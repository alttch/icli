__version__ = '0.0.9'

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='icli',
    version=__version__,
    author='Altertech',
    author_email='div@altertech.com',
    description='Interactive CLI builder',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alttch/icli',
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=['argcomplete', 'readline'],
    classifiers=('Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Software Development :: User Interfaces'),
)
