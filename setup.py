import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='foaas',
    version='0.2.0',
    description='Fuck Off As A Service',
    license='MIT',
    url='https://github.com/dmpayton/foaas-python',
    author='Derek Payton',
    author_email='derek.payton@gmail.com',
    py_modules=['foaas'],
    install_requires=['requests'],
    classifiers=(
        # 'Development Status :: 6.5 - Immature'
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ),
)
