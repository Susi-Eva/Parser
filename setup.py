import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='Parser',  
     version='0.1',
     scripts=['Parser'] ,
     author="Susi Eva",
     author_email="susipurba2@gmail.com",
     description="Parsing PR, Issue, Commit, and LOC data from GitHub REST API",
     long_description=README,
     url="https://github.com/Susi-Eva/Parsing-API",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )