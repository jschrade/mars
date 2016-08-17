try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
import pip

APP_NAME = 'mars_rover'
VERSION = '0.1'

install_reqs = pip.req.parse_requirements(
    'requirements.txt',
    session=pip.download.PipSession()
)
required = [str(ir.req) for ir in install_reqs]

settings = dict(
    name=APP_NAME,
    version=VERSION,
    author='Josh Schrade',
    author_email='josh@acedevs.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    url='https://github.com/jschrade/mars.git',
    license='',
    description='Code Challenge',
    long_description=open('README.md').read(),
    install_requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ]
)

setup(**settings)
