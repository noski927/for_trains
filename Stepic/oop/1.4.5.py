class Graph:
    LIMIT_Y = [0, 10]
    def set_data(self, data: list[int]):
        self.data = data
        
    def draw(self):
        a = [i for i in self.data if (min(self.LIMIT_Y)) <= i <= max(self.LIMIT_Y)]
        a = ' '.join(map(str,a))
        return a
        

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
print (graph_1.draw())