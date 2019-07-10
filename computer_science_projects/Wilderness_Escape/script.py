######
# TREENODE CLASS
class TreeNode:
    def __init__(self, story_pice):
        self.story_pice = story_pice
        self.choices = []
######

######
# VARIABLES FOR TREE
######

######
# TESTING AREA
######


story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")



print('\n Once upon a time.... ')

print(story_root.story_pice)
