import time

if __name__ == "__main__":
    start = time.time()
    a = range(10000000)
    b = []
    for i in a:
        b.append(i*2)
    end = time.time()
    print("The script took", f"{end - start:.3f}", "seconds to complete")
