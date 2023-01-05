/**
 * Filename: Rect.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:1/3/19<br>
 * @since:20/3/19<br>
 * @version 1.0 <br>
 * @Program purpose:To create a rectangle with appropriate values 
 *  
 */

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
/**
*
* Rect is an rectangle shape that can be drawn to the screen, either
* filled with colour or opaque.
* Its position is determined by the upper left corner of the
* rect's bounding rectangle
*/
public class Rect extends ClosedShape {
	private int width, height;
	  
	/**
     * Creates a rectangle.
     * @param insertionTime The time when the shape is printed to screen(in miliseconds) 
     * @param x The display component's x position.
     * @param y The display component's y position.
     * @param vx The display component's x velocity.
     * @param vy The display component's y velocity.
     * @param height The height of the rectangle.
     * @param width The width of the rectangle.
     * @param colour The line colour or fill colour.
     * @param isFilled True if the rectangle is filled with colour, false if opaque.
     */
	public Rect(int insertionTime, int x, int y, int vx, int vy, int width,int height, Color colour, boolean isFilled) {
		super (insertionTime, x, y, vx, vy, colour, isFilled);
		this.width = width;
		this.height = height;
	}
	/**
     * Method to convert a circle to a string.
     */
	 public String toString () {
	    	String result = "This is a rectangle\n";
	    	result += super.toString ();
		result += "Its width is " + this.width + " and its height is " + this.height + "\n";
	    	return result;
	    }
		/**
		 * @param width Resets the width.
		 */
	 	public void setWidth (int width) {
			this.width = width;
		}

	 	/**
	 	 * @param height Resets the height.
	 	 */
	 	public void setHeight (int height) {
			this.height = height;
		}

	 	/**
	 	 * @return The width of the rectangle.(Overrode to return the actual width)
	 	 */
	 	public int getWidth() {
			return width;
		}

	 	/**
	 	 * @return The height of the rectangle(overrode to return the actual height).
	 	 */
	 	public int getHeight() {
			return height;
		}

	 	/**
	 	 * Draw the rectangle.
	 	 * @param g The graphics object of the drawable component.
	 	 */
		public void draw (GraphicsContext g) {
			g.setFill (colour);
			g.setStroke( colour );
			if (isFilled) {
				g.fillRect( x, y, width, height );
			} 
			else {
				g.strokeRect( x, y, width, height );
			}
		}

}
