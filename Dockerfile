# Example Dockerfile for ROS 2 Humble and Gazebo
FROM osrf/ros:humble-desktop-full

# Install Gazebo dependencies if not included in base image
RUN apt-get update && apt-get install -y \
    ros-humble-gazebo-ros \
    vim \
    # Add other necessary Gazebo packages or ROS 2 packages
    && rm -rf /var/lib/apt/lists/*

# Copy custom code or setup workspaces
WORKDIR /ausros_turtlebot

# Build ROS 2 workspace
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build"
