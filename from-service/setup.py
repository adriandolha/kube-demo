from setuptools import setup, find_packages

setup(
    name='from_service',
    packages=find_packages(exclude=["tests*"]),
    version='1.0.0',
    description='Source pod from where to copy files to another pod',
    author='Adrian Dolha',
    author_email='adriandolha@yahoo.com',
    license='MIT',
    url='https://pypi.example.com',
    python_requires='>=3'
)
