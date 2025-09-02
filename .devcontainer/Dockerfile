FROM osrf/ros:noetic-desktop-full

ARG USERNAME=yutou
ARG USER_UID=1000
ARG USER_GID=1000

ENV DEBIAN_FRONTEND=noninteractive

# 设置地区信息
RUN apt-get update && \
    apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

# 安装所有依赖项
RUN apt-get update && \
    apt-get install -y \
    nautilus \
    gedit \
    cmake \
    git \
    libboost-all-dev \
    build-essential \
    libtbb-dev \
    libopencv-dev \
    python3-opencv \
    python3-pip \
    libeigen3-dev \
    && rm -rf /var/lib/apt/lists/*

# 创建用户
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    apt-get update && \
    apt-get install -y sudo && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER $USERNAME
WORKDIR /home/$USERNAME


# RUN mkdir fastlivo2 && \
#     cd fastlivo2 && \
#     mkdir packages && \
#     cd packages && \ 
#     git clone https://github.com/strasdat/Sophus.git && \
#     cd .. && \
#     mkdir -p catkin_ws/src && \
#     cd catkin_ws/src 
    # git clone https://github.com/xuankuzcr/rpg_vikit.git && \
    # git clone https://github.com/hku-mars/FAST-LIVO2
    # cd Sophus && \
    # git checkout b474f05 && \ 不切换分支会报错 你的cmake版本过低
    # mkdir build && cd build && \
    # cmake .. -DCMAKE_INSTALL_PREFIX=/home/$USERNAME/catkin_ws/devel && \
    # make && \           神人报错，需要修改so2.cpp文件内容
    # make install && \
    # # 验证安装
    # ls /home/$USERNAME/catkin_ws/devel/include/Sophus && \
    # ls /home/$USERNAME/catkin_ws/devel/lib/cmake/Sophus

# 下载其他代码



# # 构建代码（关键改进）
# RUN /bin/bash -c " \
#     source /opt/ros/noetic/setup.bash && \
#     export Sophus_DIR=/home/$USERNAME/catkin_ws/devel/lib/cmake/Sophus && \
#     export CMAKE_PREFIX_PATH=/home/$USERNAME/catkin_ws/devel:\$CMAKE_PREFIX_PATH && \
#     cd ~/catkin_ws && \
#     catkin_make -DCMAKE_BUILD_TYPE=Release \
#     "

# 配置环境变量
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc && \
    echo "source ~/fastlivo2/catkin_ws/devel/setup.bash" >> ~/.bashrc && \
    echo "source ~/fastlivo2/ros_ws/devel/setup.bash" >> ~/.bashrc 



CMD ["/bin/bash"]