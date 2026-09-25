import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    numerator = np.dot(a,b)
    denorm = norm_a*norm_b
    if denorm == 0:
        return 0.0
    return float(numerator/denorm)
    pass