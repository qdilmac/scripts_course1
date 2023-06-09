#!/usr/bin/env python3

import rospy
import sys
from udemy_pkg.srv import AddTwoInts
from udemy_pkg.srv import AddTwoIntsRequest
from udemy_pkg.srv import AddTwoIntsResponse

def add_two_ints_client(x,y):
    rospy.wait_for_service("add_two_ints") #ros_server içerisinde s= ... olarak tanımlanan sunucu ismiyle aynı olmalı !
    try:
        add_two_ints = rospy.ServiceProxy("add_two_ints", AddTwoInts)
        resp1 = add_two_ints(x,y)
        return resp1.sum
    except rospy.ServiceException(e):
        print("Service call failed: {}".format(e))

def usage(): # ?
    return

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("{} [x y]".format(sys.argv[0]))
        sys.exit(1)
    print("Requesting {} + {}".format(x,y))
    s = add_two_ints_client(x,y)
    print("{} + {} = {}".format(x,y,s))