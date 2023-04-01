from setuptools import setup, find_packages
from subprocess import PIPE, Popen
from setuptools.command.install import install


def cmdline(command):
    process = Popen(args=command, stdout=PIPE, shell=True)
    return process.communicate()[0]


def get_requirements():
    with open('requirements.txt', "r") as f:
        return [line.strip() for line in f.readlines()]


class CustomInstallCommand(install):
    def run(self):
        super().run()
        print(cmdline('chmod +x install.sh').decode('utf-8'))
        print(cmdline('./install.sh').decode('utf-8'))


setup(
    name="osh_python",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements(),
    description="Your saviour, when command like strikes you with errors!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/harshalbhatia/osh",
    classifiers=[
        "Programming Language :: Python :: 3.8"
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
    entry_points={
        'console_scripts': [
            'osh_py = osh.main:main',
        ],
    },
)
