# Python code 
class TrieNode: 

	# Trie node class 
	def _init_(self): 
		self.children = [None for _ in range(26)] 

		# This will keep track of number of strings that are 
		# stored in the Trie from root node to any Trie node. 
		self.wordCount = 0
		
		# This code is contributed by ishankhandelwals. 
