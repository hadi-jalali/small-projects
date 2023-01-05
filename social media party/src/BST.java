/**
 * Filename: BST.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:22/4/19<br>
 * @since:6/5/19<br>
 * @version 1.3 <br>
 * version history:<br>
 * 1.1:The code without toString or methods for alphabetic print<br>
 * 1.2:The code without methods for alphabetic print<br>
 * 1.3:The final program<br>
 * @Program purpose:To create a Binary search tree and print its nodes alphabetically if asked 
 *  
 */

public class BST {
	//root node
	private BSTNode root;
	/**
	  * Constructor to construct an empty(for now) binary search tree 
	  */
	public BST() {
		this.root=null;
	}
	/**
	  * Method to create a node using a profile and insert it 
	  * into the binary search tree
	  * 
	  * @param p: an object from Profile class
	  */
	public void insertProfile(Profile p) {
		BSTNode node=new BSTNode(p);
		//if the tree is empty then the created node becomes the root
		if (this.root==null) {
			this.root=node;
		}
		//if the tree is not empty then we call a recursive method
		else {
			addRecursively(node,this.root);
		}
	}
	/**
	  * A recursive method to add the profiles in the right 
	  * position based on their starting character
	  * 
	  * @param node: the node that we are trying to add to the tree 
	  * @param currentNode: the node that we currently are comparing our node to  
	  * 
	  */
	private void addRecursively(BSTNode node,BSTNode currentNode) {
		    //if the profile name comes before the current position's name we go left
			if(node.getProfile().getName().compareToIgnoreCase(currentNode.getProfile().getName())<=0) {
				//if the left child is empty then we add the node 
				if(currentNode.getL()==null) {
					currentNode.setL(node);
				}
				//if the left child is not empty then we call the recursive method again
				else {
					addRecursively(node,currentNode.getL());
				}
		    }
			//if the profile name comes after the current position's name we go right
			else if(node.getProfile().getName().compareToIgnoreCase(currentNode.getProfile().getName())>0) {
				//if the right child is empty then we add the node 
				if (currentNode.getR()==null) {
					currentNode.setR(node);
				}
				//if the right child is not empty then we call the recursivemethod again
				else{
					addRecursively(node,currentNode.getR());
				}
				
			}	
		
	}
	/**
	  * Method to visit the binary search tree using inorder traversal
	  * 
	  * @param currentNode: the node that we want to start our traversal from
	  *
	  */
	public void inorder(BSTNode currentNode) {
		//visit from left to right
	    if(currentNode !=  null) {
	    	inorder(currentNode.getL()); 	
	      System.out.printf(currentNode.getProfile().getName()+"/");
	      inorder(currentNode.getR());
	    }
	  }
	/**
	  * Method to pass in the root node to the inorder method 
	  * because we don't have access to it outside this class.
	  *
	  */
	public void printAlphabetical() {
		inorder(this.root);
	}
}	