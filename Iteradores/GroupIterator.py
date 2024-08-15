class GroupIterator:
    def __init__(self,groupby_object):
        self.obj = groupby_object
        self.groups = list(groupby_object.groups.keys())
        self.index = 0
        