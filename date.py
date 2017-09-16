from datetime import datetime
from statusModule import EasyI3StatusModule

class Module(EasyI3StatusModule):
	validDuration = 60

	def __init__(self, config):
		self.values = [{
			'full_text': '',
			'name': 'date',
			'separator_block_width': 40
		}];
		self.dateFormat = config.get('format', '%d-%m-%Y %H:%M')

	def update(self):
		self.values[0]['full_text'] = datetime.now().strftime(self.dateFormat)
