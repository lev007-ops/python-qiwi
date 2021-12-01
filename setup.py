from setuptools import setup, find_packages


with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name="python-qiwi",
    version="1.2.0",
    author="Lev",
    author_email="lev_bariakh@icloud.com",
    description="library for easy work with qiwi wallet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lev007-ops/python-qiwi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
