def second_sub_folder(path):
    import os

    dir_path = path
    files_dir = [ folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))]
    sub_folders = [os.path.join(dir_path, f_dir) for f_dir in files_dir]

    x=0
    sub_sub_folder_trun=[]
    while x < len(sub_folders):
        sub_files_dir = [folder for folder in os.listdir(sub_folders[x]) if os.path.isdir(os.path.join(sub_folders[x], folder) )]
        sub_sub_folder = [os.path.join(sub_folders[x], f_dir) for f_dir in sub_files_dir]
        if len(sub_sub_folder) != 0:
            sub_sub_folder_trun += sub_sub_folder
        x += 1

    y=0
    while y < len(sub_sub_folder_trun):
        size = 0
        for path, dirs, files in os.walk(str(sub_sub_folder_trun[y])):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
        print(sub_sub_folder_trun[y], str(size))
        y += 1
