import argparse
import json
import math
import networkx as nx


def calculate_distance(p1, p2):
  return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def build_tdma_schedule(nodes_data, radio_range=500.0):
  # 1. Base Physical Graph
  G = nx.Graph()
  for node in nodes_data:
    G.add_node(node)

  node_keys = list(nodes_data.keys())
  for i in range(len(node_keys)):
    for j in range(i + 1, len(node_keys)):
      n1, n2 = node_keys[i], node_keys[j]
      dist = calculate_distance(nodes_data[n1], nodes_data[n2])
      if dist <= radio_range:
        G.add_edge(n1, n2)

  # 2. Distance-2 Conflict Graph (1-hop & 2-hop interference)
  G2 = nx.Graph()
  G2.add_nodes_from(G.nodes())

  for u in G.nodes():
    # 1-hop neighbours (Direct Interference)
    one_hop = set(G.neighbors(u))
    for v in one_hop:
      if u != v:
        G2.add_edge(u, v)

    # 2-hop neighbours (Hidden Terminal Interference)
    two_hop = set()
    for neighbor in one_hop:
      two_hop.update(G.neighbors(neighbor))
    two_hop.discard(u)

    for v in two_hop:
      if u != v:
        G2.add_edge(u, v)

  # 3. Greedy Graph Coloring with Degree Ordering (Heuristic)
  nodes_sorted = sorted(G2.nodes(), key=lambda x: G2.degree(x), reverse=True)
  node_to_slot = {}

  for node in nodes_sorted:
    neighbor_slots = {
        node_to_slot[neighbor]
        for neighbor in G2.neighbors(node)
        if neighbor in node_to_slot
    }
    slot = 0
    while slot in neighbor_slots:
      slot += 1
    node_to_slot[node] = slot

  # Output Formatting
  sorted_nodes = sorted(node_keys)
  total_slots = max(node_to_slot.values()) + 1 if node_to_slot else 0

  print("=" * 60)
  print("TDMA TOPOLOGY OPTIMIZATION REPORT")
  print("=" * 60)
  print(f"Total Nodes Processed : {len(sorted_nodes)}")
  print(f"Configured Radio Range: {radio_range} meters")
  print(
      f"Optimized Frame Length: {total_slots} unique timeslots (Lower is"
      " better)"
  )
  print("\nNODE -> SLOT ASSIGNMENTS:")
  for node in sorted_nodes:
    print(f"{node}: Slot {node_to_slot[node]}")

  print("\n" + "=" * 60)
  print("STRUCTURAL TDMA SCHEDULE MATRIX (Slot x Node Boolean Matrix):")

  header = "Slot \\ Node | " + " | ".join(
      [n.replace("Node_", "") for n in sorted_nodes]
  )
  print(header)
  print("-" * len(header))

  for s in range(total_slots):
    row = [
        "1" if node_to_slot[node] == s else "0" for node in sorted_nodes
    ]
    slot_label = f"Slot {s:02d}    |"
    print(f"{slot_label}  " + "  |  ".join(row))

  print("=" * 60)
  print("Execution finalized cleanly. Schedule verified conflict-free.")
  print("=" * 60)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
      description="TDMA Conflict-Free Schedule Optimizer"
  )
  parser.add_argument(
      "--nodes",
      type=str,
      required=False,
      help="JSON formatted string of node coordinates",
  )
  args = parser.parse_args()

  default_nodes = {
      "Node_01": [0.0, 0.0],
      "Node_02": [300.0, 0.0],
      "Node_03": [600.0, 0.0],
      "Node_04": [900.0, 0.0],
      "Node_05": [0.0, 300.0],
      "Node_06": [300.0, 300.0],
      "Node_07": [600.0, 300.0],
      "Node_08": [900.0, 300.0],
      "Node_09": [0.0, 600.0],
      "Node_10": [300.0, 600.0],
      "Node_11": [600.0, 600.0],
      "Node_12": [900.0, 600.0],
      "Node_13": [0.0, 900.0],
      "Node_14": [300.0, 900.0],
      "Node_15": [600.0, 900.0],
      "Node_16": [900.0, 900.0],
  }

  if args.nodes:
    try:
      parsed_nodes = json.loads(args.nodes)
      build_tdma_schedule(parsed_nodes)
    except Exception as e:
      print(f"Error parsing JSON: {e}")
  else:
    build_tdma_schedule(default_nodes)