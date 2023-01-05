/**
 * Filename: FileReader.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:5/5/19<br>
 * @since:9/5/19<br>
 * @version 1.1 <br>
 * @Program purpose:To read in values from a file, 
 * create a profile using these values and add it to our tree
 *  
 */

import java.util.Scanner;
import java.io.*;

public class FileReader {
	/**
	  * Method to get the values needed and create a Profile.
	  * 
	  * @param line: the Scanner which has removed the new line character
	  * 
	  * @return an object of the class Profile (a triangle)
	  */
	private static Profile createProfile(Scanner line) { 
		String lastName=line.next();
		String firstName=line.next();
		int birthDay=line.nextInt();
		int birthMonth=line.nextInt();
		int birthYear=line.nextInt();
		String town=line.next();
		String country=line.next();
		String nationality=line.next();
		String email=line.next();
		String interests=line.next();
		String[] interestsList=getInterests(interests);
		
		Profile profile=new Profile(firstName,lastName, birthDay, birthMonth, birthYear,
			 town, country,nationality, email, interestsList); 
		System.out.println(profile.toString());
		return profile;
		
	}
	/**
	  *Method to separate interests from each other 
	  * 
	  * @param interest: the String of all the interests 
	  * 
	  * @return an array of interests
	  */
	private static String[] getInterests(String interests) {
		Scanner counter=new Scanner(interests);
		counter.useDelimiter(";");
		int arraySize=0;
		//we use this to get the number of interests in a profile
		while(counter.hasNext()) {
			arraySize++;
			counter.next();
		}
		counter.close();
		String[] interestsList=new String[arraySize];
		Scanner interestScanner = new Scanner(interests);
		interestScanner.useDelimiter(";");
			//add each interest as an element to the array
			for(int n=0;n<arraySize;n++) {
				interestsList[n]=interestScanner.next();
			}
			interestScanner.close();
		return interestsList;
	}
	/**
	  *Method to create a tree and insert profiles to it 
	  * 
	  * @param in: the scanner of the file  
	  * 
	  * @return the created binary search tree
	  */
	public static BST readProfileSet (Scanner in) {
		 BST profileTree=new BST();
		 while(in.hasNextLine()) {
			 String curLine=in.nextLine();
			 Scanner line = new Scanner(curLine);
			 line.useDelimiter(",");
			 profileTree.insertProfile(createProfile(line));
			 line.close();
		 }
		 in.close();
		 return profileTree;
	 }
	/**
	  *Method to read in the file and check if it exists 
	  * 
	  * @param the name of the file
	  * 
	  * @return a binary seach tree
	  */
	 public static BST readProfileSet(String filename) {
			File textFile=new File(filename);
		    Scanner in = null;
		    
			try {
			in = new Scanner (textFile);
			}
			//if the file is not found it prints an appropriate error
			catch (FileNotFoundException e) {
			System.out.println ("Cannot open " + filename);
			System.exit (0);
			}
			
		    return FileReader.readProfileSet(in);
		    
		}
	 

}
