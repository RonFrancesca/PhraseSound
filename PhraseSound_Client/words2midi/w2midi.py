import numpy as np
from gensim.models import KeyedVectors
import scipy.stats as stats

#model loading
print('Wait for model to be loaded..')
model_glove = KeyedVectors.load_word2vec_format('../words2midi/glove.6B.50d_word2vec.txt')
print('Model loaded')


def find_range(reduced_dist_word_dim, range_limits):
    """
    Given a point of reduced_dist_word and the interval range limits, the function returns on which interval that point is located
    Input
    --------
    :reduced_dist_word: distance between words collapsed in 25 dimensions
    :range_limits: mapping ranges of a particular dimension
    Return
    --------
    :limit: limit of range
    """
    n_limits = len(range_limits)
    for limit in range(n_limits - 1):
        if (reduced_dist_word_dim > range_limits[limit]) and (reduced_dist_word_dim < range_limits[limit + 1]):
            return limit
    raise ValueError



def colapse_into_25(space_50d):
    '''
    The function collapses the 50 dimensional space into 25 dimensional space summing two consecutive dimensions
    Input
    --------
    :space_50d: 50 dimensional space
    Return
    --------
    :space_25d: 25 dimensional space
    '''
    ndim = space_50d.ndim
    if ndim == 1:  # If a word embedding
        space_25d = np.zeros(25)
        for idx in range(25):
            #summing consecutive dimensions
            space_25d[idx] = np.sum(space_50d[idx*2:(idx+1)*2])
    else:
        space_25d = np.zeros([space_50d.shape[0], 25])
        for idx in range(25):
            space_25d[idx] = np.sum(space_50d[idx*2:(idx+1)*2],)
    return space_25d


def embspace_to_midi(diff_word, n_words):
    """
    The functions get the midi value for each distance of n_words
    Input
    ------------
        :diff_word: The 50dim vector resulting of difference between n_words consecutive words 
        :n_words: Number of words used to create the word_embedding
    Return
    ------------
        :midi: midi value
    """
    #loading the mapping
    embedding = np.load('../words2midi/mappings.npy')
    #collapsing the mapping into 25 dimension
    reduced_25 = colapse_into_25(embedding)
    #get the mapping
    mappings = get_mappings(reduced_25)
    #collapsing the word embedding into 25 dimensions
    reduced_embedding = colapse_into_25(diff_word)
    midi = np.zeros(25)
    for dimension in range(25):
        #get the range for each dimension
        midi[dimension] = find_range(reduced_embedding[dimension], mappings[dimension])
    return midi


def difference_word(input_words, nb_words):
    '''
    The function calulates the distance between two words
    Input
    ----------
    :input words: words received as input
    :nb_words: number of consecutive words received
    Return:
    ----------
    :dist: distance between the nb_words words
    '''
    diffwords = model_glove[input_words[0]] - model_glove[input_words[1]]
    dist = embspace_to_midi(diffwords, nb_words)
    print('Distance: {}'.format(dist))
    return dist


def get_eq_n_intervals(array):
    """
    Get equally probable n intervals for an array assuming Gaussian distribution
    Input
    -----------
    :array: embedding domension
    Return
    -----------
    :intervals: the intervals
    """
    mean = np.mean(array)
    std = 2  # Fixed std. Too extreme values when using std from the array (either 0 or 127).
             # This is very likely because np.std(array) is the standard deviation of all the points of the
             # embedded espace, but what we use in the end is the difference between those points. Calculate 
             # the standard deviation between all posible distances is not really very affordable to keep this
             # low resource consuming, and also it hard to generalise when you want to use more than 2 words 
             # to calculate the distance. 2 seems to work very good. You can try to fine tune it
             # more if you feel like it.

    norm = stats.norm(mean, std)
    intervals = norm.ppf(np.linspace(0, 1, 129))
    return intervals


def get_mappings(embedding):
    """
    Get the mappings for all dimensions of the word embedding
    Input
    -------
    :emdedding: words embedding space
    Return
    ---------
    np array reprresenting the mapping
    """
    n_columns = embedding.shape[1]
    mappings = []
    for i in range(n_columns):
        mappings.append(get_eq_n_intervals(embedding[:, i]))
    return np.array(mappings)
