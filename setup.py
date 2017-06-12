from setuptools import setup


setup(
    name='python-desknet',
    version='0.0.1',
    description='A simple Python wrapper for the DeskNet API',
    author='Los Angeles Times Data Desk',
    author_email='datadesk@latimes.com',
    url='http://www.github.com/datadesk/python-desknet/',
    license="MIT",
    packages=("desknet",),
    test_suite="desknet.tests",
    include_package_data=True,
    install_requires=(
        'requests',
    ),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ),
)
