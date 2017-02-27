#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from spinner_runner import SpinnerRunner
import sys

spinnerRunner = SpinnerRunner(sys.argv[1], True)

if len(sys.argv) > 2:
	spinnerRunner.setLoadingString(sys.argv[2])

spinnerRunner.start()
