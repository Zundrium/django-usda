import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_usda',
    version='0.1',
    include_package_data=True,
    license='MIT License',
    description='An easy to set up Django Rest Framework API that is compatible with the USDA Nutrient Database.',
    long_description=README,
    author='Sem Verbraak',
    author_email='slsverbraak@gmail.com',
    install_requires=[
        'djangorestframework',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=[
        'django_usda',
        'django_usda.management',
        'django_usda.management.commands',
    ],
)
