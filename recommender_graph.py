user_to_items = {}
item_to_users = {}

def add_interaction(user, item):
    """Add an interaction between user and item"""
    user_to_items.setdefault(user, set()).add(item)
    item_to_users.setdefault(item, set()).add(user)

def remove_interaction(user, item):
    """Remove an interaction between user and item"""
    user_to_items.get(user, set()).discard(item)
    item_to_users.get(item, set()).discard(user)
    
    # Clean up empty entries
    if user in user_to_items and not user_to_items[user]:
        del user_to_items[user]
    if item in item_to_users and not item_to_users[item]:
        del item_to_users[item]

def get_user_items(user):
    """Get all items for a specific user"""
    return user_to_items.get(user, set()).copy()

def get_item_users(item):
    """Get all users for a specific item"""
    return item_to_users.get(item, set()).copy()

def get_all_users():
    """Get all users in the system"""
    return set(user_to_items.keys())

def get_all_items():
    """Get all items in the system"""
    return set(item_to_users.keys())

def get_interaction_count():
    """Get total number of interactions"""
    return sum(len(items) for items in user_to_items.values())

def get_user_count():
    """Get total number of users"""
    return len(user_to_items)

def get_item_count():
    """Get total number of items"""
    return len(item_to_users)

def clear_all_data():
    """Clear all interaction data"""
    user_to_items.clear()
    item_to_users.clear()

def get_graph_stats():
    """Get statistics about the graph"""
    return {
        'users': get_user_count(),
        'items': get_item_count(),
        'interactions': get_interaction_count(),
        'avg_items_per_user': get_interaction_count() / max(get_user_count(), 1),
        'avg_users_per_item': get_interaction_count() / max(get_item_count(), 1)
    }
