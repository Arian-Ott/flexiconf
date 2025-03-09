from setuptools import setup, find_packages

setup(
    name='flexiconf',
    version='0.1.0',
    description='A typed, reloadable configuration library for Python',
    author='Arian Ott',
    author_email='',
    url='https://github.com/Arian-Ott/flexiconf',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pydantic>=1.0.0',
        'watchdog>=2.1.0'
    ],
    python_requires='>=3.13'
)
