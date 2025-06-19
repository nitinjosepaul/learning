import tracemalloc

def find_line_number(mode='READLINES'):
    file1 = open("Bigfile.txt",'r')
    if mode == 'READLINES':
        lines = file1.readlines()
        print(len(lines))
    elif mode == 'READLINE':
        count = 0
        while True:
            line = file1.readline()
            if not line:
                print(count)
                break
            count += 1
    elif mode == 'FORLOOP':
        count = 0
        for _ in file1:
            count += 1
        print(count)
    file1.close()


tracemalloc.start()
find_line_number('FORLOOP')
print(tracemalloc.get_traced_memory())
tracemalloc.stop()