#!/bin/bash

# Setup script for Google Cluster Analysis project

# 创建 Conda 环境
ENV_NAME="cluster-analysis"
echo "Creating conda environment: $ENV_NAME"
conda create -y -n $ENV_NAME python=3.9.21

# 激活环境
echo "Activating environment: $ENV_NAME"
conda activate $ENV_NAME

# 安装 pip 依赖
echo "Installing required Python packages..."
pip install -r requirements.txt

# 初始化完成
echo "Environment setup complete. Run notebooks under the 'notebooks/' directory."