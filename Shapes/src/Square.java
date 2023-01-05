/**
 * Filename: Square.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:1/3/19<br>
 * @since:20/3/19<br>
 * @version 1.0 <br>
 * @Program purpose:To create a square with appropriate values 
 *  
 */
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
/**
*
* Square is an square shape that can be drawn to the screen, either
* filled with colour or opaque.
* Its position is determined by the upper left corner of the
* square's bounding rectangle
*/
public class Square extends ClosedShape{
	private int side;
	/**
	 * Creates a square.
	 * @param insertionTime The time when the shape is printed to screen(in miliseconds) 
	 * @param x The display component's x position.
	 * @param y The display component's y position.
	 * @param vx The display component's x velocity.
	 * @param vy The display component's y velocity.
	 * @param side The size of the side of the square (in pixels).
	 * @param colour The line colour or fill colour.
	 * @param isFilled True if the square is filled with colour, false if opaque.
	 */
	public Square(int insertionTime, int x, int y, int vx, int vy, int side, Color colour, boolean isFilled) {
		super (insertionTime, x, y, vx, vy, colour, isFilled);
    	this.side = side;
	}
	 
	/**
     * Method to convert a square to a string.
     */
	    public String toString () {
	    	String result = "This is a Square\n";
	    	result += super.toString ();
		result += "Its side is " + this.side + "\n";
	    	return result;
	    }
	    
	    /**
	     * @param Resets the side.
	     */
	    public void setSide (int side) {
	    	this.side = side;
	    }
	    
	    /**
	     * @return The side of the square.
	     */
	    public int getSide() {
	    	return side;
	    }
	    /**
		  * Get the width of the current component(overrode so it returns the side value(actual width))
		  *
		  * @return the side of the square		  
		  */
	    public int getWidth () {
		 	return side;
		 }

		 /**
		  * Get the height of the current component(overrode so it returns the side value(actual height))
		  * @return the side of the square
		  */
		 public int getHeight () {
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
			//square is a rectangle as width and height both set to side
	    		g.fillRect( x, y, side, side );
	    	} 
	    	else {
	    		g.strokeRect( x, y, side, side );
		    }
	    }


}
