import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/admin-2/batch2/ros2_ws/install/robot_controller_sept03'
