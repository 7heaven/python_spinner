# -*- coding: UTF-8 -*-

class Spinner:
	frames = None
	cursor = 0
	len = 0

	def __init__(self, frames = None):
		self.setFrames(frames)

	def setFrames(self, frames):
		self.frames = frames
		if not self.frames is None:
			self.len = len(self.frames)
			self.cursor = 0

	def next(self):
		if self.frames is None or self.len == 0:
			raise ValueError('frames must not be null & should contains at least one element')

		result = self.frames[self.cursor]
	
		if self.cursor == self.len - 1:
			self.cursor = 0
		else:
			self.cursor = self.cursor + 1

		return result

	def length(self):
		if self.frames is None:
			return 0

		return self.len

class DotSpinner0(Spinner):

	def __init__(self):
		Spinner.__init__(self, [u'⠋', u'⠙', u'⠹', u'⠸', u'⠼', u'⠴', u'⠦', u'⠧', u'⠇', u'⠏'])

class DotSpinner1(Spinner):
	
	def __init__(self):
		Spinner.__init__(self,  ['⢀⠀', '⡀⠀', '⠄⠀', '⢂⠀', '⡂⠀', '⠅⠀', '⢃⠀', '⡃⠀', '⠍⠀', '⢋⠀', '⡋⠀', '⠍⠁', '⢋⠁', '⡋⠁', '⠍⠉', '⠋⠉', '⠋⠉', '⠉⠙', '⠉⠙', '⠉⠩', '⠈⢙', '⠈⡙', '⢈⠩', '⡀⢙', '⠄⡙', '⢂⠩', '⡂⢘', '⠅⡘', '⢃⠨', '⡃⢐', '⠍⡐', '⢋⠠', '⡋⢀', '⠍⡁', '⢋⠁', '⡋⠁', '⠍⠉', '⠋⠉', '⠋⠉', '⠉⠙', '⠉⠙', '⠉⠩', '⠈⢙', '⠈⡙', '⠈⠩', '⠀⢙', '⠀⡙', '⠀⠩', '⠀⢘', '⠀⡘', '⠀⠨', '⠀⢐', '⠀⡐', '⠀⠠', '⠀⢀', '⠀⡀'])

class DotSpinner2(Spinner):

	def __init__(self):
		Spinner.__init__(self,  ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷'])

class MoonSpinner(Spinner):

	def __init__(self):
		Spinner.__init__(self,  ['🌑 ', '🌒 ', '🌓 ', '🌔 ', '🌕 ', '🌖 ', '🌗 ', '🌘 '])

class StarSpinner(Spinner):

	def __init__(self):
		Spinner.__init__(self, ['✶', '✸', '✹', '✺', '✹', '✷'])

class ClockSpinner(Spinner):

	def __init__(self):
		Spinner.__init__(self,  ['🕐 ', '🕑 ', '🕒 ', '🕓 ', '🕔 ', '🕕 ', '🕖 ', '🕗 ', '🕘 ', '🕙 ', '🕚 '])

class ArrowSpinner0(Spinner):

	def __init__(self):
		Spinner.__init__(self, ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'])

class ArrowSpinner1(Spinner):

	def __init__(self):
		Spinner.__init__(self, ['▹▹▹▹▹', '▸▹▹▹▹', '▹▸▹▹▹', '▹▹▸▹▹', '▹▹▹▸▹', '▹▹▹▹▸'])
