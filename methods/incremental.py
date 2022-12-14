import os
import shutil


def incremental_rename(src, des):
    """
    :param src: Path
    :param des: Path
    """
    i = 1
    print(":: Incrementally Renaming Files ::")
    for filename in os.listdir(src):
        ext = os.path.splitext(filename)[1]
        new_name = str(i) + ext
        print(":: file: " + src + "/" + filename + " will be renamed to " + des + "/" + new_name + " ::")
        shutil.copyfile(src + "/" + filename, des + "/" + new_name)
        i += 1

    return ":: Done ::"


def incremental_with_extra(src, des, extra, key):
    """
    :param extra:
    :param key: boolean
    :param src: Path
    :param des: Path
    """
    i = 1
    print(":: Incrementally Renaming Files With Prefix/Suffix ::")
    for filename in os.listdir(src):
        ext = os.path.splitext(filename)[1]
        if key == 1:
            new_name = extra + "_" + str(i) + ext
        else:
            new_name = str(i) + "_" + extra + ext

        print(":: file: " + src + "/" + filename + " will be renamed to " + des + "/" + new_name + " ::")
        shutil.copyfile(src + "/" + filename, des + "/" + new_name)
        i += 1
    return ":: Done ::"
