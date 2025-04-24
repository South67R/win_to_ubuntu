#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty
msg = """
Reading from keyboard and Publishing to /cmd_vel!
---------------------------
Moving around:
   w
a  s  d
   x

CTRL-C to quit
"""
speed_linear = 0.5
speed_angular = 1.0

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('control_keyboard')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    x = 0
    th = 0
    try:
        print(msg)
        while not rospy.is_shutdown():
            key = getKey()
            if key == 'w':
                x = 1
                th = 0
            elif key == 's':
                x = 0
                th = 0
            elif key == 'x':
                x = -1
                th = 0
            elif key == 'a':
                x = 0
                th = 1
            elif key == 'd':
                x = 0
                th = -1
            else:
                x = 0
                th = 0
                if key == '\x03':  # CTRL-C
                    break
            
            twist = Twist()
            twist.linear.x = x * speed_linear
            twist.angular.z = th * speed_angular
            pub.publish(twist)
    except Exception as e:
        print(e)
    finally:
        twist = Twist()
        pub.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
