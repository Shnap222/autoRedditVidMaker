import os


def check_dir_path(path: str):
    return os.path.isdir(path)


def mkdir(path: str):
    assert not check_dir_path(path), "This Dir Already Exists"

    os.mkdir(path)


def check_if_name_exists_in_dir(path: str, name: str, extension: str):
    files = os.listdir(path)

    file_full_name = f"{name}.{extension}"
    print(file_full_name in files)
    return file_full_name in files
