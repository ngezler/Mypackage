def top_n(items, n):
    """Retue=rns the top N elements in an array.

    Args:
        items (Array): list or array like object.
        n (int): num of items to return.

    Return:
        array: top n items, in desc order.

    Egs:
        >>> top_n([2,9,5,8,4],3)
        >>> [9,8,5]
    """
    #keep sorting until you have the top n items
    for i in range(n):
        for j in range(len(items)-1-i):

            #if the current item is biggr than the next item swap the two items
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    #get the last two items
    top_n = items[-n:]

    #return in descending order
    return top_n[::-1]