#!/bin/bash
# Script to setup the your deep-learning machine
# Developed and tested on 64 bit Ubuntu 14.04.
#
# Author: Lakshay Garg <lakshayg@iitk.ac.in>

# Configuration Parameters
USE_GPU=true
INSTALL_CMD="apt-get install -y"
PIP_INSTALL_CMD="pip install"
DL_DATASETS=false

# Install Packages
packages=(                                   \
    vim nano git tig python-dev ipython      \  
    build-essential libopencv-dev            \
    libboost-all-dev gcc g++ tmux pkg-config \
    ack-grep exuberant-ctags gfortran        \
    python-pip python-numpy cmake            \
    python-scipy python-sklearn              \
    python-matplotlib python-nltk            \
    python-h5py python-pil python-opencv     \
    libhdf5-serial-dev python-skimage        \
    libblas-dev libatlas-dev libopencv-dev   \
    software-properties-common wget          \
    libprotobuf-dev libleveldb-dev           \
    libsnappy-dev libopencv-dev              \
    libhdf5-serial-dev protobuf-compiler     \
    libgflags-dev libgoogle-glog-dev         \
    liblmdb-dev python-nose python-pygments  \
    python-sphinx  libatlas-base-dev         \
)

for item in ${packages[*]}; do
    dpkg -s $item &> /dev/null
    if [ $? -ne 0 ]; then
        echo -e "Installing [$item]. \c"
        $INSTALL_CMD $item > /dev/null
        if [ $? -ne 0 ]; then
            echo "Could not install the package [code: $?]"
        else
            echo "Package successfully installed"
        fi
    else
        echo "Already Installed [$item]"
    fi
done

pip_packages=(                              \
    pgen cython hickle scikit-image keras   \
    Theano                                  \
)

# Install python packages
for item in ${pip_packages[*]}; do
    echo -e "Installing [$item]. \c"
    $PIP_INSTALL_CMD $item > /dev/null
    if [ $? -ne 0 ]; then
        echo "Could not install the package [code: $?]"
    else
        echo "Package successfully installed"
    fi
done

# Install GPU Drivers
# if [ "$USE_GPU" = true ]; then
#    PPA=ppa:graphics-drivers/ppa
#    echo "Installing GPU Drivers"
#    if ! grep -q "$PPA" /etc/apt/sources.list /etc/apt/sources.list.d/*; then
#        add-apt-repository -y $PPA
#        apt-get update
#    fi
#    $INSTALL_CMD nvidia-352
# fi

# Install TensorFlow
echo -e "Installing [tensorflow]. \c"
python -c "import tensorflow" &> /dev/null
if [ $? -ne 0 ]; then # check if it is already installed
    if [ "$USE_GPU" = true ]; then
        export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0rc0-cp27-none-linux_x86_64.whl
    else
        export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0rc0-cp27-none-linux_x86_64.whl
    fi
    pip install --upgrade $TF_BINARY_URL &> /dev/null
    if [ $? -ne 0 ]; then
        echo "Could not install the package [code: $?]"
    else
        echo "Package successfully installed"
    fi
else
    echo "Package successfully installed"
fi

if [ ! -d "~/mlpack" ]; then
    mkdir ~/mlpack   # directory for installing packages from source
fi

# Install Torch
if [ ! -d "~/mlpack/torch" ]; then
    echo "Installing [Torch]"
    pushd ~/mlpack
    git clone https://github.com/torch/distro.git torch --recursive
    cd torch; bash install-deps;
    ./install.sh
    popd
    echo "Installed"
else
    echo "Already Installed [Torch]"
fi

exit 0

# Install Caffe (assumes GPU is available, change makefile for CPU only)
if [ ! -d "~/mlpack/caffe" ]; then
    pushd ~/mlpack
    git clone https://github.com/BVLC/caffe.git
    cd caffe
    cp Makefile.config.example Makefile.config
    sudo pip install -r python/requirements.txt
    make all -j $(($(nproc) + 1))
    make test -j $(($(nproc) + 1))
    make runtest -j $(($(nproc) + 1))
    make pycaffe -j $(($(nproc) + 1))
    echo 'export CAFFE_ROOT=$(pwd)' >> ~/.bashrc
    echo 'export PYTHONPATH=$CAFFE_ROOT/python:$PYTHONPATH' >> ~/.bashrc
    source ~/.bashrc
    popd
    echo "Installed"
else
    echo "Already Installed [Caffe]"
fi
