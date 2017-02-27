#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import print_function
import time, sys, threading
from spinners import *

SPINNER_STYLES = {'dot0' : DotSpinner0(), 'dot1' : DotSpinner1(), 'dot2' : DotSpinner2(), 'star' : StarSpinner(), 'moon' : MoonSpinner(), 'clock' : ClockSpinner(), 'arrow0' : ArrowSpinner0(), 'arrow1' : ArrowSpinner1()}

COLOR_START = 31
COLOR_END 	= 27
TAIL_LENGTH = 3
TAIL_CHAR = '.'

class SpinnerRunner:
	colorCursor = COLOR_START
	tailCursor = 0
	occupyCursor = TAIL_LENGTH
	loadingString = 'Loading'

	spinner = None

	shouldSwitchColors = False
	cancelled = False
	
	def __init__(self, spinnerStyle, shouldSwitchColors = False):
		if not spinnerStyle is None and spinnerStyle in SPINNER_STYLES:
			self.spinner = SPINNER_STYLES[spinnerStyle]

		self.shouldSwitchColors = shouldSwitchColors

	def resetArgs(self):
		self.colorCursor = COLOR_START
		self.tailCursor = 0
		self.occupyCursor = TAIL_LENGTH

	def setLoadingString(self, loadingString):
		self.loadingString = loadingString

	def singleRun(self):
		self.occupyCursor = TAIL_LENGTH - self.tailCursor
		
		tail = TAIL_CHAR * self.tailCursor
		occupy = ' ' * self.occupyCursor

		if self.shouldSwitchColors:
			print("\x1b[0;" + `self.colorCursor` + "m" + self.spinner.next() + '\x1b[0;0m ' + self.loadingString + tail + occupy)
		else:
			print(self.spinner.next() + ' ' + self.loadingString + tail + occupy)
		
		sys.stdout.write("\033[F")

		if self.tailCursor == TAIL_LENGTH:
			self.tailCursor = 0
		else:
			self.tailCursor = self.tailCursor + 1

		if self.spinner.cursor == self.spinner.length() - 1:
			self.colorCursor = self.colorCursor + 1

		if self.colorCursor == COLOR_END:
			self.colorCursor = COLOR_START

		time.sleep(0.4)

	def start(self):
		try:
			threading.Thread(target=self.run).start()
		except Exception as e:
			print(str(e))

	def run(self):
		while not self.cancelled:
			self.singleRun()

	def cancel(self):
		self.cancelled = True
