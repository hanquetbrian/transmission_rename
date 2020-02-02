#!/usr/bin/python3.6

import os
import json

f = open("/home/brian/demofile2.txt", "w")
f.write(json.dumps(dict(os.environ)))
f.close()

