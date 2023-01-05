/**
 * Filename: Queue.java<br>
 * @author Hadi Jalali<br>
 * Copyright: no copyright<br>
 * Created:15/3/19<br>
 * @since:18/3/19<br>
 * @version 1.1 <br>
 * version history:
 * 1.0:code without print method
 * 1.1:code with the print method
 * @Program purpose:A class that implements a queue
 *  
 */
import java.io.FileNotFoundException;
import java.util.NoSuchElementException;

public class Queue<T> {
	//create head and nail nodes
	private QueueElement<T> head,tail;
	
	
	/**
	 * Constructs an empty Queue.
	 */
	public Queue () {
		 this.head= null;
		 this.tail=null;
	}
	
	
	/**
	 * checks if the queue is empty
	 * 
	 * @return true if the queue is empty
	 * 
	 */
	public boolean isEmpty () {
	    return (this.head==null)&&(this.tail==null);
	}
	
	
	/**
	 * finds out the the element at the head of the queue
	 * 
	 * @return the head element of the queue
	 */
	public T peek () throws NoSuchElementException {
		if(isEmpty()){
			throw new NoSuchElementException("The queue is empty!!!");
		}
		return head.getElement();
		
		
	}
	
	/**
	 * Removes the front element of the queue
	 */
	public void dequeue () throws NoSuchElementException {
		if (isEmpty()){
			throw new NoSuchElementException("The queue is empty!!!");
			}
		//gets the ellements after head
		QueueElement<T> temp=head.getNext();
		
		/*if there's only one element then the tail would be set to null,
		if not we'll remove from head*/
		
		if(temp==null){
			this.tail=null;
		}
		if(temp!=null){
			this.head=null;
		}
	//set the new head
		this.head=temp;
			
		}
	
	/**
	 * Puts an element on the back of the queue.
	 * 
	 * @param the  element to be added
	 */
	public void enqueue (T element) {
		QueueElement<T> temp = new QueueElement<T>(element,null);
       
        // If queue is empty, then new node is head and tail both 
        if (isEmpty()) {
        	this.head  = temp; 
        	this.tail=temp;
        }
        //add the element to the tail
        this.tail.setNext(temp);
        this.tail=temp;
 
 
     
	}

	/**
	 * Method to print the full contents of the queue in order from head to tail and
	 * to print an appropriate message if it's empty.
	 */
	public void print () {
		QueueElement<T> temp = this.head;
		while(temp!=null){
			System.out.println(temp.getElement());
			temp=temp.getNext();
		if(isEmpty()){
			System.out.println("The queue is empty");
		}
		}
		
		
		
		
	}
}
