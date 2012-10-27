# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
      name='django-exchange_rate',
      version='0.1.0',
      author=u'René Lux',
      author_email='luxdevelopment.net',
      packages=find_packages(),
      url='https://github.com/luxdevelopment/django-exchange_rate',
      license='BSD license',
      description='This django app will gave you realtime exchange rate that feed its data from http://themoneyconverter.com The currency symbol that being used are 3 chars currency symbol base from ISO-4217',
      long_description=open('README.rst').read(),
      zip_safe=False,
      install_requires = "feedparser",
      
)