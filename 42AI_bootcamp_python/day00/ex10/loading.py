import sys
import time


def ft_progress(lst):
    bar_width = 40
    count = len(lst)
    st_time = time.time()

    def show(j):
        x = int(bar_width*j/count)
        sys.stdout.write("[%s>%s] %i/%i | elapsed time %.2fs\r"
                         % ("="*x, " "*(bar_width - x - 1),
                             j, count, time.time() - st_time))
        sys.stdout.flush()
    show(0)
    for i in lst:
        yield i
        show(i + 1)
    sys.stdout.write("\n")
    sys.stdout.flush()


listy = range(300)
ret = 0
time_interval = 0.01   # 1ms

for elem in ft_progress(listy):
    sys.stdout.write("ETA : %.2fs " % (len(listy)*time_interval))
    sys.stdout.flush()
    ret += (elem + 3) % 5
    time.sleep(time_interval)
print("...")
print(ret)
