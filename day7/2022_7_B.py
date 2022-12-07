import glob
import os


# get size of any folder
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, _, filenames in os.walk(start_path):
        for f in filenames:
            total_size += os.path.getsize(os.path.join(dirpath, f))
    return total_size

need_to_delete = get_size('aman') - (70000000 - 30000000)
print(sorted(f for f in [get_size(x) for x in glob.iglob("aman" + '**/**', recursive=True) if os.path.isdir(x)] if f>= need_to_delete)[0])











