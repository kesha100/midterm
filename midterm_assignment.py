import networkx as nx
import matplotlib.pyplot as plt  # For visualization (optional)

# Создаем пустой направленный граф с помощью NetworkX.

G = nx.DiGraph()

# Определение узлов ввода:
input_0 = 0
input_1 = 1

# Определение логических ворот:
def or_gate(inputs):
    return inputs[0] or inputs[1]

def not_gate(input):
    return not input

# Добавление узлов в граф:
G.add_node("Input 0", value=input_0)
G.add_node("Input 1", value=input_1)
G.add_node("OR Gate", function=or_gate)
G.add_node("NOT Gate", function=not_gate)

# Создание связей между узлами:
G.add_edge("Input 0", "OR Gate")
G.add_edge("Input 1", "OR Gate")
G.add_edge("OR Gate", "NOT Gate")

# Мы выполняем обход графа в топологическом порядке и вычисляем значения узлов на основе их входов и функций.
for node in nx.topological_sort(G):
    if "value" in G.nodes[node]:
        continue  # Skip input nodes
    inputs = [G.nodes[predecessor]["value"] for predecessor in G.predecessors(node)]
    G.nodes[node]["value"] = G.nodes[node]["function"](inputs)

# Вывод результата и визуализация графа
result = G.nodes["NOT Gate"]["value"]
print("Result:", result)

# Визуализация графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue')
plt.show()
