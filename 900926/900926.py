import random  # this should be helpful!


def probability_of_repeated_kmer(num_trials: int, n: int, k: int, alphabet_size: int) -> float:
    """
    Estimate the probability that a random genome contains two equal k-mers.

    Parameters:
        num_trials (int)    - How many random genomes to build (at least 1).
        n (int)             - The length of each random genome.
        k (int)             - The length of the k-mers to compare.
        alphabet_size (int) - How many distinct symbols the genome is built from.

    Returns:
        float - The fraction of the random genomes that contained some k-mer twice.
    """
    summ=0
    for i in range(num_trials):
        summ=summ+one_trial(n,k,alphabet_size)
    return summ/num_trials


def one_trial(n: int, k: int, alphabet_size: int):
    genome=make_genome(n,alphabet_size)
    histt={}
    for i in range(n-k+1):
        frame=genome[i:i+k]
        if not(histt.get(frame)==None):
            return 1
        else:
            histt[frame]=1
    return 0

def make_genome(n: int, alphabet_size: int):
    genome=""
    for i in range(n):
        genome=genome+str(random.randrange(0,alphabet_size))
    return genome
    
