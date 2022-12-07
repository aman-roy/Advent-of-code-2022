from aocd import lines
import os
import glob

# rather than implementing the logic, just run the command as normal linux command
oldpwd = os.getcwd()
os.system('mkdir aman')

for l in lines:
    l = l.strip().replace("$ ", "").replace("/", 'aman')
    if l.startswith("cd"):
        os.chdir(l[3:])
    elif l.startswith('ls'):
        continue
    elif l.startswith('dir '):
        os.system('mkdir ' + l[4:])
    else:
        size, file = l.split()
        os.system(f"fallocate -l {size} {file}")

os.chdir(oldpwd)


# get size of any folder
def get_size(start_path='.'):
    total_size = 0
    for dirpath, _, filenames in os.walk(start_path):
        for f in filenames:
            total_size += os.path.getsize(os.path.join(dirpath, f))
    return total_size


print(sum([get_size(x) for x in glob.iglob("aman" + '**/**', recursive=True) if
           os.path.isdir(x) and get_size(x) <= 100000]))
