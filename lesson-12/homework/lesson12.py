import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    for number in range(start, end):
        if is_prime(number):
            result.append(number)

def threaded_prime_checker(start, end, thread_count=4):
    step = (end - start) // thread_count
    threads = []
    results = [[] for _ in range(thread_count)]

    for i in range(thread_count):
        thread_start = start + i * step
        thread_end = start + (i + 1) * step if i < thread_count - 1 else end
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, results[i]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    primes = [num for sublist in results for num in sublist]
    print("Prime numbers found:", sorted(primes))

# Example usage
threaded_prime_checker(1, 100)
import threading
from collections import Counter
import os

def process_lines(lines, counter):
    local_counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        local_counter.update(words)
    counter.append(local_counter)

def threaded_word_count(file_path, thread_count=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    step = total_lines // thread_count
    threads = []
    counters = []

    for i in range(thread_count):
        start = i * step
        end = (i + 1) * step if i < thread_count - 1 else total_lines
        part = lines[start:end]
        counter = []
        thread = threading.Thread(target=process_lines, args=(part, counter))
        threads.append(thread)
        counters.append(counter)
        thread.start()

    for thread in threads:
        thread.join()

    final_counter = Counter()
    for counter in counters:
        final_counter.update(counter[0])

    print("Word occurrences:")
    for word, count in final_counter.most_common(10):  # Show top 10 words
        print(f"{word}: {count}")

# Example usage (make sure to provide a valid text file)
# threaded_word_count("large_text_file.txt")
