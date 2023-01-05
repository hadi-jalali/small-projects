/**
 * Filename: ProfileMain.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:19/4/19<br>
 * @since:19/4/19<br>
 * @version 1.1 <br>
 * @Program purpose:To test if we can create a profile using our profile.java class 
 *  
 */

public class ProfileMain {
	public static void main(String[] args) {
		String interests[]= {"Hockey","Movies"};
		Profile profile=new Profile("chris","brown",20,1,1995,"London","UK","British","c.brown@gmail.com",interests);
		System.out.println(profile);

	}

}
