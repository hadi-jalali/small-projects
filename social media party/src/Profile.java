/**
 * Filename: Profile.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:18/5/19<br>
 * @since:19/5/19<br>
 * @version 1.1 <br>
 * @Program purpose:to construct a profile and set and get related variables
 *  
 */

import java.util.Arrays;

public class Profile {
	private final String firstName; //first name of the profile owner
	private final String lastName;	//last name of the profile owner
	private final int birthDay;		//the day of the birth date
	private final int birthMonth;	//the month of the birth date
	private final int birthYear;	//the year of the birth date
	private String town;			//the town which the profile owner lives in
	private String country;			//the town which the profile owner lives in
	private String nationality;		//the nationality of the profile owner
	private String email;			//profile owner's email
	private String[] interestsList; //an array containing profile
	private Profile[] friendsList;  //an array of the list of friends
	/**
	  * Constructor to create a Profile
	  * 
	  * @param firstName: first name of the profile owner
	  * @param lastName: last name of the profile owner
	  * @param birthDay: the day of the birth date
	  * @param birthMonth: the month of the birth date
	  * @param birthYear: the year of the birth date
	  * @param town: the town which the profile owner lives in
	  * @param country: the town which the profile owner lives in
	  * @param nationality:the nationality of the profile owner
	  * @param email: profile owner's email
	  * @param interestsList: an array containing profile
	  * @param friendsList: an array of the list of friends
	  * 
	  */
	public Profile(String firstName,String lastName,int birthDay,int birthMonth,int birthYear,
			String town, String country,String nationality, String email,String[] interestsList) {
		this.firstName=firstName;
		this.lastName=lastName;
		this.birthDay=birthDay;
		this.birthMonth=birthMonth;
		this.birthYear=birthYear;
		this.country=country;
		this.town=town;
		this.nationality=nationality;
		this.email=email;
		this.interestsList= interestsList;
		
		
	}

	/**
	 * @return the town
	 */
	public String getTown() {
		return town;
	}

	/**
	 * @param town the town to set
	 */
	public void setTown(String town) {
		this.town = town;
	}

	/**
	 * @return the country
	 */
	public String getCountry() {
		return country;
	}

	/**
	 * @param country the country to set
	 */
	public void setCountry(String country) {
		this.country = country;
	}

	/**
	 * @return the nationality
	 */
	public String getNationality() {
		return nationality;
	}

	/**
	 * @param nationality the nationality to set
	 */
	public void setNationality(String nationality) {
		this.nationality = nationality;
	}

	/**
	 * @return the email
	 */
	public String getEmail() {
		return email;
	}

	/**
	 * @param email the email to set
	 */
	public void setEmail(String email) {
		this.email = email;
	}

	/**
	 * @return an array list containing the interests
	 */
	public String[] getInterestsList() {
		return interestsList;
	}

	/**
	 * @param interestsList the interestsList to set
	 */
	public void setInterestsList(String[] interestsList) {
		this.interestsList = interestsList;
	}

	/**
	 * @return the full name
	 */
	public String getName() {
		return firstName+" "+lastName;
	}

	/**
	 * @return the full birth date in a nice format
	 */
	public String getBirthDate() {
		return birthDay+"/" + birthMonth +"/"+ birthYear;
	}
	/**
	 * adds a profile as a friend 
	 * @param: an object of Profile class
	 */
	public void addFriend(Profile P) {
		friendsList[friendsList.length]=P;
	}
	/**
	 * @return the number of friends
	 */
	public Profile getFriend(int i) {
		return friendsList[i-1];
	}
	/**
	 * @return the number of friends
	 */
	public int numOfFriends() {
		return friendsList.length;
	}
	@Override
	/**
	 * @return a string containing all information about the profile
	 */
	public String toString() {
		return "firstName=" + firstName + " \nlastName=" + lastName + " \nbirthDay=" + birthDay + " \nbirthMonth="
				+ birthMonth + " \nbirthYear=" + birthYear + " \ntown=" + town + " \ncountry=" + country + "\nnationality="
				+ nationality + "\nemail=" + email + "\ninterestsList=" + Arrays.toString(interestsList)
				+ "\nfriendsList=" + Arrays.toString(friendsList)+"\n" ;
	}
}	
