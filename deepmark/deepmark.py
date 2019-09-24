import sys

from time import clock_gettime
from benchmarks import mnist, mnist_data
from benchmarks import simple_lstm, simple_lstm_data
from benchmarks import simple_mlp, simple_mlp_data

import pandas as pd

def round_end(results, out, start, test_name):
    
    out.insert(0, test_name)
    out.insert(1, start)
    out.insert(2, clock_gettime(1))
    
    return out

def run_tests(env=None, cpu_clock=None, gpu=None, modes=None):

    results = []

    batch_sizes = [1024, 512, 256, 128, 64, 32, 16, 8]
    system_details = env + '_' + cpu_clock + '_' + gpu
    
    model_name = 'simple_mlp'
    test_name = model_name + '_' + system_details
    for mode in modes:
        for batch_size in batch_sizes:
            start = clock_gettime(1)
            out = simple_mlp(simple_mlp_data(), batch_size=batch_size, resource_mode=mode)
            results.append(round_end(results, out, start, test_name))


    model_name = 'mnist' 
    test_name = model_name + '_' + system_details
    for mode in modes:
        for batch_size in batch_sizes:
            start = clock_gettime(1)
            out = mnist(mnist_data(), batch_size=batch_size, resource_mode=mode)
            results.append(round_end(results, out, start, test_name))

    model_name = 'simple_lstm'
    test_name = model_name + '_' + system_details
    for mode in modes:
        for batch_size in batch_sizes:

            start = clock_gettime(1)
            out = simple_lstm(simple_lstm_data(), batch_size=batch_size, resource_mode=mode, cudnn=False)
            results.append(round_end(results, out, start, test_name))

    model_name = 'simple_cudnnlstm'
    test_name = model_name + '_' + system_details

    try:
        modes.remove('cpu')
    except ValueError:
        pass
    for mode in modes:
        for batch_size in batch_sizes:
            start = clock_gettime(1)
            out = simple_lstm(simple_lstm_data(), batch_size=batch_size, resource_mode=mode, cudnn=True)
            results.append(round_end(results, out, start, test_name))
            
    return results, test_name

def save_results(results, test_name):

    data = pd.DataFrame(results)
    data.columns = ['test', 'start', 'end', 'seconds', 'mode', 'batch_size']
    data.to_csv(test_name)
    
if __name__ == '__main__':

    print("hello")
    env = sys.argv[1]
    cpu_clock = sys.argv[2]
    gpu = sys.argv[3]
    try:
    	modes = sys.argv[4]
    except ValueError:
        modes = 'gpu,cpu,multi_gpu,parallel_gpu'

    modes = modes.split(',')    

    results, test_name = run_tests(env, cpu_clock, gpu, modes)
    test_name = test_name.replace('simple_cudnnlstm_', '')
    save_results(results, test_name)
    
    print('Benchmarking Completed!')

