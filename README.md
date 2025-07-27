# Recommender System Implementation

## Overview
This repository contains a Python implementation of a collaborative filtering recommender system. The system uses a bipartite graph representation to model user-item interactions and provides multiple recommendation algorithms including collaborative filtering, item-based, and user-based approaches.

## Project Structure
- `recommender_graph.py`: Implements the bipartite graph data structure using hash tables (dictionaries) to efficiently manage user-item interactions with O(1) average time complexity for add/remove operations.
- `recommender_engine.py`: Contains the core recommendation algorithms and similarity calculations using Jaccard similarity metrics.
- `test_recommender.py`: Comprehensive test suite demonstrating system functionality with various scenarios including edge cases and larger datasets.

## Key Features

### Data Structure
- **Bipartite Graph**: Dual hash table implementation (`user_to_items` and `item_to_users`) for efficient bidirectional lookups
- **Memory Management**: Automatic cleanup of empty entries when interactions are removed
- **Statistics**: Built-in methods to track graph metrics (user count, item count, interaction count, averages)

### Recommendation Algorithms
1. **Collaborative Filtering**: Finds items liked by users who share similar preferences
2. **Item-Based**: Recommends items similar to those the user has already interacted with
3. **User-Based**: Identifies similar users and recommends their preferred items

### Similarity Metrics
- **Jaccard Similarity**: Used for both user-user and item-item similarity calculations
- **Priority Queue**: Efficient retrieval of top-N recommendations using heapq

## Setup & Running

### Requirements
- Python 3.x (no external dependencies required)

### Running the Test Suite
```bash
python test_recommender.py
```

### Basic Usage Example
```python
from recommender_graph import add_interaction
from recommender_engine import get_top_n_recommendations

# Add user-item interactions
add_interaction('Alice', 'Movie1')
add_interaction('Alice', 'Movie2')
add_interaction('Bob', 'Movie1')
add_interaction('Bob', 'Movie3')

# Get recommendations
recommendations = get_top_n_recommendations('Alice', 3, algorithm='collaborative_filtering')
print(recommendations)  # Returns list of (item, score) tuples
```

## API Reference

### Graph Operations (`recommender_graph.py`)
- `add_interaction(user, item)`: Add a user-item interaction
- `remove_interaction(user, item)`: Remove a user-item interaction
- `get_user_items(user)`: Get all items for a specific user
- `get_item_users(item)`: Get all users for a specific item
- `get_graph_stats()`: Get comprehensive graph statistics

### Recommendation Engine (`recommender_engine.py`)
- `get_top_n_recommendations(user, n, algorithm)`: Get top N recommendations using specified algorithm
- `get_recommendation_stats(user)`: Get detailed statistics about recommendations for a user
- Supported algorithms: `'collaborative_filtering'`, `'item_based'`, `'user_based'`

## Performance Characteristics
- **Time Complexity**: O(1) average for add/remove operations, O(k*m) for recommendations where k is user's items and m is average items per user
- **Space Complexity**: O(U + I + E) where U=users, I=items, E=interactions
- **Memory Efficient**: Automatic cleanup of empty entries

## Testing
The test suite includes:
- Basic recommendation functionality
- Edge cases (new users, single interactions)
- Large dataset scenarios
- Graph state visualization

## Limitations & Future Improvements
- **Current Limitations**: 
  - No rating system (binary interactions only)
  - No temporal dynamics
  - No content-based features
  - Single-threaded implementation

- **Planned Enhancements**:
  - Integration with vector similarity libraries (e.g., FAISS, Annoy)
  - Support for weighted interactions and ratings
  - Temporal decay factors
  - Distributed processing capabilities
  - Content-based filtering integration
