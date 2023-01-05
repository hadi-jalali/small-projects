
/**
 * Filename: ReadShapeFile.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:10/3/19<br>
 * @since:21/3/19<br>
 * @version 1.3 <br>
 * version history:
 * 1.0:Plain code Dan gave us.
 * 1.1:code with readData,createCircle and createOval methods
 * 1.2:Added createSquare and createRect methods to the code.
 * 1.3:Added createTriangle method to the code.
 * @Program purpose:A class that reads a file and adds different shapes to a queue.
 *  
 */
import javafx.scene.paint.Color;

//import javafx.scene.text.Font;
import java.io.*;
import java.util.Scanner;

public class ReadShapeFile {
	/**
	 * Method to get the values needed and create a equilateral triangle.
	 * 
	 * @param line
	 *             the Scanner which has removed the new line character
	 * @return an object of the class Triangle (a triangle)
	 */
	public static Triangle createTriangle(Scanner line){
		int x=line.nextInt();
		int y=line.nextInt();
		int vx=line.nextInt();
		int vy=line.nextInt();
		boolean isFilled=line.nextBoolean();
		int side=line.nextInt();
		int r=line.nextInt();
		int g=line.nextInt();
		int b=line.nextInt();
		int insertionTime=line.nextInt();
		Color triangleColour=Color.rgb(r, g, b);
		Triangle triangle=new Triangle(insertionTime, x, y,vx, vy,side, triangleColour, isFilled);
		return triangle;
		}
	/**
	 * Method to get the values needed and create a circle .
	 * 
	 * @param line
	 *             the Scanner which has removed the new line character
	 * @return an object of the class Circle (a circle)
	 */
	private static Circle createCircle(Scanner line){
		int x=line.nextInt();
		int y=line.nextInt();
		int vx=line.nextInt();
		int vy=line.nextInt();
		boolean isFilled=line.nextBoolean();
		int diameter=line.nextInt();
		int r=line.nextInt();
		int g=line.nextInt();
		int b=line.nextInt();
		int insertionTime=line.nextInt();
		Color circleColor=Color.rgb(r, g, b);
		Circle circle=new Circle(insertionTime, x, y, vx, vy, diameter, circleColor, isFilled);
		return circle;
	}
	/**
	 * Method to get the values needed and create an oval .
	 * 
	 * @param line
	 *             the Scanner which has removed the new line character
	 * @return an object of the class Oval (an oval)
	 */
	private static Oval createOval(Scanner line){
		int x=line.nextInt();
		int y=line.nextInt();
		int vx=line.nextInt();
		int vy=line.nextInt();
		boolean isFilled=line.nextBoolean();
		int width=line.nextInt();
		int height=line.nextInt();
		int r=line.nextInt();
		int g=line.nextInt();
		int b=line.nextInt();
		int insertionTime=line.nextInt();
		Color ovalColor=Color.rgb(r, g, b);
		Oval oval=new Oval(insertionTime, x, y, vx, vy, width, height, ovalColor, isFilled);
		return oval;
	}
	
	/**
	 * Method to get the values needed and create a rectangle .
	 * 
	 * @param line
	 *            of the Scanner which has removed the new line character
	 * @return an object of the class Rect (a rectangle)
	 */
	private static Rect createRect(Scanner line){
		int x=line.nextInt();
		int y=line.nextInt();
		int vx=line.nextInt();
		int vy=line.nextInt();
		boolean isFilled=line.nextBoolean();
		int width=line.nextInt();
		int height=line.nextInt();
		int r=line.nextInt();
		int g=line.nextInt();
		int b=line.nextInt();
		int insertionTime=line.nextInt();
		Color rectColor=Color.rgb(r, g, b);
		Rect rect=new Rect(insertionTime, x, y, vx, vy, width, height, rectColor, isFilled);
		return rect;
	}
	/**
	 * Method to get the values needed and create a square .
	 * 
	 * @param line
	 *            the name of the Scanner which has removed the new line character
	 * @return an object of the class Square (a square)
	 */
	private static Square createSquare(Scanner line){
		int x=line.nextInt();
		int y=line.nextInt();
		int vx=line.nextInt();
		int vy=line.nextInt();
		boolean isFilled=line.nextBoolean();
		int side=line.nextInt();
		int r=line.nextInt();
		int g=line.nextInt();
		int b=line.nextInt();
		int insertionTime=line.nextInt();
		Color squareColor=Color.rgb(r, g, b);
		Square square=new Square(insertionTime, x, y, vx, vy, side, squareColor, isFilled);
		return square;
	}
	/**
	 * Reads the data file used by the program, add the proper shape to the queue based on the
	 * shape name and then returns the constructed queue.
	 * 
	 * @param in
	 *            the scanner of the file
	 * @return the queue represented by the data file
	 */
	private static Queue<ClosedShape> readDataFile(Scanner in) {
		Queue<ClosedShape> shapeQueue = new Queue<ClosedShape>();
		/*creates an scanner and gets rid of the new line character(/n)*/
		while (in.hasNextLine ()) {
			String curLine = in.nextLine ();
			Scanner line = new Scanner (curLine);
			String shapeName=line.next();
			//Checks the first word and adds the right shape based on it
			if(shapeName.equals("circle")){
				shapeQueue.enqueue(createCircle(line));
			}
			else if(shapeName.equals("oval")){
				shapeQueue.enqueue(createOval(line));
			}
			else if(shapeName.equals("square")){
				shapeQueue.enqueue(createSquare(line));
			}
			else if(shapeName.equals("rect")){
				shapeQueue.enqueue(createRect(line));
			}
			else if(shapeName.equals("triangle")){
				shapeQueue.enqueue(createTriangle(line));
			}
			line.close();
			
		}
		in.close();
		return shapeQueue;
	}





	/**
	 * Method to read the file and return a queue of shapes from this file. The
	 * program should handle the file not found exception here and shut down the
	 * program gracefully.
	 * 
	 * @param filename
	 *            the name of the file
	 * @return the queue of shapes from the file
	 */
	public static Queue<ClosedShape> readDataFile(String filename) {
		File shapeList=new File(filename);
	    Scanner in = null; 
	    

		try {
		in = new Scanner (shapeList);
		}
		
		catch (FileNotFoundException e) {
		System.out.println ("Cannot open " + filename);
		System.exit (0);
		}
		
	    return ReadShapeFile.readDataFile(in);
	    
	}
}
