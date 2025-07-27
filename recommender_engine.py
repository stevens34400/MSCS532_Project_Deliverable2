import heapq
from collections import defaultdict
from recommender_graph import user_to_items, item_to_users, get_graph_stats

def get_top_n_recommendations(user, n, algorithm='collaborative_filtering'):
    """
    Get top N recommendations for a user using specified algorithm
    
    Args:
        user: Target user
        n: Number of recommendations to return
        algorithm: 'collaborative_filtering', 'item_based', or 'user_based'
    
    Returns:
        List of tuples (item, score) sorted by score descending
    """
    if user not in user_to_items or not user_to_items[user]:
        return []
    
    if algorithm == 'collaborative_filtering':
        return collaborative_filtering(user, n)
    elif algorithm == 'item_based':
        return item_based_recommendations(user, n)
    elif algorithm == 'user_based':
        return user_based_recommendations(user, n)
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")

def collaborative_filtering(user, n):
    """Original collaborative filtering algorithm"""
    if user not in user_to_items or not user_to_items[user]:
        return []
    
    scores = {}
    user_items = user_to_items[user]
    
    for item in user_items:
        for other_user in item_to_users.get(item, []):
            if other_user != user:
                for candidate_item in user_to_items.get(other_user, []):
                    if candidate_item not in user_items:
                        scores[candidate_item] = scores.get(candidate_item, 0) + 1
    
    return heapq.nlargest(n, scores.items(), key=lambda x: x[1])

def item_based_recommendations(user, n):
    """Item-based collaborative filtering"""
    if user not in user_to_items or not user_to_items[user]:
        return []
    
    user_items = user_to_items[user]
    item_scores = defaultdict(float)
    
    for user_item in user_items:
        # Find users who also like this item
        similar_users = item_to_users.get(user_item, set())
        
        for similar_user in similar_users:
            if similar_user != user:
                # Get items liked by similar users
                for candidate_item in user_to_items.get(similar_user, []):
                    if candidate_item not in user_items:
                        # Calculate similarity based on item overlap
                        similarity = calculate_item_similarity(user_item, candidate_item)
                        item_scores[candidate_item] += similarity
    
    return heapq.nlargest(n, item_scores.items(), key=lambda x: x[1])

def user_based_recommendations(user, n):
    """User-based collaborative filtering"""
    if user not in user_to_items or not user_to_items[user]:
        return []
    
    user_items = user_to_items[user]
    item_scores = defaultdict(float)
    
    # Find similar users
    similar_users = find_similar_users(user)
    
    for similar_user, similarity in similar_users:
        for candidate_item in user_to_items.get(similar_user, []):
            if candidate_item not in user_items:
                item_scores[candidate_item] += similarity
    
    return heapq.nlargest(n, item_scores.items(), key=lambda x: x[1])

def calculate_item_similarity(item1, item2):
    """Calculate similarity between two items using Jaccard similarity"""
    users1 = item_to_users.get(item1, set())
    users2 = item_to_users.get(item2, set())
    
    if not users1 or not users2:
        return 0.0
    
    intersection = len(users1 & users2)
    union = len(users1 | users2)
    
    return intersection / union if union > 0 else 0.0

def find_similar_users(user, top_k=10):
    """Find users similar to the target user"""
    if user not in user_to_items:
        return []
    
    user_items = user_to_items[user]
    user_similarities = []
    
    for other_user, other_items in user_to_items.items():
        if other_user != user:
            similarity = calculate_user_similarity(user_items, other_items)
            if similarity > 0:
                user_similarities.append((other_user, similarity))
    
    return heapq.nlargest(top_k, user_similarities, key=lambda x: x[1])

def calculate_user_similarity(user1_items, user2_items):
    """Calculate similarity between two users using Jaccard similarity"""
    if not user1_items or not user2_items:
        return 0.0
    
    intersection = len(user1_items & user2_items)
    union = len(user1_items | user2_items)
    
    return intersection / union if union > 0 else 0.0

def get_recommendation_stats(user):
    """Get detailed statistics about recommendations for a user"""
    if user not in user_to_items:
        return {
            'user': user,
            'user_items': 0,
            'total_candidates': 0,
            'recommendations': [],
            'similar_users': 0
        }
    
    user_items = user_to_items[user]
    candidates = set()
    similar_users = set()
    
    for item in user_items:
        for other_user in item_to_users.get(item, []):
            if other_user != user:
                similar_users.add(other_user)
                for candidate_item in user_to_items.get(other_user, []):
                    if candidate_item not in user_items:
                        candidates.add(candidate_item)
    
    return {
        'user': user,
        'user_items': len(user_items),
        'total_candidates': len(candidates),
        'similar_users': len(similar_users),
        'candidates': list(candidates)[:10]  # First 10 candidates
    }
