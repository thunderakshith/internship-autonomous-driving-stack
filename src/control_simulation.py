lane_center = 320
vehicle_position = 300

error = lane_center - vehicle_position

if error > 10:
    action = "Steer Right"
elif error < -10:
    action = "Steer Left"
else:
    action = "Go Straight"

print("Control Action:", action)
