#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages


# Long list of classifiers
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Information Technology",
	"Intended Audience :: Science/Research",
	"Intended Audience :: System Administrators",
    "Operating System :: OS Independent",
    "Topic :: Internet",
    "Topic :: Scientific/Engineering",
    "Topic :: System :: Networking",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: Implementation",
    "Programming Language :: Python :: Implementation :: CPython",
]

# Path to main file
FILE_TAGS = os.path.abspath("src/torseeker/torseeker.py")


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_tag(tag, file):
    contents = open(file, "r", encoding="UTF-8").read()

    match = re.search(
        r"^__{tag}__\s*=\s*['\"]([^'\"]*)['\"]".format(tag=tag), contents, re.M
    )

    if match:
        return match.group(1)
    raise RuntimeError("Failed to find tag __{tag}__.".format(tag=tag))

setup(
    name=get_tag("package", FILE_TAGS),
    version=get_tag("version", FILE_TAGS),
    description=get_tag("description", FILE_TAGS),
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url=get_tag("url", FILE_TAGS),
    author=get_tag("author", FILE_TAGS),
    author_email=get_tag("email", FILE_TAGS),
    maintainer=get_tag("author", FILE_TAGS),
    maintainer_email=get_tag("email", FILE_TAGS),
    download_url=get_tag("url", FILE_TAGS),
    bugtrack_url=get_tag("bug_tracker", FILE_TAGS),
    platforms=["Linux", "Windows", "MAC OS X"],
    classifiers=CLASSIFIERS,
    keywords=["tor", "relay", "network", "ip", "anonymity"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    license=get_tag("license", FILE_TAGS),
    python_requires='>=3',
)