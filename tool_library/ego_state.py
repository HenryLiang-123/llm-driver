# Not really a tool you call but you call this to get current state of vehicle
# Current State:
#  - Velocity (vx,vy): (-0.01,0.92)
#  - Heading Angular Velocity (v_yaw): (0.00)
#  - Acceleration (ax,ay): (-0.00,-0.50)
#  - Can Bus: (-0.74,0.14)
#  - Heading Speed: (0.95)
#  - Steering: (-0.02)
# Historical Trajectory (last 2 seconds): [(-0.07,-6.43), (-0.05,-4.34), (-0.02,-2.32), (-0.01,-0.91)]
# Mission Goal: FORWARD

def get_current_state(ego):
    