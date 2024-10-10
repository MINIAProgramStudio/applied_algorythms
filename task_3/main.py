import RandomGraph
import GraphAlgorythm
import time
import matplotlib.pyplot as plt

def test_matrixes(ver_range, p_percent_range, tests):
    graphs = []
    for ver in ver_range:
        graphs.append([])
        for p in p_percent_range:
            graphs[-1].append([])
            for t in range(tests):
                graph = RandomGraph.RandomGraph(ver, p/100)
                for i in range(len(graph.matrix)):
                    graph.matrix[i][i] = True
                graphs[-1][-1].append(graph)

    dfs_map = []
    w_map = []
    for row in graphs:
        dfs_map.append([])
        w_map.append([])
        for column in row:
            dfs_time = 0
            w_time = 0
            for test in column:
                lists = test.to_ll()
                dfs_start = time.time()
                GraphAlgorythm.recursive_dfs_starter(lists)
                dfs_end = time.time()
                dfs_time += dfs_end-dfs_start

                w_start = time.time()
                GraphAlgorythm.warshall_starter(test)
                w_end = time.time()
                w_time += w_end - w_start
            dfs_map[-1].append(dfs_time/tests)
            w_map[-1].append(w_time/tests)
    return (dfs_map, w_map)

ver = range(5,25)
p = range(10,101,10)
result = test_matrixes(ver, p, 10)

fig, ax = plt.subplots()

im = ax.imshow(result[0])
ax.set_xlabel("probability")
ax.set_xticks(range(len(list(p))), labels=p)
ax.set_yticks(range(len(list(ver))), labels=ver)
ax.set_ylabel("vertices")
for i in range(len(result[0])):
    for j in range(len(result[0][0])):
        text = ax.text(j, i, int(result[0][i][j] * 10**7) / 10, ha="center", va="center", color="w")
plt.show()