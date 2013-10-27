from myvpn.connection import VPNConnection
from myvpn.cli import myvpnCLI
import os
import sys

class Management:

	def __init__(self):
		# Auto check for directory
		self.create_config()
		self.check_for_sudo()
		self.check_mydir()
		self.check_profile_directory()

	# Create a config dictonary
	def create_config(self):
		clidata = self.get_option_parser()
		profile = clidata.profile

		home = os.environ['HOME']
		mydir = home+'/.myvpn/'
		self.config = { 'home' : home,
				'mydir' : mydir,
				'profile' : mydir+'/'+profile+'/',
				'profile_name' : profile }

	def get_option_parser(self):
		mcli = myvpnCLI()
		cli = mcli.get_values()


		if cli.profile == None:
			mcli.show_help()
		else:
			return cli

	# Create ~/.myinfo directoy if it doesn't exist
	def check_mydir(self):
		if os.path.exists(self.config['mydir']) != True:
			print "> Creating %s" % [self.config['mydir']]
			if os.makedirs(self.config['mydir']):
				print "%s created successfully!" % [self.config['mydir']]

	def check_profile_directory(self):
		if not os.path.exists(self.config['profile']):
			raise Exception("""Profile directory doesn't exist, please create \
it inside ~/.myvpn/ directory with the valid structure.""")

	def check_for_sudo(self):
		if not os.path.exists(self.config['mydir']+".sudo"):
			raise Exception("""Please create ~/.myvpn/.sudo file containing \
your sudo password""")

	def connect(self):
		conn = VPNConnection(self.config)
		conn.open()



