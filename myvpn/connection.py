import pexpect
import sys

class VPNConnection:

	def __init__(self, config):
		self.config = config
		self.ovpn = self.config['profile']+self.config['profile_name']+'.ovpn'

		# Load the sudo pw
		self.read_sudo()
		self.password = raw_input("Enter VPN  passphrase: ")

	def open(self):
		command = "sudo openvpn --config "+self.ovpn

		child = pexpect.spawn(command)
		child.expect('\[sudo\] password.*:')
		child.sendline(self.sudo)
		child.expect('^.*Username:')
		child.sendline(self.config['profile_name'])

		child.expect('^.*Password:')
		child.sendline(self.password)
		child.interact()

	def read_sudo(self):
		f = open(self.config['mydir']+'.sudo')
		self.sudo = f.readlines()[0].rsplit()[0]

