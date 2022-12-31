FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git
RUN git clone https://github.com/elliotfklein/ddia-4-protobufs-rpc.git
WORKDIR /ddia-4-protobufs-rpc
RUN pip install -r requirements.txt
CMD ["/bin/bash"]
