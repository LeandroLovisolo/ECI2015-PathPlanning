# -*- coding: utf-8 -*-
"""
@author: Thomas Fischer
Created on Jul 22 2015
"""

import vrep
import sys
import time
import numpy as np
import math
from quadcopter import Quadcopter

# just in case, close all opened connections
vrep.simxFinish( -1 )

PORT=19997
clientID = vrep.simxStart("127.0.0.1", PORT, True, True, 5000, 5)

# check if client connection successful
if clientID == -1:
  print('Could not connect to remote API server')
  sys.exit( 1 )

print('Connected to remote API server')

ret, handle = vrep.simxGetObjectHandle( clientID, 'Quadricopter_target', vrep.simx_opmode_oneshot_wait )
if ( not ret == vrep.simx_return_ok ):
  print('Failed to retrieve handle for Quadricopter_target')
  sys.exit( 1 )


quad = None

while ( 1 ):

  ret, pos = vrep.simxGetObjectPosition( clientID, handle, -1, vrep.simx_opmode_oneshot_wait )
  if ( not ret == vrep.simx_return_ok ):
    print('Failed to retrieve position for Quadricopter_target')
    sys.exit( 1 )

  print pos

  if quad is None:
    quad = Quadcopter(pos)

  new_pos = quad.update(pos)

  # new_pos = pos
  # new_pos[0] = new_pos[0]+.01

  ret = vrep.simxSetObjectPosition( clientID, handle, -1, new_pos, vrep.simx_opmode_oneshot_wait )
  if ( not ret == vrep.simx_return_ok ):
    print('Failed to set position for Quadricopter_target')
    sys.exit( 1 )
