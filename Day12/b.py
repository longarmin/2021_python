class path_processor:
    connections = []
    edges = {}
    routes = []
    path_contains_small_vertex_twice = False

    def generate_net(self, pos):
        for connection in self.connections:
            if connection[0] not in self.edges:
                self.edges[connection[0]] = set()
            if connection[1] not in self.edges:
                self.edges[connection[1]] = set()
            self.edges[connection[0]].add(connection[1])
            self.edges[connection[1]].add(connection[0])
            
    def check_second_twice(self, current_vertex, path, twice):
        if current_vertex == 'start':
            return current_vertex in path
        return (twice and current_vertex.islower() and (current_vertex in path))
    def check_twice(self, path, twice):
        if twice:
            return True
        else:
            vertices=set()
            for vertex in path:
                if vertex.islower():
                    if twice:
                        return True
                    elif vertex in vertices:
                        twice = True
                    else:
                        vertices.add(vertex)
            return twice

    def find_route(self, current_vertex, path, twice):
        if(current_vertex == 'end'):
            current_path = [i for i in path]
            current_path.append(current_vertex)
            self.routes.append(current_path)
            return
        if self.check_second_twice(current_vertex, path, twice):
            return
        else:
            path.append(current_vertex)
            twice = self.check_twice(path, twice)
            for neighbour in self.edges[current_vertex]:
                current_path = [i for i in path]
                self.find_route(neighbour, current_path, twice)
            

def main(inp):
    pp = path_processor()
    for line in inp:
        b = line.strip().split('-')
        pp.connections.append((b[0],b[1]))
    for con in pp.connections:
        pp.generate_net(con)
    pp.find_route('start', [], False)
    print(len(pp.routes))

if __name__ == "__main__":
    import os 
    with open("Day12/input.txt",'r',newline='\n') as inp:
        main(inp)