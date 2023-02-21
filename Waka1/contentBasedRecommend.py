from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Movie A's categories ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy']

# Movie B's categories ['Adventure', 'Children', 'Fantasty'])

# Calculate Jaccard similarity index

# Movie A's categories as a binary vector
category_a = np.array([1, 1, 1, 1, 1])

# Movie B's categories as a binary vector
category_b = np.array([1, 0, 1, 0, 1])

# Calculate cosine similarity
similarity = cosine_similarity([category_a], [category_b])
print("The Cosine similarity between Movie A and Movie B based on category is: ", similarity[0][0]) #0.7745966692414834

similarity = jaccard_score(category_a, category_b, average='macro')
print("The Jaccard similarity between Movie A and Movie B based on category is: ", similarity) #0.3
