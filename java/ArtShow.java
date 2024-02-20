
/**
 * Avni Gandhi
 * 02/14/2022
 * ArtShow.java
 * 
 * Makes use of recursion to create an interesting
 * pattern. Also uses 2D Graphics to create a sphere for
 * the recursive pattern.
 */

import java.awt.Color;

import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;

import java.awt.geom.Ellipse2D;

public class ArtShow extends JFrame implements ActionListener {
	private double time = 0; // time
	private double dt = 0.00001; // change in time
	private int width = 1200;
	private int height = 800;

	Timer timer = new Timer(100, this);
	MyPanel drawingArea1 = null; // The Panel
	public final int size = 400; // The width of the frame

	public static void main(String[] args) {
		ArtShow as = new ArtShow();
	}

	/**
	 * Constructor creates a JPanel and starts the timer for the recursive pattern.
	 */
	public ArtShow() {
		drawingArea1 = new MyPanel();
		drawingArea1.setVisible(true);
		setPreferredSize(new Dimension(width, height));
		// Set the drawingArea panel as its content
		setContentPane(drawingArea1);
		// Tell this frame to terminate when the JFrame display is closed.
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		// Set the title of the displayed window.
		setTitle("Art Show");
		// Make it visible
		// Make it visible
		setVisible(true);
		// Pack this frame
		pack();
		// Make it visible.
		setVisible(true);
		timer.start();
	}

	private class MyPanel extends JPanel {
		public void paintComponent(Graphics g) {
			super.paintComponent(g);
			Graphics2D g2 = (Graphics2D) g;
			g2.translate(width / 2, height / 2);
			draw(g2);
		}

		/**
		 * Draws the spiral and adds to time.
		 */
		public void draw(Graphics2D g) {
			spiral(2, 1000, g);
			time += dt;
		}

		/**
		 * Recursive method that creates the spiral and rotates the pattern accordingly.
		 * Draws a 2D Ellipse then changes the location according to the math
		 * calculated.
		 * 
		 * @param size
		 * @param level
		 * @param g
		 */
		public void spiral(int size, int level, Graphics2D g) {
			if (level > 0) {
				if (level % 2 == 0) {
					g.setColor(new Color((int) (100 + Math.random() * 100), (int) (100 + Math.random() * 100),
							(int) (100 + Math.random() * 100)));
					g.draw(new Ellipse2D.Double(0, 0, size * 50, size * 50));
					g.translate(size, 0);
					g.rotate(0.09 * Math.sin(level * time * 4)); // speed
					spiral(size, level - 2, g);
				} else {
					g.setColor(new Color((int) (50 + Math.random() * 100), (int) (50 + Math.random() * 100),
							(int) (50 + Math.random() * 100)));
					g.draw(new Ellipse2D.Double(0, 0, size * 50, size * 50));
					g.translate(-size, 0);
					g.rotate(0.09 * Math.sin(level * time * 4));
					spiral(size, level - 2, g);
				}
			}
		}
	}
	/**
	 * Repaints the JFrame every 1 second.
	 */
	public void actionPerformed(ActionEvent e) {
		repaint();// this will call at every 1 second
	}

}
