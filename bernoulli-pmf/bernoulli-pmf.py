import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    pmf = []
    for i in x:
        if i == 0:
            pmf.append(float(abs(1-p)))
        else:
            pmf.append(p)
    pmf = np.array(pmf)
                       
    return {"pmf":pmf,"mean":float(p),"variance":float(p*(1-p))}
    pass