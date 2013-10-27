from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='myvpn',
      version=version,
      description="VPN management utility",
      long_description="""\
Way to manage VPN connections and automatically connect you to your VPN server""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='vpn connection',
      author='Antun Krasic',
      author_email='antun@martuna.co',
      url='',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
	  scripts=['myvpn/bin/myvpn'],
      install_requires=[
		  'pexpect'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
