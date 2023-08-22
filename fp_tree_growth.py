# Define a class for nodes of the FP-Tree
class TreeNode:
    def __init__(self, item, count, parent):
        self.item = item          # Item name/label
        self.count = count        # Count of occurrences for this item in the path
        self.parent = parent      # Parent node in the tree
        self.children = {}        # Dictionary of children nodes
        self.link = None          # Link to the next node of the same item

# Function to insert transactions into the FP-Tree
def insert_tree(transaction, tree, header_table, count):
    # Check if the item exists as a child of the current node
    if transaction[0] in tree.children:
        # Increment the count if it does
        tree.children[transaction[0]].count += count
    else:
        # Otherwise, create a new child node for this item
        tree.children[transaction[0]] = TreeNode(transaction[0], count, tree)
        # Link this node to the header table
        if header_table[transaction[0]][1] is None:
            header_table[transaction[0]][1] = tree.children[transaction[0]]
        else:
            update_header(header_table[transaction[0]][1], tree.children[transaction[0]])
    # Recursively insert the remaining items of the transaction into the tree
    if len(transaction) > 1:
        insert_tree(transaction[1:], tree.children[transaction[0]], header_table, count)

# Update the link for nodes in the header table
def update_header(node, target_node):
    # Traverse the linked list until the last node
    while node.link is not None:
        node = node.link
    # Attach the target node at the end
    node.link = target_node

# Build the initial FP-Tree
def construct_fp_tree(data, min_support):
    item_counts = {}
    # Count the occurrences of each item in the dataset
    for transaction, count in data.items():
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + count
    # Filter out items that don't meet the minimum support
    item_counts = {k: v for k, v in item_counts.items() if v >= min_support}
    # Create the header table
    header_table = {item: [count, None] for item, count in item_counts.items()}
    # Initialize the root of the tree
    tree_root = TreeNode(None, 1, None)
    # Insert each transaction into the tree
    for transaction, count in data.items():
        # Sort items by frequency and filter
        sorted_items = [item for item in transaction if item in item_counts]
        sorted_items.sort(key=lambda x: item_counts[x], reverse=True)
        # Only insert non-empty transactions
        if len(sorted_items) > 0:
            insert_tree(sorted_items, tree_root, header_table, count)
    return tree_root, header_table

# Function to mine frequent patterns from the tree
def mine_tree(header_table, min_support, prefix, frequent_itemsets):
    # Sort items in the header table by count
    sorted_items = sorted(list(header_table.items()), key=lambda p: p[1][0])
    for item, (count, node) in sorted_items:
        # Extend the current prefix
        new_prefix = prefix.copy()
        new_prefix.add(item)
        # Save the current frequent itemset
        frequent_itemsets[tuple(sorted(new_prefix))] = count
        # Construct conditional pattern base for the current item
        conditional_pattern_base = find_conditional_pattern_base(node)
        conditional_tree_data = {}
        for pattern, count in conditional_pattern_base:
            conditional_tree_data[pattern] = count
        # Build a conditional FP-tree for the item
        conditional_tree_root, conditional_header_table = construct_fp_tree(conditional_tree_data, min_support)
        # If there are items in the conditional header table, mine recursively
        if conditional_header_table:
            mine_tree(conditional_header_table, min_support, new_prefix, frequent_itemsets)

# Find the conditional pattern base for a node/item
def find_conditional_pattern_base(node):
    patterns = []
    # For each node of the same item
    while node is not None:
        # Get the path leading to this node
        prefix_path = ascend_tree(node)
        # If the path is not empty, add it to the patterns
        if len(prefix_path) > 1:
            patterns.append((tuple(prefix_path[1:]), node.count))
        node = node.link
    return patterns

# Ascend the tree from a node to the root and get the path
def ascend_tree(node):
    path = []
    while node and node.parent:  # Exclude the root
        path.append(node.item)
        node = node.parent
    return path

# Main FP-Growth algorithm
def fp_growth(data, min_support):
    # Build the initial FP-Tree
    tree, header_table = construct_fp_tree(data, min_support)
    frequent_itemsets = {}
    # Mine the FP-Tree
    mine_tree(header_table, min_support, set(), frequent_itemsets)
    return frequent_itemsets

# Convert a list of transactions to a frequency dictionary
def convert_to_freq_dict(transactions):
    freq_dict = {}
    for transaction in transactions:
        transaction_tuple = tuple(sorted(transaction))
        freq_dict[transaction_tuple] = freq_dict.get(transaction_tuple, 0) + 1
    return freq_dict
