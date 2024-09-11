from Set import Set
from random import random
import time
from progressbar import progressbar
import matplotlib.pyplot as plt


class SkilledTester:
    def __init__(self):
        pass

    def random_set(self, power, minimum, maximum, integer=False):
        set = Set()
        if integer and maximum - minimum < power:
            return -1

        multiply_by = maximum - minimum
        if integer:
            while len(set) <= power:
                set.insert(float(
                    int(random() * multiply_by + minimum)))  # float after int to ensure similar memory and/or time usage
        else:
            while len(set) < power:
                set.insert(random() * multiply_by + minimum)
        return set

    def simple_test_search_not_in_set_but_in_range(self, power, n_tests, results=None, t=None):
        total_time = 0
        start = 0
        end = 0
        for i in range(n_tests):
            set = self.random_set(power, 0, 1)
            element = random()

            start = time.time()
            set.search(element)
            end = time.time()

            total_time += (end - start) * 10 ** 6
        if results is None:
            return total_time / n_tests
        else:
            results[t] = total_time / n_tests

    def complex_test_search_not_in_set_but_in_range(self, powers, n_tests):
        av_time_list = [None] * len(powers)
        for i in progressbar(range(len(powers))):
            self.simple_test_search_not_in_set_but_in_range(powers[i], n_tests[i], results=av_time_list, t=i)
        return av_time_list

    def simple_test_search_in_set(self, power, n_tests, results=None, t=None):
        total_time = 0
        start = 0
        end = 0
        for i in range(n_tests):
            set = self.random_set(power, 0, power * 2, True)
            elements = set.to_list()
            element = elements[int(random() * len(elements))]

            start = time.time()
            set.search(element)
            end = time.time()

            total_time += (end - start) * 10 ** 6
        if results is None:
            return total_time / n_tests
        else:
            results[t] = total_time / n_tests

    def complex_test_search_in_set(self, powers, n_tests):
        av_time_list = [None] * len(powers)
        for i in progressbar(range(len(powers))):
            self.simple_test_search_in_set(powers[i], n_tests[i], results=av_time_list, t=i)
        return av_time_list

    def simple_union_test(self, powers, n_tests):
        av_time_map = []
        start = None
        end = None
        for a in progressbar(range(len(powers))):
            av_time_map.append([])
            for b in range(len(powers)):
                total_time = 0
                for i in range(n_tests):
                    set_a = self.random_set(powers[a], 0, (powers[a] + powers[b]) * 2, True)
                    set_b = self.random_set(powers[b], 0, (powers[a] + powers[b]) * 2, True)
                    start = time.time()
                    set_a.union(set_b)
                    end = time.time()
                    total_time += end - start
                av_time_map[a].append(total_time * 10 ** 6 / n_tests)
        return av_time_map


UncleFester = SkilledTester()
'''
powers = [i ** 2 for i in range(1, 20)]
n_tests = [int(1000000 / i) for i in powers]
plt.plot(powers, UncleFester.complex_test_search_not_in_set_but_in_range(powers, n_tests))
plt.show()

powers = [i ** 2 for i in range(1, 20)]
n_tests = [int(1000000 / i) for i in powers]
plt.plot(powers, UncleFester.complex_test_search_in_set(powers, n_tests))
plt.show()
'''

powers = [i ** 2 for i in range(1, 11)]
n_tests = 5000
fig, ax = plt.subplots()
result = UncleFester.simple_union_test(powers, n_tests)
im = ax.imshow(result)
ax.set_xticks(range(10), labels=powers)
ax.set_yticks(range(10), labels=powers)
for i in range(len(result)):
    for j in range(len(result)):
        text = ax.text(j, i, int(result[i][j] * 10) / 10,
                       ha="center", va="center", color="w")
plt.show()
print(result)
