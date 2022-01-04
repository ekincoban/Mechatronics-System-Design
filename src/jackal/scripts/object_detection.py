
import rospy
from sensor_msgs.msg import Image
import cv2
import time
from cv_bridge import CvBridge, CvBridgeError

""" Showing the camera view on a screen """

rospy.init_node('opencv_example', anonymous=True)
bridge = CvBridge()
counter=0
#pub=rospy.Publisher("/rear_upper/image_raw",Image,queue_size=1)
def show_image(img):
    cv2.imshow("Car Front Camera View", img)
    cv2.waitKey(3)


def image_callback(img_msg):
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
        cv_image=cv2.cvtColor(cv_image,cv2.COLOR_BGR2RGB)
        
    except CvBridgeError, e:
        rospy.logerr("CvBridge Error: {0}".format(e))

    show_image(cv_image)

sub_image = rospy.Subscriber("/rear_upper/image_raw", Image, image_callback)
cv2.namedWindow("Car Front Camera View", 1)

while not rospy.is_shutdown():
      rospy.spin()