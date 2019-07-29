import os
class Progress:

	def __init__(self, range_v, step=5, cls=False):
		self.step = step
		self.range_v = range_v - 1
		self.last_p = 0
		self.cls = cls
		self.prog_string = []
		for i in range(100//step):
			self.prog_string.append(" ")

	def compute(self, iter):
		progress = iter / self.range_v
		progress *= 100
		dash = progress // self.step

		if dash != self.last_p:

			self.last_p = dash
			if self.cls:
				self._clear()
			string = ""
			prog_percent = str(progress) + " %"
			self.prog_string[int(dash) - 1] = "-"
			for st in self.prog_string:
				string += st
			
			print("|" + string + "| "+ prog_percent)

	def _clear(self):
		os.system('clear')
