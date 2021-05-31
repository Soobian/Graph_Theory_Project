import json
from ford_fulkerson import Graph

if __name__ == '__main__':
    path = "test_data.json"
    with open(path) as json_file:
        data = json.load(json_file)
        x = Graph(data)
        if x.is_list():
            x.graph = x.list_to_matrix()

        print(x.graph)
        print('Result: ', x.FordFulkerson(0, 5))
