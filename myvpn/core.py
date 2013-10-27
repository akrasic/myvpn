from myvpn.connection import VPNConnection
import os

class Management:

	def __init__(self, profile):
		# Auto check for directory
		self.create_config(profile)
		self.check_for_sudo()
		self.check_mydir()
		self.check_profile_directory()

	# Create a config dictonary
	def create_config(self, profile):
		home = os.environ['HOME']
		mydir = home+'/.myvpn/'
		self.config = { 'home' : home,
				'mydir' : mydir,
				'profile' : mydir+'/'+profile+'/',
				'profile_name' : profile }

	# Create ~/.myinfo directoy if it doesn't exist
	def check_mydir(self):
		if os.path.exists(self.config['mydir']) != True:
			print "> Creating %s" % [self.config['mydir']]
			if os.makedirs(self.config['mydir']):
				print "%s created successfully!" % [self.config['mydir']]

	def check_profile_directory(self):
		if not os.path.exists(self.config['profile']):
			raise Exception("""Profile directory doesn't exist, please create it
inside ~/.myvpn/ directory with the valid structure.""")

	def check_for_sudo(self):
		if not os.path.exists(self.config['mydir']+".sudo"):
			raise Exception("""Please create ~/.myvpn/.sudo file containing your
sudo password""")

	def connect(self):
		conn = VPNConnection(self.config)
		conn.open()



