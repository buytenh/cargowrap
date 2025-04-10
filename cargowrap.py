#!/usr/bin/env python3

import pathlib
import subprocess
import sys

def find_mount_root(pwd):
    p = pwd

    while True:
        if p.joinpath("Cargo.toml").is_file() and p.joinpath("src").is_dir():
            return p

        parent = p.parent
        if p == parent:
            return pwd

        p = parent

pwd = pathlib.Path().absolute()
mount_root = find_mount_root(pwd)

subprocess.run(["podman", "run",
                "--env", "RUST_LOG",
                "--interactive",
                "--mount", f"type=bind,src={mount_root},dst={mount_root}",
                "--mount", "type=volume,src=cargo-git,dst=/home/buytenh/.cargo/git",
                "--mount", "type=volume,src=cargo-registry,dst=/home/buytenh/.cargo/registry",
                "--tty",
                "--userns", "keep-id",
                "rustdev",
                "/bin/bash", "-l", "-c",
                f"cd {pwd}; cargo {" ".join(sys.argv[1:])}"])
