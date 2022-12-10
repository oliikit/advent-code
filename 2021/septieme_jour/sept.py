import re

with open("commands.txt", "r") as f:
    commands = f.read().splitlines()
    cwd = ''
    old_cwd = []
    added_dirs = []
    file_size = {}

    for i, command in enumerate(commands):
        j = i

        # keeps track of cwd
        if "$ cd" in command:
            if command[5] != '.':
                old_cwd.append(cwd)
                cwd += command[5:] + '/'
                # adds the directory to the file_size dict
                if cwd not in file_size:
                    dict.setdefault(file_size, cwd, 0)
            else:
                cwd = old_cwd[-1]
                old_cwd.pop()
            # print(f'{i} cwd: {cwd}')

        # finds all the directories
        if "$ ls" in command:
            # print(f'{j} {commands[j]}')
            j = i + 1 # go to ls results
            while True:
                # extracts the file size
                if 'dir' not in commands[j] and cwd not in added_dirs:
                    size = re.findall('\d+', commands[j])
                    file_size[cwd] += int(size[0])

                j += 1 # next line in ls result
                if j >= len(commands):
                    added_dirs.append(cwd)
                    break
                elif '$' in commands[j]:
                    added_dirs.append(cwd)
                    i = j
                    break

    # add all dirs together
    for file in sorted(file_size):
        match = dict(filter(lambda item: file in item[0], file_size.items()))
        # print(f'{file}: {match} \n')
        if len(match) > 1:
            for k, v in match.items():
                file_size[file] += v

    # create dictionary of files with size < 100000
    min_size = {k: v for k, v in file_size.items() if v < 100000}
    total_size = 0

    for file in sorted(min_size, reverse=True):
        total_size += min_size[file] # this is a bottom file so gets added


    system_space = 70000000
    needed_space = 30000000
    search_space = system_space - needed_space
    used_space = sum(file_size.values())
    del_val = system_space

    # find the smallest file that can be deleted
    for file in sorted(file_size):
        print(used_space - file_size[file])

        if (used_space - file_size[file]) <= search_space and file_size[file] < del_val:
            print(file_size[file])
            del_val = file_size[file]

    print(f'Total size: {total_size}')
    print(f'File to delete: {del_val}')
    