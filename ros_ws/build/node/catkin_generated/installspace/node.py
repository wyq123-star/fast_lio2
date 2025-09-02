#!/usr/bin/env python3
# coding:utf-8
import rospy
import subprocess
from geometry_msgs.msg import Twist  # 导入Twist消息类型
# 定义一个全局标志位，确保只启动一次
launch_triggered = False

def cmd_vel_callback(msg):
    global launch_triggered
    
    rospy.loginfo("Received velocity command:")
    rospy.loginfo("  Linear: x=%.2f, y=%.2f, z=%.2f", 
                 msg.linear.x, msg.linear.y, msg.linear.z)
    rospy.loginfo("  Angular: x=%.2f, y=%.2f, z=%.2f", 
                 msg.angular.x, msg.angular.y, msg.angular.z)
    print("---")
    
    # 检查是否已经触发过，避免重复启动
    if not launch_triggered:
        rospy.loginfo("检测到速度命令，正在启动目标launch文件...")
        try:
            # 使用subprocess.Popen在后台启动launch文件
            # 替换"your_package_name"和"your_launch_file.launch"为你的实际包名和launch文件名
            process = subprocess.Popen(["roslaunch", "your_package_name", "your_launch_file.launch"])
            launch_triggered = True
            rospy.loginfo("目标launch文件已启动 (PID: %d)", process.pid)
        except Exception as e:
            rospy.logerr("启动launch文件失败: %s", str(e))

if __name__ == '__main__':
    rospy.init_node("keyboard_listener", anonymous=True)
    print("hello Irvingao! this is ur first ros python code! Good luck for u!")

    rospy.Subscriber("/turtle1/cmd_vel", Twist, cmd_vel_callback, queue_size=10)
    
    rospy.loginfo("Keyboard listener node started. Waiting for messages...")
    rospy.spin()