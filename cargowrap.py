#!/usr/bin/env python3

import pathlib
import subprocess
import sys

def find_mount_root(pwd):
    mount_root = pwd

    while True:
        if mount_root.joinpath("Cargo.toml").is_file() and mount_root.joinpath("src").is_dir():
            return mount_root

        parent = mount_root.parent
        if mount_root == parent:
            return pwd

        mount_root = parent

pwd = pathlib.Path().absolute()
mount_root = find_mount_root(pwd)

subprocess.run(["podman", "run",
                "--env", "RUST_BACKTRACE",
                "--env", "RUST_LOG",
                "--env", "RUSTFLAGS",
                "--interactive",
                "--mount", "type=volume,src=cargo-git,dst=/home/buytenh/.cargo/git",
                "--mount", "type=volume,src=cargo-registry,dst=/home/buytenh/.cargo/registry",
                "--mount", f"type=bind,src={mount_root},dst={mount_root}",
                "--tty",
                "--userns", "keep-id",
                "rustdev",
                "/bin/bash", "-l", "-c",
                f"cd {pwd}; cargo {" ".join(sys.argv[1:])}"])
