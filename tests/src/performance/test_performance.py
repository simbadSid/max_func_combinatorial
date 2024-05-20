import time
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from src.utils.utils import project_file_path
from src.main.s_max import Smax


OUTPUT_FILE = 'tests/output/performance/performance.png'
K_LIST      = [2, 3, 4, 5, 6, 7, 8, 9]
M_LIST      = [10]


if __name__ == '__main__':
    s_max = Smax()

    # Dictionary to store execution times for each value of m
    execution_times = {m: [] for m in M_LIST}

    # Run f for all values of k and m
    for m in M_LIST:
        for k in K_LIST:
            print(f'k={k}, m={m}')
            s_max.set_random_input(k, m)
            start_time = time.time()
            _ = s_max.find_max()
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times[m].append(execution_time)

    # Plot the execution times
    for m, times in execution_times.items():
        plt.plot(K_LIST, times, label=f'm={m}')

    plt.xlabel('k')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs. k for Different Values of m')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.yscale('log')

    plt.show()
    plt.savefig(project_file_path(OUTPUT_FILE))