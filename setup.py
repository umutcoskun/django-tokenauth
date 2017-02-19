import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tokenauth',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='The GNU General Public License v3.0',
    description='Token based authentication for Django.',
    long_description=README,
    url='https://github.com/umutcoskun/django-tokenauth',
    author='Umut Çağdaş Coşkun',
    author_email='umut34@outlook.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Entended Audience :: Developers',
        'License :: The GNU General Public License v3.0',
        'Operating System :: Os Independent',
        'Programming Language :: Python',
    ]
)
