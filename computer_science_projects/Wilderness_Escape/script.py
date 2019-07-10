######
# TREENODE CLASS
######

class TreeNode:
    def __init__(self, story_pice):
        self.story_pice = story_pice
        self.choices = []

    def add_child(self, node):
        #print('\nAdding child node......')
        self.choices = []
        self.choices += [node]

    def traverse(self):
        story_node = self
        print(story_root.story_pice)
        while story_node.choices != []:
            user_choice = input('What is your choice? 1 or 2? \n ')
            if user_choice not in ["1", "2"]:
                 print('choice is invalid. Try agian. ')
                 print(user_choice)
            else:
                chosen_index = int(user_choice)
                
                chosen_child = story_node.choices[chosen_index-1]
                print(chosen_child.story_pice)
                story_node=chosen_child



######
# VARIABLES FOR TREE
######

story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")


choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b= TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

######
# TESTING AREA
######

print('\n Once upon a time.... ')



story_root.add_child(choice_a)
story_root.add_child(choice_b)

story_root.traverse()
#user_choice = input('What is your name?')
#print(user_choice)
#print(story_root.story_pice)