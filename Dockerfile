FROM fedora:42
RUN dnf -y upgrade
RUN dnf -y install gcc openssl-devel
RUN useradd -s /bin/bash buytenh
USER buytenh
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN /home/buytenh/.cargo/bin/rustup toolchain install 1.86.0 1.89.0 nightly-2025-03-31 nightly-2025-08-24
