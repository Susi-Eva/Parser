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
     long_description=long_description,
     long_description_content_type= "text/markdown",
     url="https://github.com/Susi-Eva/Parser",
     packages=setuptools.find_packages(),
     include_package_data = True,
     install_requires = [
                        "request", 
                        "math",
                        "pandas",
                        "json",
                        "operator",],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )