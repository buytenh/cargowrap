FROM fedora:44
RUN dnf -y upgrade
RUN dnf -y install gcc iverilog openssl-devel
RUN useradd -s /bin/bash buytenh
USER buytenh
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN /home/buytenh/.cargo/bin/rustup toolchain install 1.92.0 1.94.0 nightly-2025-03-31 nightly-2025-08-24 nightly-2025-12-29 nightly-2026-03-05
RUN /home/buytenh/.cargo/bin/cargo install cargo-audit --locked --features=fix
