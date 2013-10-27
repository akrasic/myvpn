from optparse import OptionParser
import sys

class myvpnCLI:

	def __init__(self):
		self.parser = OptionParser()
		self.create_menu()

	def create_menu(self):
		self.parser.add_option("-n", "--profile", dest="profile",
				help="Profile name")

	def get_values(self):
		(opt, args) = self.parser.parse_args()
		return opt

	def show_help(self):
		self.parser.print_help()
		sys.exit()
