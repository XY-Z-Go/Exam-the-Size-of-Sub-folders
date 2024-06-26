def first_sub_folder(path):
    import os
    dir_path = path
    # print("dir_path", dir_path)
    files_dir = [folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))]
    sub_folders = [os.path.join(dir_path, f_dir) for f_dir in files_dir]
    # print("sub_folders", sub_folders)
    # print(sub_folders)
    x=0
    while x < len(sub_folders):
        size = 0
        for path, dirs, files in os.walk(str(sub_folders[x])):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
        print(sub_folders[x], str(size))
        x += 1

