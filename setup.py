from setuptools import setup, find_packages

setup(
    name="python-desknet",
    version="0.0.0",
    packages=find_packages(),
    install_requires=(
        "requests",
    ),
    test_suite='desknet.tests',
    author="Los Angeles Times Data Desk",
    author_email="datadesk@latimes.com",
    description="A simple Python wrapper for Desk-Net.com's API ",
    url="http://github.com/datadesk/python-desknet",
    license="MIT",
)
