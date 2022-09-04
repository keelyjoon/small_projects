package a3;

import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

import ca.queensu.cs.cisc124.notes.basics.geometry.Vector2;

import princeton.introcs.StdDraw;

public class LineFit 
{

	/**
	 * Finds the line of best fit to a sequence of points using ordinary least
	 * squares. The returned array consists of the y-intercept followed by
	 * the slope of the best fit line. If {@code a} is the returned array,
	 * then the equation of the line is given by:
	 * 
	 * <pre>
	 * y = a[0] + a[1] * x;
	 * </pre>
	 * 
	 * @param p a list of points to fit a line to
	 * @return an array containing the y-intercept and slope of the best fit line
	 * @throws IllegalArgumentException if {@code p} has fewer than two points
	 * @throws ArithmeticException if the line of best fit is exactly vertical
	 */
	public static double[] lsfit(List<Vector2> p) 
	{
		// throwing exeption if arraylist has less than two points 
		if (p.size() < 2)
		{
			throw new  IllegalArgumentException("p (given ArrayList) has fewer than two points");
		}
		else
		{
			// declaring varaibles for future calculations
			int i = 0;
			double b = 0.0;
			double c = 0.0;
			double d = 0.0;
			double y = 0.0;
			double x = 0.0;

			// while loop running for the size of p
			while (i < p.size())
			{
				// calculating doubles for Matrix and Vector
				b += p.get(i).x();
				c = b;
				d += Math.pow(p.get(i).x(), 2);
				y += (p.get(i).y());
				x += p.get(i).y()*p.get(i).x();
				i++;
			} 
			double a = (double) i;
			// creating first Matrix
			Matrix2 first_matrix = new Matrix2(a, b, c, d);
			// creating first Vector
			Vector2 first_vector = new Vector2(y, x);
			// calculating the inverse of the first Matrix
			Matrix2 inv_matrix = first_matrix.inv();
			// calculating the final Vector
			Vector2 mult_vector = inv_matrix.mult(first_vector);
			// returning the vector as an array of doubles
			double parameters[] = {mult_vector.x(), mult_vector.y()};
			return parameters;
		}
	}
	/**
	 * Plots the specified sequence of points and line.
	 * 
	 * @param p a list of points to plot
	 * @param line the y-intercept and slope of the line to plot
	 */
	public static void plot(List<Vector2> p, double[] line) {
		StdDraw.clear();
		for (Vector2 v : p) {
			StdDraw.setPenColor(Color.BLACK);
			StdDraw.filledCircle(v.x(), v.y(), 0.25);
		}
		double x1 = -10.0;
		double y1 = line[1] * x1 + line[0];
		double x2 = 10.0;
		double y2 = line[1] * x2 + line[0];
		StdDraw.setPenColor(Color.RED);
		StdDraw.line(x1, y1, x2, y2);
	}
	/**
	 * Plots 10 points randomly displaced vertically from the line
	 * {@code y = 0.0 + x} and the line of the best fit. Prints the
	 * slope and intercept of the best fit line to standard output. 
	 * 
	 * @param args not used
	 */
	public static void main(String[] args) 
	{
		StdDraw.setScale(-11, 11);
		List<Vector2> p = new ArrayList<>();
		for (int i = 0; i < 5; i++) 
		{
			double x = i * 2 - 10;
			double y = x + (Math.random() - 0.5) * 4;
			p.add(new Vector2(x, y));
		}
		lsfit(p);
		double[] params = lsfit(p);
		System.out.println("slope : " + params[1] + ", intercept : " + params[0]);
		plot(p, params);
	}
}
