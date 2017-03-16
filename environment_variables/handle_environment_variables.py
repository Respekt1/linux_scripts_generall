#!/usr/bin/env python

import os 

def set_environ(variable, value)
    os.environ[variable] = value


def get_environ_as_int(variable)
    var_exists = os.environ.get(variable, '-1')
    if invar == '-1':
       # not set
       return -1
    else
	return int(os.environ[variable])


