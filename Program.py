import os


path =(input('please in put the path: '))
print(path)
# path = repr(path)[1:-1]

x = input ('which class of sub-folder you need? (1st, 2nd, 3rd): ')

if x == '1st':
    import function.first_sub_folder as fsf
    fsf.first_sub_folder(path)

elif x == '2nd':
    import function.second_sub_folder as ssf
    ssf.second_sub_folder(path)

elif x == '3rd':
    import function.third_sub_folder as tsf
    tsf.third_sub_folder(path)