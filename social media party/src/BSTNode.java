/**
 * Filename: BSTNode.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:20/4/19<br>
 * @since:21/4/19<br>
 * @version 1.1 <br>
 * @Program purpose:To create a node for our binary search tree 
 *  
 */

public class BSTNode {
	private Profile data; //all the data such as name
	private BSTNode l;    //left child of the node
	private BSTNode r;    //right child of the node
	/**
	  * Constructor to make a binary search true using a profile
	  * 
	  * @param data: an instance of a profile which contains data like name,etc
	  */
	public BSTNode(Profile data) {
		this.data=data;
		l=null;
		r=null;
	}
	/**
	  * Method to get the profile in an specific node
	  * 
	  * @return an object of the class Profile
	  */
	public Profile getProfile() {
		return data;
	}
	
	/**
	  * Method to make a left reference to an specific node
	  * 
	  * @param l: an object of BSTNode
	  */
	public void setL(BSTNode l) {
		this.l=l;
	}
	/**
	  * Method to make a right reference to an specific node
	  * 
	  * @param r: an object of BSTNode
	  */
	public void setR(BSTNode r) {
		this.r=r;
	}
	/**
	  * Method to get the left node of an specific node
	  * 
	  * @return an object of the class BSTNode
	  */
	public BSTNode getL(){
		return this.l;
	}
	/**
	  * Method to get the right node of an specific node
	  * 
	  * @return an object of the class BSTNode
	  */
	public BSTNode getR() {
		return this.r;
	}

}
