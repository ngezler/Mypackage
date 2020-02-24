from Mypackage import Mymodule

    """
        testing the accurracy of the top_n function
    """
    assert Mymodule.top_n([6,4,3,1,9],3) == [9,6,4], 'Failed'
    assert Mymodule.top_n([10,6,1],2) == [10,6], 'Failed'
    assert Mymodule.top_n([6,4,3,1,9],1) == [9], 'Failed'

