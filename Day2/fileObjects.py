# f = open('text.txt', 'r')

# print(f.name)


# with open('text.txt','r') as f:
#     f_content = f.read()
#     print(f_content)


# with open('text.txt','r') as f:
#     f_content = f.readline()
#     print(f_content, end='')

#     f_content = f.readline()
#     print(f_content, end='')

# with open('text.txt','r') as f:

#     for line in f:
#         print(line, end='')


with open('text.txt','r') as f:
    size_to_read = 10
    f_content = f.read(size_to_read)

    while len(f_content) >0:
        print(f_content, end='#') # remove #
        f_content = f.read(size_to_read)


# with open('text.txt', 'w') as rf:
#     pass


with open('text.txt', 'r') as rf:
    with open('text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)






