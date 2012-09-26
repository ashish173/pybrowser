#!/usr/bin/python
# interpreting the a parse tree in a recursive procedure 
# recursive procs are cool...:)
def eval_exp(tree):
	nodetype = tree[0]
	if nodetype == "number":
		return int(tree[1])
	elif nodetype == "binop":	# if the tree is a nodetype "binop" then we are breaking it furthur.
		left_child = tree[1]
		right_child = tree[3]
		operator = tree[2]
		#now evaluating the left and right child
		left_value = eval_exp(left_child)   #evaluates the left subtree
		right_value = eval_exp(right_child)  #evals the right subtree
		if operator == "+":
			return left_value + right_value
		elif operator == "-":
			return left_value - right_value
	



def main():
	tree = ("binop",("number","5"),"+",("number","8"))
	test_tree2 = ("number","1776")
	test_tree3 = ("binop",("number","5"),"+",("binop",("number","7"),"-",("number","18")))
	print eval_exp(tree)
	print eval_exp(test_tree2)
	print eval_exp(test_tree3)	
	print "happy now!!!"
if __name__ == "__main__":
	main()
