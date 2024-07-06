from setuptools import setup, find_packages

setup(
    name='AlgoPy',  # Name of your library
    version='0.1.0',  # Initial version (e.g., 0.1.0)
    description='A brief description of MyLibrary.',  # Short description of your library
    long_description=open('README.md').read(),  # Long description from README.md
    url='https://github.com/DefinetlyNotAI/AlgoPy',  # URL of your library's homepage
    author='Shahm Najeeb',  # Author's name
    author_email='Nirt_12023@outlook.com',  # Author's email
    license='MIT',  # License of your library
    packages=find_packages(),  # Automatically discover all packages and subpackages
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['logging', 'sorting', 'searching'],  # Keywords that describe your library
    install_requires=[  # List of dependencies
        'datetime',
        'os',
    ],
    extras_require={  # Optional dependencies
        'dev': ['check-manifest'],
    },
    zip_safe=False,
)
