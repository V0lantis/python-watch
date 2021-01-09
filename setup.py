import io
import os
from setuptools import setup, find_packages


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filepath, mode='r', encoding='utf-8') as f:
        return f.read()


setup(
    name='python-watch',
    version='0.1.0',
    description='Local continuous script runner with watchdog.',
    long_description=read('README.md'),
    author='Arthur Volant',
    author_email='arthurvolant@gmail.com',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    install_requires=read('requirements.txt').splitlines(),
    entry_points={
        'console_scripts': [
            'python-watch = python_watch:main',
            'pyw = python_watch:main',
        ]
    },
)
