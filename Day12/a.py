class path_processor:
    connections = []
    edges = {}
    routes = []

    def generate_net(self, pos):
        for connection in self.connections:
            if connection[0] not in self.edges:
                self.edges[connection[0]] = set()
            if connection[1] not in self.edges:
                self.edges[connection[1]] = set()
            self.edges[connection[0]].add(connection[1])
            self.edges[connection[1]].add(connection[0])

    def find_route(self, current_vertex, path):
        if(current_vertex == 'end'):
            current_path = [i for i in path]
            current_path.append(current_vertex)
            self.routes.append(current_path)
            return
        elif current_vertex.islower() and (current_vertex in path):
            return
        else:
            path.append(current_vertex)
            for neighbour in self.edges[current_vertex]:
                current_path = [i for i in path]
                self.find_route(neighbour, current_path)
            

def main(inp):
    pp = path_processor()
    for line in inp:
        b = line.strip().split('-')
        pp.connections.append((b[0],b[1]))
    for con in pp.connections:
        pp.generate_net(con)
    pp.find_route('start', [])
    print(len(pp.routes))

if __name__ == "__main__":
    import os 
    with open("Day12/input.txt",'r',newline='\n') as inp:
        main(inp)