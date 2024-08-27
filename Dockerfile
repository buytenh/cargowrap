FROM fedora:40
RUN dnf -y upgrade
RUN dnf -y install gcc
RUN useradd -s /bin/bash buytenh
USER buytenh
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
