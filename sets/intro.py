def average(array):
    # remove duplicates
    heights = set(array)
    average = sum(heights)/len(heights)
    return average
