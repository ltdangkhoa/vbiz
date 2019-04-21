"""setup.py"""
import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='vbiz',
    version='0.0.1',
    author='Kris Luu',
    author_email='luuthaidangkhoa@gmail.com',
    description='The vbiz fetcher',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='http://github.com/ltdangkhoa/vbiz',
    packages=setuptools.find_packages(),
    install_requires=[
        'pdfminer.six',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['vbiz=vbiz.command_line:main'],
    })