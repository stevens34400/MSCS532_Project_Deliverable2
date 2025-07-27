from recommender_graph import add_interaction, remove_interaction, user_to_items, item_to_users
from recommender_engine import get_top_n_recommendations

def clear_data():
    """Clear all interaction data for testing"""
    user_to_items.clear()
    item_to_users.clear()

def test_basic_recommendations():
    """Test basic recommendation functionality"""
    print("=== Basic Recommendation Test ===")
    clear_data()
    
    # Setup interactions
    add_interaction('Alice', 'Item1')
    add_interaction('Bob', 'Item2')
    add_interaction('Alice', 'Item2')
    add_interaction('Charlie', 'Item1')
    add_interaction('Charlie', 'Item3')
    add_interaction('David', 'Item2')
    add_interaction('David', 'Item3')
    
    # Generate recommendations
    recommendations = get_top_n_recommendations('Alice', 3)
    print(f"Recommendations for Alice: {recommendations}")
    
    # Test recommendations for other users
    recommendations = get_top_n_recommendations('Bob', 2)
    print(f"Recommendations for Bob: {recommendations}")
    
    recommendations = get_top_n_recommendations('Charlie', 2)
    print(f"Recommendations for Charlie: {recommendations}")

def test_edge_cases():
    """Test edge cases and error handling"""
    print("\n=== Edge Cases Test ===")
    clear_data()
    
    # Test user with no interactions
    recommendations = get_top_n_recommendations('NewUser', 2)
    print(f"Recommendations for new user: {recommendations}")
    
    # Test user with only one item
    add_interaction('LonelyUser', 'Item1')
    recommendations = get_top_n_recommendations('LonelyUser', 2)
    print(f"Recommendations for lonely user: {recommendations}")
    
    # Test removal of interactions
    add_interaction('TestUser', 'Item1')
    add_interaction('TestUser', 'Item2')
    remove_interaction('TestUser', 'Item1')
    recommendations = get_top_n_recommendations('TestUser', 2)
    print(f"Recommendations after removal: {recommendations}")

def test_large_dataset():
    """Test with larger dataset"""
    print("\n=== Large Dataset Test ===")
    clear_data()
    
    # Create a more complex interaction network
    users = ['User1', 'User2', 'User3', 'User4', 'User5']
    items = ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5', 'Movie6']
    
    # Add various interactions
    interactions = [
        ('User1', 'Movie1'), ('User1', 'Movie2'), ('User1', 'Movie3'),
        ('User2', 'Movie2'), ('User2', 'Movie3'), ('User2', 'Movie4'),
        ('User3', 'Movie1'), ('User3', 'Movie4'), ('User3', 'Movie5'),
        ('User4', 'Movie2'), ('User4', 'Movie5'), ('User4', 'Movie6'),
        ('User5', 'Movie3'), ('User5', 'Movie6')
    ]
    
    for user, item in interactions:
        add_interaction(user, item)
    
    # Test recommendations for each user
    for user in users:
        recommendations = get_top_n_recommendations(user, 3)
        print(f"Top 3 recommendations for {user}: {recommendations}")

def display_graph_state():
    """Display current state of the graph"""
    print("\n=== Current Graph State ===")
    print("User to Items:")
    for user, items in user_to_items.items():
        print(f"  {user}: {list(items)}")
    
    print("\nItem to Users:")
    for item, users in item_to_users.items():
        print(f"  {item}: {list(users)}")

if __name__ == "__main__":
    test_basic_recommendations()
    test_edge_cases()
    test_large_dataset()
    display_graph_state()
