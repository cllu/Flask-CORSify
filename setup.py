"""
Flask-CORSify
------------

This is a simple Flask extension that configures your Flask application to allow
CORS from selected origins.
"""

from setuptools import setup

setup(
    name='Flask-CORSify',
    version='0.1.0',
    url='https://github.com/cllu/Flask-CORSify',
    license='BSD',
    author='Chunliang Lyu',
    author_email='hi@chunlianglyu.com',
    description='Add CORS support for your Flask app.',
    long_description=__doc__,
    py_modules=['flask_corsify'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
