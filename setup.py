from setuptools import setup, find_packages

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="databricks_filesystem",
    version="0.0.1",
    description="Databricks Utils does not support few crucial file system operations like recursive directory listing, pattern-matching for files, listing only directories or files, and more. This package provides seamless execution of these tasks.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Rahul Madhani",
    author_email="madhani.rahul@gmail.com",
    packages=find_packages(),
)
