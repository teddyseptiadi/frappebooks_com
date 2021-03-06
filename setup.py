# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappebooks_com/__init__.py
from frappebooks_com import __version__ as version

setup(
	name='frappebooks_com',
	version=version,
	description='Website for Frappe Books',
	author='Frappe Technologies',
	author_email='developers@frappe.io',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
