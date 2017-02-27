#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from spinner_runner import SpinnerRunner, SPINNER_STYLES
import sys, time

for key, value in SPINNER_STYLES.iteritems():
	spinnerRunner = SpinnerRunner(key, True)
	spinnerRunner.start()
	time.sleep(3)
	spinnerRunner.cancel()
