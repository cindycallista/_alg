def path_cost(path):
    return sum(abs(path[i] - path[i+1]) for i in range(len(path)-1))

def improvement_method(path):
    improved = True
    while improved:
        improved = False
        for i in range(len(path)-1):
            new_path = path[:]
            new_path[i], new_path[i+1] = new_path[i+1], new_path[i]  # swap

            if path_cost(new_path) < path_cost(path):
                path = new_path
                improved = True
    return path, path_cost(path)

if __name__ == "__main__":
    best_path, cost = improvement_method([5, 2, 8, 1, 7])
    print("Improved path:", best_path)
    print("Cost:", cost)
