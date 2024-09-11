from Set import Set
from random import random
import time
from progressbar import progressbar
import matplotlib.pyplot as plt
import threading

class SkilledTester:
    def __init__(self):
        pass

    def random_set(self, power, minimum, maximum, integer = False):
        set = Set()
        if integer and maximum-minimum < power:
            return -1

        multiply_by = maximum-minimum
        if integer:
            while len(set) < power:
                set.insert(float(int(random() * multiply_by + minimum))) # float after int to ensure similar memory and/or time usage
        else:
            while len(set) < power:
                set.insert(random() * multiply_by + minimum)
        return set

    def simple_test_search_not_in_set_but_in_range(self, power, n_tests,results = None, i = None):
        total_time = 0
        start = 0
        end = 0
        for i in range(n_tests):
            set = self.random_set(power, 0, 1)
            element = random()

            start = time.time()
            set.search(element)
            end = time.time()

            total_time += end-start
        if results is None:
            return total_time/n_tests
        else:
            results[i] = total_time/n_tests

    def complex_test_search_not_in_set_but_in_range(self, powers, n_tests):
        av_time_list = [None]
        threads = []
        for i in range(len(powers)):
            threads.append(threading.Thread(target=self.simple_test_search_not_in_set_but_in_range, args=(self,powers[i],n_tests[i], av_time_list, i)))
            threads[i].start()
        for i in progressbar(range(len(threads))):
            threads[i].join()
        return av_time_list


UncleFester = SkilledTester()

powers = [i**2 for i in range(1,100)]
n_tests = [int(10**6/i) for i in powers]

plt.plot(powers, UncleFester.complex_test_search_not_in_set_but_in_range(powers,n_tests))
plt.show()






