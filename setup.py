#setup.py file

from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_lambdata",
    version="1.0",
    decription="A data science helper function that sums null values in a pd.DataFrame"
    url = https://github.com/TLG229/lambdata
    packages = ["my_lambdata]
)