def third_sub_folder(path):

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
    sub_sub_sub_folder_trun=[]
    while y < len(sub_sub_folder_trun):
        sub_sub_files_dir = [folder for folder in os.listdir(sub_sub_folder_trun[y]) if os.path.isdir(os.path.join(sub_sub_folder_trun[y], folder) )]
        sub_sub_sub_folder = [os.path.join(sub_sub_folder_trun[y], f_dir) for f_dir in sub_sub_files_dir]
        if len(sub_sub_sub_folder) != 0:
            sub_sub_sub_folder_trun += sub_sub_sub_folder
        y += 1

    z=0
    path_list=[]
    size_list=[]
    data={}

    while z < len(sub_sub_sub_folder_trun):
        size = 0
        for path, dirs, files in os.walk(str(sub_sub_sub_folder_trun[z])):
            for f in files:
                fp = os.path.join(path, f)
        size += os.path.getsize(fp)
        path_list += [sub_sub_sub_folder_trun[z]]
        size_list += [size]
        print(sub_sub_sub_folder_trun[z], size)
        z += 1
    # data = {'path': path_list, 'size': size_list}
    # print(data)

