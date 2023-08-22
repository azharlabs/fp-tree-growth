# FP-Tree Growth Algorithm
An efficient way to find frequent patterns in data!

## Overview
The FP-Tree Growth Algorithm provides a fast and efficient way to extract frequent patterns from datasets without generating tedious candidate sets. Rather than relying on the typical database scan approach, this algorithm constructs a special tree structure, aptly named the FP-Tree (Frequent Pattern Tree), to encapsulate all the essential information in the transaction database. The true magic lies in then extracting the most common patterns directly from this tree.

## Features
**Efficiency**: Reduces the need for repeated scans of the database.
**Compactness**: FP-Tree provides a compressed representation of the input data.
**Scalability**: Handles large datasets with ease.
**Flexible**: Suitable for a variety of data types and applications.

## How to Use
### Prerequisites
This implementation requires Python 3.x.

## Running the Algorithm
1. Import the FP-Tree Growth Algorithm functions.
1. Prepare your transaction dataset.
1. Decide on a minimum support threshold.
1. Call the **fp_growth** function and marvel at the frequent itemsets!

```python
from fp_tree_growth import fp_growth, convert_to_freq_dict

data_list = [['apple', 'banana', 'cherry'],
             ['apple', 'banana'],
             ['banana', 'cherry'],
             ['apple', 'cherry']]

data = convert_to_freq_dict(data_list)
min_support = 2
frequent_itemsets = fp_growth(data, min_support)
print(frequent_itemsets)
```

### Example
For a dataset of grocery transactions:

```python
data_list = [['eggs', 'bacon', 'soup'],
             ['eggs', 'bacon', 'apple'],
             ['eggs', 'soup', 'bacon', 'banana']]
```

The FP-Tree Growth Algorithm could reveal that eggs and bacon are often bought together (especially when you're planning a hearty breakfast!).

## Why Use FP-Tree Growth?
Traditional algorithms like Apriori can become increasingly slow and inefficient as datasets grow, due to the need to repeatedly scan the database and evaluate large candidate sets. FP-Tree Growth condenses the database into a compact tree structure, eliminating the need for these candidate sets and significantly speeding up the frequent pattern discovery process.

## Contributing
We welcome contributions! Please fork the repository and submit a pull request with your improvements.

## Acknowledgments
Thanks to all the data miners out there for their continuous research and innovations.
Special shoutout to coffee for fueling this project. ☕

Happy data mining! 🚀📊🌳
