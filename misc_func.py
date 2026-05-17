# -*- coding: utf-8 -*-

from time import strftime, localtime, time
from datetime import timedelta

#******************************************************************************
def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))
