from setuptools import setup, find_packages

setup(
    name='to_service',
    packages=find_packages(exclude=["tests*"]),
    version='1.0.0',
    description='Destination pod where to copy files from another pod',
    author='Adrian Dolha',
    author_email='adriandolha@yahoo.com',
    license='MIT',
    url='https://pypi.example.com',
    python_requires='>=3'
)
