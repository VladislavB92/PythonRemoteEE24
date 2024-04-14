class Board:

	def __init__(
			self,
			cell1=None,
			cell2=None,
			cell3=None,
			cell4=None,
			cell5=None,
			cell6=None,
			cell7=None,
			cell8=None,
			cell9=None
	):
		self.cell1 = cell1
		self.cell2 = cell2
		self.cell3 = cell3
		self.cell4 = cell4
		self.cell5 = cell5
		self.cell6 = cell6
		self.cell7 = cell7
		self.cell8 = cell8
		self.cell9 = cell9

	def board_output(self):
		x = [
			[self.cell1, self.cell2, self.cell3],
			[self.cell4, self.cell5, self.cell6],
			[self.cell7, self.cell8, self.cell9]
		]
		for row in x:
			print(row)

	def board_input(self, input_source, mark):
		if input_source == "1":
			self.cell1 = mark
		if input_source == "2":
			self.cell2 = mark
		if input_source == "3":
			self.cell3 = mark
		if input_source == "4":
			self.cell4 = mark
		if input_source == "5":
			self.cell5 = mark
		if input_source == "6":
			self.cell6 = mark
		if input_source == "7":
			self.cell7 = mark
		if input_source == "8":
			self.cell8 = mark
		if input_source == "9":
			self.cell9 = mark
