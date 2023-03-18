"""" import required functions """
from setuptools import setup, find_packages

# Call setup function
setup(
      author = "Mikhail Vokhmianin",
      description = "A package full of fruitfull staff",
      name = "suomi",
      version = "0.1.0",
      packages = find_packages(include=["suomi","suomi.*"]),
      install_requires = [datetime, random],
      )
