import time 

def naive_search(list, target):
    """
    Perform a naive search to find the target in the given list.
    
    Args:
    list (list): The list to search in.
    target: The target value to find in the list.
    
    Returns:
    int: The index of the target value in the list if it is found, or -1 if it is not found.
    """
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1


def binary_search(list, target):
    """
    This function takes list and target as parameters and 
    searches for a target value in a sorted list using binary search.

    Args:
        list (list): A sorted list of integers.
        target (int): The target value to search for in the list.

    Returns:
        int: The index of the target value in the list, or -1 if the target 
        value is not found.

    """
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# A list with more than 100 words in it.
words = ['abundance', 'accumulate', 'acquaintance', 'administration', 'advertisement', 'advantageous', 'affirmative', 'alternative', 'ambassador', 'announcement', 'appreciate', 'architecture', 'articulate', 'assassination', 'association', 'atmosphere', 'authentication', 'authorization', 'availability', 'beneficial', 'benevolent', 'cancellation', 'capability', 'capacity', 'characteristic', 'circumstance', 'combination', 'communication', 'competition', 'comprehensive', 'conceivable', 'concurrent', 'consequently', 'conservative', 'considerable', 'consistently', 'constitution', 'controversy', 'convenience', 'cooperative', 'coordinate', 'correspondence', 'credibility', 'curiosity', 'declaration', 'definitely', 'deliberation', 'demonstration', 'depression', 'derivation', 'description', 'development', 'differentiate', 'dimensional', 'discrimination', 'disposition', 'distinction', 'dramatically', 'education', 'elimination', 'emphasize', 'enlightenment', 'entertainment', 'environment', 'equivalent', 'establishment', 'evolutionary', 'exaggeration', 'examination', 'exceptional', 'exhibition', 'expansion', 'explanation', 'expression', 'extravagant', 'fundamental', 'generalization', 'government', 'graduation', 'hypothesis', 'identification', 'illustration', 'implementation', 'implication', 'improvement', 'independence', 'indication', 'individual', 'industrial', 'inevitable', 'influence', 'innovation', 'instruction', 'intellectual', 'interpretation', 'intervention', 'investigation', 'legislation', 'legitimate', 'logistical', 'magnificent', 'management', 'manipulation', 'measurement', 'methodology', 'motivation', 'negotiation', 'notification', 'obligation', 'observation', 'opportunity', 'optimization', 'organization', 'originally', 'overwhelming', 'participation', 'particularly', 'perpetrator', 'perspective', 'philosophy', 'plagiarism', 'possibility', 'practically', 'preliminary', 'preparation', 'presidential', 'principally', 'probability', 'professional', 'progression', 'prohibition', 'proposition', 'provisional', 'qualification', 'reconstruction', 'reinforcement', 'relationship', 'repetition', 'representation', 'republican', 'reservation', 'responsible', 'revolutionary', 'significant', 'specialist', 'specifically', 'spontaneous', 'standardize', 'stimulation', 'subsequently', 'substantial', 'substitute', 'sufficiently', 'supplemental', 'sustainability', 'symbolically', 'technological', 'termination', 'theoretical', 'traditional', 'transmission', 'university', 'utilization', 'vocabulary', 'voluntarily', 'vulnerability', 'willingness']


# Target word to be found.
target_word = 'technological'

# Looking for the target using naive search and timing the searching time.
start = time.time()
results = naive_search(words, target_word)
print(f'Resutls with naive search {results}')
end = time.time()
print(f"Time taken searching using naive search algorithm: {end-start} seconds")

# Looking for the target using binary search and timing the searching time.
start = time.time()
results = binary_search(words, target_word)
print(f'\nResutls with binary search {results}')
end = time.time()
print(f"Time taken searching using binary search algorithm: {end-start} seconds")

# Note that this code will output 156, since Python uses 0-indexing (the first item in the list has an index of 0).