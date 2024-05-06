from setuptools import setup, find_packages

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="databricks_filesystem",
    version="0.0.3",
    description="Databricks Utils does not support few crucial file system operations like recursive directory listing, pattern-matching for files, listing only directories or files, and more. This package provides seamless execution of these tasks.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Rahul Madhani",
    author_email="madhani.rahul@gmail.com",
    packages=find_packages(),
    url="https://medium.com/data-engineer-things/finally-in-databricks-we-can-now-perform-recursive-directory-listing-and-many-more-operations-c5f32aad78e7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Documentation": "https://medium.com/data-engineer-things/finally-in-databricks-we-can-now-perform-recursive-directory-listing-and-many-more-operations-c5f32aad78e7",
        "Source": "https://github.com/madhanir/databricks_filesystem",
    },
)
