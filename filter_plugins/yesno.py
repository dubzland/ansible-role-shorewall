#!/usr/bin/python

def yesno(value, icaps=True):
	"""
	Return 'yes' or 'no' according to the (assumed-bool) value.
	"""

	if (value):
		str = 'Yes' if icaps else 'yes'
	else:
		str = 'No' if icaps else 'no'

	return str


class FilterModule(object):

	def filters(self):
		return {
			'yesno': yesno,
		}
