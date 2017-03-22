import os
import sys

from setuptools import find_packages, setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = find_packages()

setup(
    name='django_weather_darksky',
    version='0.1.0',
    description='Wrapper for darksky.net API for django',
    long_description='Simply wrapper for https://darksky.net API for django',
    author='Slava M',
    author_email='master@neucom.ru',
    url='https://github.com/slavama/django_weather_darksky',
    packages=packages,
    include_package_data=True,
    py_modules=['django_weather_darksky'],
    requires = ['python (>= 2.7)', 'django (>= 1.8)'],
    install_requires=[
        'requests>=2'
    ],
    license='MIT License',
    zip_safe=False,
    keywords='forecast forecast.io darksky.net weather',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
