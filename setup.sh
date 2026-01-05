# Author: Chitraaksh
# All Rights Reserved

#!/bin/bash
# Setup script for Raspberry Pi Face Recognition Project

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing build tools and Python packages..."
sudo apt install -y python3-pip python3-dev cmake gfortran

echo "Installing OpenCV dependencies..."
sudo apt install -y libopencv-dev

echo "Installing math libraries..."
sudo apt install -y libopenblas-dev liblapack-dev

echo "Installing image libraries..."
sudo apt install -y libjpeg-dev libtiff-dev libpng-dev

echo "Installing Python libraries..."
pip3 install --upgrade pip
pip3 install opencv-python face_recognition numpy imutils

echo "Setup complete!"
echo "Remember to enable the Pi Camera using: sudo raspi-config"
echo "Then reboot your Pi before running your face recognition script."
