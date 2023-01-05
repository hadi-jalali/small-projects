/**
 * Filename: BSTMain.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:25/4/19<br>
 * @since:26/4/19<br>
 * @version 1.1 <br>
 * @Program purpose:To test if our BST class works and we can add profile without any error
 * (we check if it is possible to crate a binary tree search using this class)
 *  
 */
public class BSTMain {

	public static void main(String[] args) {
		String interests[]= {"Football","Basketball"};
		Profile chris=new Profile("Chris","Bosh",10,6,1990,"Miami","USA","American","c.bosh@gail.com",interests);
		Profile alex=new Profile("alex","brown",20,1,1995,"London","UK","British","c.brown@gmail.com",interests);
		Profile james=new Profile("james","harden",10,11,1895,"Manchester","UK","American","james@gmail.com",interests);
		Profile david=new Profile("david","villa",10,2,1993,"Barcelona","Spain","Spanish","d.villa@gmail.com",interests);
		BST tree=new BST();
		tree.insertProfile(alex);
		tree.insertProfile(chris);
		tree.insertProfile(james);
		tree.insertProfile(david);
		tree.printAlphabetical();
	}

}
