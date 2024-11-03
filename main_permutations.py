from permutation import find_all_hamiltonian_cycles
from graph_data import graph_data
import global_game_data

def main():
        for i in range(len(graph_data)):
               global_game_data.current_graph_index = i
               print(f"processing graph index: {i}")
               cycles = find_all_hamiltonian_cycles(graph_data[i])
               if cycles != -1:
                      print(f"Cycles in graph {i}: {cycles}")

if __name__ == "__main__":
    main()