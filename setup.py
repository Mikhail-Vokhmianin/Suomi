""" import required functions """
from setuptools import setup, find_packages

# Call setup function
setup(
    author="Mikhail Vokhmianin",
    description="A package full of fruitful stuff",
    name="suomi",
    version="0.1.1",
    packages=find_packages(include=["suomi", "suomi.*"]),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 0 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Free',
        'Natural Language :: English',
        'Programming language :: Python :: 3.10'
    ]
)
