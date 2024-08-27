#!/usr/bin/env python3

import pathlib
import subprocess
import sys

def find_repository_root(pwd):
    p = pwd

    while True:
        if p.joinpath("Cargo.toml").is_file() and p.joinpath("src").is_dir():
            return p

        parent = p.parent
        if p == parent:
            print(f"can't find root of repository", file=sys.stderr)
            sys.exit(1)

        p = parent

pwd = pathlib.Path().absolute()
reporoot = find_repository_root(pwd)

subprocess.run(["podman", "run",
                "--interactive",
                "--mount", f"type=bind,src={reporoot},dst={reporoot}",
                "--tty",
                "--userns", "keep-id",
                "rustdev",
                "/bin/bash", "-l", "-c",
                f"cd {pwd}; cargo {" ".join(sys.argv[1:])}"])
