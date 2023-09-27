from setuptools import setup, find_packages

with open('../requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='ethically',
    version='1.0',
    packages=find_packages(),
    # entry_points={
    #     'console_scripts': ['your-command = your_package.module:your_function'],
    # },
    install_requires=[required_packages],
    author='Alexander Shepherd',
    author_email='alexnshepherd@hotmail.com',
    description='To evaluate ethical aspects of data and modelling pipeline',
    license='MIT',
    url='https://github.com/your-username/your-repository',
)
