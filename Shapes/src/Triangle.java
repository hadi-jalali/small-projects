/**
 * Filename: Triangle.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:21/3/19<br>
 * @since:21/3/19<br>
 * @version 1.0 <br>
 * @Program purpose:To create a equilateral rectangle with appropriate values 
 *  
 */
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
/**
*
* Triangle is a equilateral triangle shape that can be drawn to the screen, either
* filled with colour or opaque.
* Its position is determined by the upper left corner of the
* triangle's bounding rectangle
*/
public class Triangle extends ClosedShape{
	private int side;
	  
	/**
     * Creates a triangle.
     * @param insertionTime The time when the shape is printed to screen(in miliseconds) 
     * @param x The display component's x position.
     * @param y The display component's y position.
     * @param vx The display component's x velocity.
     * @param vy The display component's y velocity.
     * @param side is the size of the triangle's sides.
     * @param colour The line colour or fill colour.
     * @param isFilled True if the rectangle is filled with colour, false if opaque.
     */
	public Triangle(int insertionTime, int x, int y,
			int vx, int vy,int side, Color colour, boolean isFilled) {
		super (insertionTime,x, y, vx, vy, colour, isFilled);
		this.side=side;
		//this.width=width;
	}
	/**
	 * Creates an array and adds three elements to it
	 * @param x first value to be added to the array.
	 * @param y second value to be added to the array.
	 * @param z third value to be added to the array.
	 * @return the completed array 
	 */
	public double[] setPoints(double x,double y,double z){
		double[] points= new double[3];
		points[0]=x;
		points[1]=y;
		points[2]=z;
		return points;
		
	}
	
	 /**
     * Method to convert a triangle to a string.
     */
	 public String toString (){
	    	String result = "This is a Triangle\n";
	    	result += super.toString ();
	    	return result;
	 }
	 /**
	  * Get the width of the current component(overrode so it returns the actual height)
	  *
	  * @return half of the value of side multiplied by the square root of3.	  
	  */
	 public int getHeight() {
		return (int)(side*Math.sqrt(3)/2);
		}
	 /**
	  * Get the width of the current component(overrode so it returns the side value(actual width))
	  *
	  * @return the side of the triangle.	  
	  */
	public int getWidth() {
		return side;
		}
	    /**
	     * Draw the Square on the screen.
	     * @param g The graphics object of the scene component.
	     */
	    public void draw (GraphicsContext g) {
	    	g.setFill( colour );
	    	g.setStroke( colour );
	    	if (isFilled) {
	    		//Started from a point and added appropriate value to draw an equilateral triangle
	    		g.fillPolygon(setPoints(x,x+(side/2),x+side),setPoints(y,y+(side*Math.sqrt(3)/2),y), 3 );
	    		
	    	} 
	    	else {
	    		g.strokePolygon(setPoints(x,x+side/2,x+side),setPoints(y,y+(side*Math.sqrt(3)/2),y), 3 );
		    }
	    }


}
