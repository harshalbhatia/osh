from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt', "r") as f:
        return [line.strip() for line in f.readlines()]


setup(
    name="osh",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements(),
    description="Your saviour when command like strikes you!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/harshalbhatia/osh",
    classifiers=[
        "Programming Language :: Python :: 3.8"
    ],
)
