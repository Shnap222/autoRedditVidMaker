import os


def check_dir_path(path: str):
    return os.path.isdir(path)


def mkdir(path: str):
    assert not check_dir_path(path), "This Dir Already Exists"

    os.mkdir(path)
