class TreeNode:

 def __init__(self, value):
  self.value = value
  self.children = []
 
 def add_child(self, child_node):
  ##print("Adding " + child_node.value) uncomment if you need to test
  self.children.append(child_node) 
    
 def remove_child(self, child_node):
  ##print("Removing " + child_node.value + " from " + self.value) uncomment if you need to test
  self.children = [
  child for child in self.children if child is not child_node
   ]
 
 def traverse(self):
  nodes_to_visit = [self]
  while len(nodes_to_visit) > 0:
   current_node = nodes_to_visit.pop()
   print(current_node.value)
   nodes_to_visit += current_node.children

digital_cg = TreeNode("Digital Card Games")

mtg_arena = TreeNode("Magic_the_Gathering_Arena")
mtg_f2p = TreeNode({"f2p": 2})
mtg_pve = TreeNode({"pve": 1})
mtg_competitive = TreeNode({"competitive": 2})
mtg_p2w = TreeNode({"p2w": 4})
mtg_arena.add_child(mtg_f2p)
mtg_arena.add_child(mtg_pve)
mtg_arena.add_child(mtg_competitive)
mtg_arena.add_child(mtg_p2w)

eternal = TreeNode("Eternal")
eternal_f2p = TreeNode({"f2p": 4})
eternal_pve = TreeNode({"pve": 2})
eternal_competitive = TreeNode({"competitive": 3})
eternal_p2w = TreeNode({"p2w": 2})
eternal.add_child(eternal_f2p)
eternal.add_child(eternal_pve)
eternal.add_child(eternal_competitive)
eternal.add_child(eternal_p2w)

lor = TreeNode("Legends of Runeterra")
lor_f2p = TreeNode({"f2p": 5})
lor_pve = TreeNode({"pve": 2})
lor_competitive = TreeNode({"competitive": 3})
lor_p2w = TreeNode({"p2w": 2})
lor.add_child(lor_f2p)
lor.add_child(lor_pve)
lor.add_child(lor_competitive)
lor.add_child(lor_p2w)

hearthstone = TreeNode("Hearthstone")
hearthstone_f2p = TreeNode({"f2p": 1})
hearthstone_pve = TreeNode({"pve": 2})
hearthstone_competitive = TreeNode({"competitive": 3})
hearthstone_p2w = TreeNode({"p2w": 5})
hearthstone.add_child(hearthstone_f2p)
hearthstone.add_child(hearthstone_pve)
hearthstone.add_child(hearthstone_competitive)
hearthstone.add_child(hearthstone_p2w)

ptcgo = TreeNode("Pokemon Trading Card Game Online")
ptcgo_f2p = TreeNode({"f2p": 3})
ptcgo_pve = TreeNode({"pve": 1})
ptcgo_competitive = TreeNode({"competitive": 3})
ptcgo_p2w = TreeNode({"p2w": 5})
ptcgo.add_child(ptcgo_f2p)
ptcgo.add_child(ptcgo_pve)
ptcgo.add_child(ptcgo_competitive)
ptcgo.add_child(ptcgo_p2w)

digital_cg.add_child(mtg_arena)
digital_cg.add_child(eternal)
digital_cg.add_child(lor)
digital_cg.add_child(hearthstone)
digital_cg.add_child(ptcgo)