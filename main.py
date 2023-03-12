# python3

# Deniss Dmitrijevs 221RDB322

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    thread_execution_times = []
    for i in range(n):
        thread_execution_times.append(0)

    output.append((0, 0))
    thread_execution_times[0] = data[0]

    for i in range(m)[1:]:
        #thread with least execution time
        n_min = 0
        for k in range(n)[1:]:
            if thread_execution_times[k] < thread_execution_times[n_min]:
                n_min = k
        output.append((n_min, thread_execution_times[n_min]))
        thread_execution_times[n_min] = thread_execution_times[n_min] + data[i]
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    (n, m) = tuple(map(int, input().split()))
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pair in result:
        print(str(pair[0]) + " " + str(pair[1]))



if __name__ == "__main__":
    main()
