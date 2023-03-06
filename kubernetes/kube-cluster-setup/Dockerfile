FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install sudo ansible vim curl git sshpass iputils-ping python-is-python3 -y

--disabled-password

COPY README.md inventory *.yml /home/ansible/kube-cluster-setup/

