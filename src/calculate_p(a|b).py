"""
Calculates the probability of event A given event B using Bayes' theorem.
"""

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8, 9]
s = 9

def get_sample_size(a, b):

    max_sample_size = max(len(a), len(b))
    sample_size = 0

    for i in len(max_sample_size):
        if a(i) == b(i):
            continue
        else:
            sample_size+=1

    return sample_size

print(get_sample_size)

def calculate_p_a_given_b(a, b, s):
    """
    Calculate P(A|B) using Bayes' theorem.
    
    P(A|B) = P(B|A) * P(A) / P(B)
    
    For simplicity, we assume uniform probabilities for events A and B.
    """
    p_a = len(a)/s  # P(A)
    p_b = len(b)/s # P(B)
    p_b_given_a = 2/5

    p_a_given_b = (p_b_given_a * p_a) / p_b
    return round(p_a_given_b, 2)

print(f"P(A|B) = {calculate_p_a_given_b(a, b, s)}")
