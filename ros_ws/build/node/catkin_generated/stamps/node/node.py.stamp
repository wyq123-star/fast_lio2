#!/usr/bin/env python
# coding:utf-8
import rospy
from geometry_msgs.msg import Twist  # 导入Twist消息类型

def cmd_vel_callback(msg):
    rospy.loginfo("Received velocity command:")
    rospy.loginfo("  Linear: x=%.2f, y=%.2f, z=%.2f", 
                 msg.linear.x, msg.linear.y, msg.linear.z)
    rospy.loginfo("  Angular: x=%.2f, y=%.2f, z=%.2f", 
                 msg.angular.x, msg.angular.y, msg.angular.z)
    print("---")  # 添加分隔线使输出更清晰

if __name__ == '__main__':
    # 创建节点，设置anonymous=True可以避免节点名称冲突
    rospy.init_node("keyboard_listener", anonymous=True)
    print("hello Irvingao! this is ur first ros python code! Good luck for u!")
    
    # 创建订阅者，订阅/turtle1/cmd_vel话题
    # 当有新消息时，调用cmd_vel_callback函数
    rospy.Subscriber("/turtle1/cmd_vel", Twist, cmd_vel_callback, queue_size=10)
    
    # 保持节点运行，等待消息
    rospy.loginfo("Keyboard listener node started. Waiting for messages...")
    rospy.spin()