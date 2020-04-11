import numpy as np
from gensim.models import KeyedVectors
import scipy.stats as stats

#model loading

print('Wait for model to be loaded..')
model_glove = KeyedVectors.load_word2vec_format('../words2midi/glove.6B.50d_word2vec.txt')
print('Model loaded')


def find_range(point, range_limits):
    """
    Given a point and the interval range limits, returns on which interval is located that point
    """
    n_limits = len(range_limits)
    for limit in range(n_limits - 1):
        if (point > range_limits[limit]) and (point < range_limits[limit + 1]):
            return limit
    raise ValueError


def colapse_into_10(space_50d):
    ndim = space_50d.ndim
    if ndim == 1:  # If a word embedding
        space_10d = np.zeros(10)
        for idx in range(10):
            space_10d[idx] = np.sum(space_50d[idx*5:(idx+1)*5])
    else:
        space_10d = np.zeros([space_50d.shape[0], 10])
        for idx in range(10):
            space_10d[idx] = np.sum(space_50d[idx*5:(idx+1)*5],)
    return space_10d


def colapse_into_25(space_50d):
    ndim = space_50d.ndim
    if ndim == 1:  # If a word embedding
        space_25d = np.zeros(25)
        for idx in range(25):
            space_25d[idx] = np.sum(space_50d[idx*2:(idx+1)*2])
    else:
        space_25d = np.zeros([space_50d.shape[0], 25])
        for idx in range(25):
            space_25d[idx] = np.sum(space_50d[idx*2:(idx+1)*2],)
    return space_25d


def embspace_to_midi(word_embedding, n_words):
    """
        word_embedding: The 50dim vector resulting of difference between multiple words embedding
        n_words: Number of words used to create the word_embedding
    """
    embedding = np.load('../words2midi/mappings.npy')
    reduced_25 = colapse_into_25(embedding)
    mappings = get_mappings(reduced_25)

    reduced_embedding = colapse_into_25(word_embedding)
        
    midi = np.zeros(25)
    for dimension in range(25):
        midi[dimension] = find_range(reduced_embedding[dimension], mappings[dimension])
    return midi

def difference_word(input_words, nb_words):
    #todo: loop in case more than 2 words are received 
    diffwords = model_glove[input_words[0]] - model_glove[input_words[1]]
    dist = embspace_to_midi(diffwords, nb_words)
    print('Distance: {}'.format(dist))
    return dist


def get_eq_n_intervals(array):
    """
    Get equally probable n intervals for an array assuming gaussian distribution
    """
    mean = np.mean(array)
    std = 2  # Fixed std. Too extreme values when using std from the array (either 0 or 127).
             # This is very likely because np.std(array) is the standard deviation of all the points of the
             # embedded espace, but what we use in the end is the difference between those points. Calculate 
             # the standard deviation between all posible distances isn't really very affordable to keep this
             # low resource consuming, and also it hard to generalise when you want to use more than 2 words 
             # to calculate the distance. I choosed 2 because seems to work very good. You can try to fine tune it
             # more if you feel like it.

    norm = stats.norm(mean, std)
    intervals = norm.ppf(np.linspace(0, 1, 129))
    return intervals


def get_mappings(embedding):
    """
    Get the mappings for all dimensions of the embedding
    """
    n_columns = embedding.shape[1]
    mappings = []
    for i in range(n_columns):
        mappings.append(get_eq_n_intervals(embedding[:, i]))
    return np.array(mappings)
