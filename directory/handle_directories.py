#!/usr/bin/env python

import os 

def mkdir( path ):
    try:
	if not os.path.exists(path):
		os.makedirs( path, 0755 );
    except OSError:
	pass
