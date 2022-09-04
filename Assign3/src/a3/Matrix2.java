package a3;

import ca.queensu.cs.cisc124.notes.basics.geometry.Vector2;

/**
 * A 2x2 matrix. This class provides basic mathematical operations such
 * as matrix-vector and matrix-matrix products, determinant, and inverse.
 *
 */
public class Matrix2 
{
	public double a;
	public double b;
	public double c;
	public double d;
	/**
	 * Initializes this matrix to the identity matrix.
	 */
    public Matrix2()
    {

    }
	/**
	 * Initializes this matrix so that its entries are equal to the specified
	 * values. The matrix entries are defined to be:
	 * 
	 * <pre>
	 * a b
	 * c d
	 * </pre>
	 * 
	 * @param a the value of the upper left element.
	 * @param b the value of the upper right element.
	 * @param c the value of the lower left element.
	 * @param d the value of the lower right element.
	 */
	public Matrix2(double a, double b, double c, double d) 
	{
		this.a = a;
		this.b = b;
		this.c = c;
		this.d = d;
	}
	/**
	 * Initializes this matrix so that it is equal to the specified matrix.
	 * 
	 * @param other a matrix to copy.
	 */
	public Matrix2(Matrix2 other)
    {
        this.a = other.a;
        this.b = other.b;
        this.c = other.c;
        this.d = other.d;
    }
	/**
	 * Returns the entry of this matrix located at the given one-based
	 * row and column indexes. 
	 * 
	 * @throws @IndexOutOfBoundsException if {@code row} is not 1 and not 2.
	 * @throws @IndexOutOfBoundsException if {@code col} is not 1 and not 2.
	 * @param row the row index of the element.
	 * @param col the column index of the element.
	 * @return the element at the specified row and column indexes.
	 */
	public double get(int row, int col)
    {
        if (row > 2 || row < 1 || col > 2 || col < 1)
        {
            throw new IndexOutOfBoundsException("The row or colum provided is out of bounds");
        }
        if (row == 1 && col == 1)
        {
            return a;
        }
        else if (row == 1 && col == 2)
        {
            return b;
        }
        else if (row == 2 && col == 1)
        {
            return c;
        }
        else
        {
            return d;
        }
    }
	/**
	 * Returns a string representation of this matrix. The returned string
	 * has the following form:
	 * 
	 * <pre>
	 * [a, b]
	 * [c, d]
	 * </pre>
	 * 
	 * <p>
	 * where {@code a}, {@code b}, {@code c}, and {@code d} are the {@code double}
	 * values of the entries of this matrix.
	 * 
	 * @return a string representation of this matrix.
	 */
	@Override
	public String toString() 
	{
        return String.format("[%f, %f]\n[%f, %f]", this.a, this.b, this.c, this.d);    
	}
	/**
	 * Returns the determinant of this matrix.
	 * @return the determinant of this matrix.
	 */
	public double det()
    {
        return a*d - b*c;
    }
	/**
	 * Sets the entry of this matrix located at the given
	 * zero-based row and column indexes to the specified value.
	 * 
	 * @param row the row index of the element.
	 * @param col the column index of the element.
	 * @param val the element to store in this matrix.
	 * 
	 * @throws @IndexOutOfBoundsException if {@code row} is not 1 and not 2.
	 * @throws @IndexOutOfBoundsException if {@code col} is not 1 and not 2.
	 * @return a reference to this matrix.
	 */
    public Matrix2 set(int row, int col, double val)
    {
        if (row > 2 || row < 1 || col > 2 || col < 1)
        {
            throw new IndexOutOfBoundsException("The row or colum provided is out of bounds");
        }
        else
        {
            if (row == 1 && col == 1)
            {
                a = val;
                Matrix2 reference = new Matrix2(a, 0.0, 0.0, 0.0);
                return reference;
            }
            else if (row == 1 && col == 2)
            {
                b = val;
                Matrix2 reference = new Matrix2(0.0, b, 0.0, 0.0);
                return reference;
            }
            else if (row == 2 && col == 1)
            {
                c = val;
                Matrix2 reference = new Matrix2(0.0, 0.0, c, 0.0);
                return reference;
            }
            else
            {
                d = val;
                Matrix2 reference = new Matrix2(0.0, 0.0, 0.0, d);
                return reference;
            }
        } 
    }
	/**
	 * Returns the inverse of this matrix if the determinant
	 * of this matrix is not exactly zero.
	 * 
	 * @throws @ArithmeticException if the determinant of this
	 * matrix is exactly zero.
	 * @return the inverse of this matrix.
	 */
	public Matrix2 inv()
    {
        double det_value = det();
        if (det_value == 0)
        {
           throw new ArithmeticException("the determinant of this matrix is exactly zero");
        }
        else
        {
            double fraction = 1/det();
            d = fraction*d;
            b = fraction*(b*-1);
            c = fraction*(c*-1);
            a = fraction*a;
            Matrix2 inv_matrix = new Matrix2(d, b, c, a);
            return inv_matrix;
        }
    }
	/**
	 * Postmultiply this matrix with the specified matrix returning a new matrix.
	 * C = A.mult(B) is equivalent to the mathematical equation C = AB.
	 * 
	 * @param m - a 2x2 matrix.
	 * @return a 2x2 matrix equal to this matrix times {@code m}.
	 */
	public Matrix2 mult(Matrix2 m)
    {
        double new_a = (a*m.a + b*m.c);
        double new_b = (a*m.b + b*m.d);
        double new_c = (c*m.a + d*m.c);
        double new_d = (c*m.b + d*m.d);
        Matrix2 C = new Matrix2(new_a, new_b, new_c, new_d);
        return C;
    }
	/**
	 * Postmultiply this matrix with the specified column
	 * vector returning a new vector.
	 * w = A.mult(v) is equivalent to the mathematical equation
	 * w = Av where v and w are 2x1 column vectors.
	 * @param v - a 2x1 vector.
	 * @return a 2x1 vector equal to this matrix times {@code v}.
	 */
	public Vector2 mult(Vector2 v)
	{
		double new_x = (a*v.x) + (b*v.y);
		double new_y = (c*v.x) + (d*v.y);
		Vector2 new_v = new Vector2(new_x, new_y);
		return new_v;
	}
} 
