/**
 * Filename: BSTNodeMain.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:21/4/19<br>
 * @since:21/4/19<br>
 * @version 1.1 <br>
 * @Program purpose:To test if we can create nodes and set 
 * them as right or left nodes to a specidic node in our binary search tree 
 *  
 */
public class BSTNodeMain {

	public static void main(String[] args) {
		String interests[]= {"Hockey","Movies"};
		Profile chris=new Profile("chris","brown",20,1,1995,"London","UK","British","c.brown@gmail.com",interests);
		Profile james=new Profile("james","harden",10,11,1895,"Manchester","UK","American","james@gmail.com",interests);
		Profile david=new Profile("david","villa",10,2,1993,"Barcelona","Spain","Spanish","d.villa@gmail.com",interests);
		BSTNode node1=new BSTNode(chris);
		BSTNode node2=new BSTNode(james);
		BSTNode node3=new BSTNode(david);
		node1.setL(node2);
		node1.setR(node3);
		System.out.println(node1.getL().getProfile().getName());
		System.out.println(node1.getR().getProfile().getName());
		
		
	}

}
