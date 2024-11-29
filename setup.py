from os import path
from setuptools import setup

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "description.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="whatsapp-flows",
    version="0.1.0",
    description="Opensource python wrapper for Meta Whatsapp Flows Cloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/misingo255/whatsapp-flows",
    download_url="https://github.com/Neurotech-HQ/sarufi-python-sdk/archive/refs/tags/v0.0.2.tar.gz",
    author="Wilbert Misingo",
    author_email="wilbertmisingo@gmail.com",
    license="Apache",
    packages=[""],
    install_requires=["requests"],
    keywords=[
        "Whatsapp",
        "Whatsapp Flows",
        "Whatsapp API",
        "Whatsapp Python",
        "Whatsapp Python API",
        "Whatsapp Flows Python API",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
