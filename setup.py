from setuptools import setup, find_packages

setup(
    name='algopy',
    version='2.0.0',
    packages=find_packages(),
    install_requires=[
        "colorlog~=6.8.2"
        "DateTime~=5.5"
        "setuptools~=73.0.0"
    ],
    test_suite='tests',
    author='Shahm Najeeb',
    author_email='Nirt_12023@outlook.com',
    description='A library for many different algorithms and other utilities',
    url='https://github.com/DefinetlyNotAI/AlgoPy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
