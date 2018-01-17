import os
import sys
from setuptools import find_packages, setup

from uwallet import __version__

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: prowallet requires Python version >= 2.7.0...")

data_files = []

requires = [
    'slowaes',
    'ecdsa',
    'pbkdf2',
    'requests',
    'jsonrpclib',
    'six',
    'appdirs',
    'protobuf',
    'jsonschema',
    'unetschema',
]

console_scripts = [
    'uwallet = uwallet.main:main',
]

base_dir = os.path.abspath(os.path.dirname(__file__))

setup(
    name="uwallet",
    version=__version__,
    install_requires=requires,
    packages=find_packages(exclude=['tests']),
    package_data={'uwallet': ['wordlist/*.txt']},
    entry_points={'console_scripts': console_scripts},
    description="Lightweight unet Wallet",
    author="UC Inc.",
    author_email="qiping@unet.io",
    license="GNU GPLv3",
    url="https://b.network",
    long_description="""Lightweight unet Wallet""",
    zip_safe=False
)
