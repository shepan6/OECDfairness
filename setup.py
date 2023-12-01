from setuptools import setup, find_packages
import os

with open('../requirements.txt') as f:
    required_packages = f.read().splitlines()

required_dev_packages = []
if "requirements-dev.txt" in os.listdir():
    with open('../requirements-dev.txt') as f:
        required_dev_packages = f.read().splitlines()

long_description = None
if "README.md" in os.listdir():
    with open ("README.md", "r") as f:
        long_description = f.read()



setup(
    name='ethically',
    version='1.0',
    packages=find_packages("app/src"),
    # entry_points={
    #     'console_scripts': ['your-command = your_package.module:your_function'],
    # },
    package_dir={"": "src"},
    install_requires=[required_packages],
    author='Alexander Shepherd',
    author_email='alexnshepherd@hotmail.com',
    description='To evaluate ethical aspects of data and modelling pipeline',
    license='MIT',
    url='https://github.com/shepan6/ethicAI',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLV2+)!",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={
        "dev": required_dev_packages,
    },
)