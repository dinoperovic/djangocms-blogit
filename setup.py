import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    """Return the README file contents. Supports text,rst, and markdown"""
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file(name)
    return ''

setup(
    name="cmsplugin-blogit",
    version=__import__('blogit').__version__,
    url='http://pypi.python.org/pypi/cmsplugin-blogit/',
    author='Dino Perovic',
    author_email='dino.perovic@gmail.com',
    description='django-cms blog plugin',
    long_description=get_readme(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=(
        'django-cms>=2.4',
        'django-hvad==0.3',
        'easy-thumbnails==1.4',
        'django-filer>=0.9',
        'django-taggit==0.10',
    ),
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
