import sys
print(sys.version)

import os
os.environ['ACTIVELOOP_TOKEN'] = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTY4MjQ1NTc1OCwiZXhwIjoxNjg4MTU4MDIwfQ.eyJpZCI6ImVkbXVuZGJlcmttYW5uIn0.vaP4o-zEc-NSuUJQher8iemlXd-cL_uibN_nfgPdWALEQTMPMgZttZZjOq1NUtsLWJZ_B8wRTgp2UhHGkUDFpg"

import deeplake

ds = deeplake.empty('hub://Steelo/Steelo-dataset')
ds = deeplake.dataset('hub://Steelo/Steelo-dataset')