from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

setup(
    name='agots',
    author='Sebastian Bischoff, Willi Gierke',
    description='Anomaly Generator on Time Series',
    long_description=open('README.md').read(),
    version='0.1',
    packages=[],
    scripts=[],
    install_requires=parse_requirements('requirements.txt'),
    url='github.com/WGierke/agots',
    license='MIT License',
)
