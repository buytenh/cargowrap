#!/usr/bin/env python3

import pathlib
import subprocess
import sys

# Find the grandest parent directory that contains a Cargo.toml file.
def find_mount_root(pwd):
    dir = pwd

    mount_root = dir

    while True:
        if dir.joinpath("Cargo.toml").is_file():
            mount_root = dir

        parent = dir.parent
        if dir == parent:
            break

        dir = parent

    return mount_root

pwd = pathlib.Path().absolute()
mount_root = find_mount_root(pwd)

subprocess.run(["podman", "run",
                "--env", "RUST_BACKTRACE",
                "--env", "RUST_LOG",
                "--env", "RUSTFLAGS",
                "--interactive",
                "--mount", "type=volume,src=cargo,dst=/home/buytenh/.cargo",
                "--mount", f"type=bind,src={mount_root},dst={mount_root}",
                "--tty",
                "--userns", "keep-id",
                "rustdev",
                "/bin/bash", "-l", "-c",
                f"cd {pwd}; cargo {" ".join(sys.argv[1:])}"])
