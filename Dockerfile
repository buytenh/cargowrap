FROM fedora:41
RUN dnf -y upgrade
RUN dnf -y install gcc openssl-devel
RUN useradd -s /bin/bash buytenh
USER buytenh
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN /home/buytenh/.cargo/bin/rustup toolchain install nightly-2024-07-21
