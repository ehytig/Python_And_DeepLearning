FROM 10.11.3.8:5000/bitahub/pytorch:1.3-py3
RUN apt update && apt install -y libsm6 libxext6
RUN apt-get install -y libxrender-dev
RUN pip install torch==1.8.0+cu101 torchvision==0.9.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.8/index.html


