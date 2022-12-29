import os
import concurrent.futures
import time
start=time.perf_counter()
def find_files(filename, search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result
Drives=["C:","E:","F:"]
input_file='Test_1.txt'
with concurrent.futures.ThreadPoolExecutor() as executor:

    results=[executor.submit(find_files,input_file,drive) for drive in Drives]
    finish = time.perf_counter()

    for r in concurrent.futures.as_completed(results):
        print(r.result())
       # print(find_files("maintextdocument")
finish = time.perf_counter()
print(f'Finish in {finish - start}seconds')
