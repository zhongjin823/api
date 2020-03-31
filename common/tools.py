import os


def root_dir():

    root_path = os.path.dirname(__file__)

    while True:
        md_file = os.path.join(root_path, 'readme.md')
        if os.path.exists(md_file):
            break
        root_path = os.path.dirname(root_path)
    return root_path


if __name__ == '__main__':
    root_path = root_dir()
    print(root_path)