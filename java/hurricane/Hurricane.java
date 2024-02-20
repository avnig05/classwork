
/**
* Hurricane.java
* Creates a map of the United States (lower 48),
* using a text file that contains information
* for US cities. The name of the text file is
* cities.txt, and each line of this file has:
* zip,state,city,latitude,longitude
* OpenFile is used to open the text file, and
* each line is read, with latitude and longitude
* information parsed from the line. These
* values are then plotted on canvas. The class
* StdDraw is used to create the canvas. After the
* map of the US is created, information from another
* text file (like f.txt) is used to animate
* the progress of a hurricane. An animation is
* created, and a path is displayed, as the
* hurricane tracks its path on the canvas.
*
* @author Avni Gandhi
* @version 1.0
* @since 9/16/2021
*/

import java.awt.Color;
import java.awt.Font;
import java.util.Scanner;

public class Hurricane {
	/** The name of the text file, containing data about the hurricane. */
	private String fileName;
	/** The pause duration, in milliseconds, between views of the storm. */
	private int pause;

	/**
	 * Creates a Hurricane object.
	 * 
	 * @param file The name of the text file to be used.
	 * @param p    The pause time, in milliseconds.
	 */
	public Hurricane(String file, int p) {
		fileName = new String(file);
		pause = p;
	}

	/**
	 * The main method, to create the map of the US, then track the hurricane.
	 */
	public static void main(String[] args) {
		int p = 200;
		String fileName = "/Users/avnigandhi/eclipse-workspace/Class 11/src/f.txt";
		if (args.length >= 1) {
			fileName = args[0];
		}
		if(args.length == 2)
		{
			p = Integer.parseInt(args[1]);
		}
		
		
		Hurricane run = new Hurricane(fileName, p);
	
		run.setUpCanvas();
		run.loadUSA();
		run.showIt();
		run.legend();
		run.animateStorm();
	}

	/**
	 * Sets up the canvas, using methods from StdDraw. This includes setting up the
	 * canvas size, the horizontal scale (Xscale), and the vertical scale (Yscale).
	 * We will enable double buffering, in anticipation of running an animation.
	 * Also, the pen radius should be relatively small, and the dots should be dark
	 * gray.
	 */
	public void setUpCanvas() {
		StdDraw.setCanvasSize(1100, 500);
		StdDraw.setXscale(125.0, 15.0); // Related to the longitude
		StdDraw.setYscale(10.0, 50.0); // Related to the latitude

		StdDraw.enableDoubleBuffering();
		StdDraw.setPenRadius(0.0075);
		StdDraw.setPenColor(StdDraw.DARK_GRAY);
	}

	/**
	 * Opens the file (cities.txt), and reads in the data one line at a time. The
	 * data in cities.txt is of the form: zip,state,city,latitude,longitude The code
	 * here makes use of String methods, along with Double.parseDouble, to split up
	 * the String, and pull out the latitude and longitude. These values are then
	 * used to plot points on the canvas, using StdDraw.point(horizontal,vertical).
	 */
	public void loadUSA() {
		double diameter = 0.15;
		StdDraw.setPenColor(new Color(50, 50, 50));

		// Scanner infile = OpenFile.openToRead("cities.txt");
		Scanner infile = OpenFile.openToRead("/Users/avnigandhi/eclipse-workspace/Class 11/src/cities2.txt");
		while (infile.hasNext()) {
			String line = infile.nextLine();

			int index1 = line.indexOf(",");
			String part1 = line.substring(index1 + 1);

			int index2 = part1.indexOf(",");
			String part2 = part1.substring(index2 + 1);

			int index3 = part2.indexOf(",");
			String part3 = part2.substring(index3 + 1);

			String num1 = part3.substring(0, part3.indexOf(","));

			String num2 = part3.substring(part3.indexOf(" ") + 1, part3.length() - 1);

			float yCoord = Float.parseFloat(num1);

			float xCoord = Float.parseFloat(num2);

			StdDraw.filledEllipse(xCoord, yCoord, diameter, diameter);

		}
		infile.close();
	}
	
	/**
	 * Prints the image to the screen (image is saved offscreen before the reveal
	 * here).
	 */
	public void showIt() {

		StdDraw.show();
	}

	/**
	 * Creates a legend, in the lower left-hand corner of the screen. This legend
	 * describes the different stages (or levels) of a storm, from Disturbance to
	 * Hurricane 5.
	 */
	public void legend() {
		StdDraw.setPenRadius(0.04);
		StdDraw.setPenColor(new Color(0, 0, 0));
		StdDraw.filledRectangle(112.7, 19.6, 15.8, 9.2);
		StdDraw.setPenColor(new Color(255, 255, 255));
		StdDraw.filledRectangle(112.7, 19.6, 15.6, 9);
		StdDraw.setPenColor(new Color(255, 60, 60));
		StdDraw.picture(122.6, 27.3, "hurricane.png", 135);
		StdDraw.point(122.6, 27.3);
		StdDraw.setPenColor(new Color(255, 150, 20));
		StdDraw.picture(122.6, 25.1, "hurricane.png", 135);
		StdDraw.point(122.6, 25.1);
		StdDraw.setPenColor(new Color(255, 210, 40));
		StdDraw.picture(122.6, 22.9, "hurricane.png", 135);
		StdDraw.point(122.6, 22.9);
		StdDraw.setPenColor(new Color(255, 235, 75));
		StdDraw.picture(122.6, 20.7, "hurricane.png", 135);
		StdDraw.point(122.6, 20.7);
		StdDraw.setPenColor(new Color(255, 255, 180));
		StdDraw.picture(122.6, 18.5, "hurricane.png", 135);
		StdDraw.point(122.6, 18.5);
		StdDraw.setPenColor(new Color(0, 250, 240));
		StdDraw.picture(122.6, 16.3, "hurricane.png", 135);
		StdDraw.point(122.6, 16.3);
		StdDraw.setPenColor(new Color(95, 185, 255));
		StdDraw.picture(122.6, 14.1, "hurricane.png", 135);
		StdDraw.point(122.6, 14.1);
		StdDraw.setPenColor(new Color(80, 200, 255));
		StdDraw.picture(122.6, 11.9, "hurricane.png", 135);
		StdDraw.point(122.6, 11.9);
		StdDraw.setPenColor(new Color(0, 0, 0));
		Font font = new Font("Arial", Font.BOLD, 13);
		StdDraw.setFont(font);
		StdDraw.textLeft(121, 27.3, "Hurricane 5, Winds > 155");
		StdDraw.textLeft(121, 25.1, "Hurricane 4, 130 < Winds < 155");
		StdDraw.textLeft(121, 22.9, "Hurricane 3, 110 < Winds < 130");
		StdDraw.textLeft(121, 20.7, "Hurricane 2, 95 < Winds < 110");
		StdDraw.textLeft(121, 18.5, "Hurricane 1, 75 < Winds < 95");
		StdDraw.textLeft(121, 16.3, "Storm, 35 < Winds < 75");
		StdDraw.textLeft(121, 14.1, "Depression, 15 < Winds < 35");
		StdDraw.textLeft(121, 11.9, "Disturbance, 0 < Winds < 15");
	}

	/**
	 * Animates the storm. Provide your own description here.
	 */

	public void animateStorm() {
		Scanner fText = OpenFile.openToRead(this.fileName);
		String date = null;
		String time = null;
		String lat = null;
		String lon = null;
		String mph = null;
		String mb = null;
		String type = null;
		String numMiles = null;
		while (fText.hasNext()) {
			String line = fText.nextLine();
			int firstComma = line.indexOf(',');
			date = line.substring(0, firstComma);

			int secondComma = line.indexOf(',', firstComma + 1);
			time = line.substring(firstComma + 1, secondComma).trim();

			int thirdComma = line.indexOf(',', secondComma + 1);
			lat = line.substring(secondComma + 1, thirdComma).trim();

			int fourthComma = line.indexOf(',', thirdComma + 1);
			lon = line.substring(thirdComma + 1, fourthComma).trim();

			double latitude = Double.parseDouble(lat);

			double longitude = Double.parseDouble(lon);

			int fifthComma = line.indexOf(',', fourthComma + 1);
			mph = line.substring(fourthComma + 1, fifthComma).trim();

			int space = line.indexOf(' ', fourthComma + 4);
			numMiles = line.substring(fourthComma + 1, space).trim();
			
			double milesPerHour = Double.parseDouble(numMiles);

			int sixthComma = line.indexOf(',', fifthComma + 1);
			mb = line.substring(fifthComma + 1, sixthComma).trim();

			type = line.substring(sixthComma + 1).trim();

			int seventhComma = line.indexOf(',', sixthComma + 1);
			if (seventhComma != -1) {
				type = line.substring(sixthComma + 1, seventhComma).trim();
			}

			StdDraw.setPenRadius(0.04);

			if (milesPerHour > 155) {
				StdDraw.setPenColor(new Color(255, 60, 60));
				StdDraw.picture(longitude, latitude, "hurricane.png", 360 * Math.random());
				StdDraw.point(longitude, latitude);
			}
			if (milesPerHour > 130 && milesPerHour <= 155) {
				StdDraw.setPenColor(new Color(255, 150, 20));
				StdDraw.picture(longitude, latitude, "hurricane.png", 360 * Math.random());
				StdDraw.point(longitude, latitude);
			}
			if (milesPerHour > 110 && milesPerHour <= 130) {
				StdDraw.setPenColor(new Color(255, 210, 40));
				StdDraw.picture(longitude, latitude, "hurricane.png", 360 * Math.random());
				StdDraw.point(longitude, latitude);
			}
			if (milesPerHour > 95 && milesPerHour <= 110) {
				StdDraw.setPenColor(new Color(255, 235, 75));
				StdDraw.picture(longitude, latitude, "hurricane.png", 360 * Math.random());
				StdDraw.point(longitude, latitude);
			}
			if (milesPerHour > 75 && milesPerHour <= 95) {
				StdDraw.setPenColor(new Color(255, 255, 180));
				StdDraw.picture(longitude, latitude, "hurricane.png", 360 * Math.random());
				StdDraw.point(longitude, latitude);
			}
			if (milesPerHour > 35 && milesPerHour <= 75) {
				StdDraw.setPenColor(new Color(0, 250, 240));
				StdDraw.picture(longitude, latitude, "hurricane.png", 360 * Math.random());
				StdDraw.point(longitude, latitude);
			}
			if (milesPerHour > 15 && milesPerHour <= 35) {
				StdDraw.setPenColor(new Color(95, 185, 255));
				StdDraw.picture(longitude, latitude, "hurricane.png", 360 * Math.random());
				StdDraw.point(longitude, latitude);
			}
			if (milesPerHour > 0 && milesPerHour <= 15) {
				StdDraw.setPenColor(new Color(80, 200, 255));
				StdDraw.picture(longitude, latitude, "hurricane.png", 360 * Math.random());
				StdDraw.point(longitude, latitude);
			}

			StdDraw.setPenColor(new Color(255, 255, 255));
			StdDraw.filledRectangle(40, 47, 23, 3);
			StdDraw.setPenColor(new Color(0, 0, 0));
			Font font = new Font("Arial", Font.BOLD, 40);
			StdDraw.setFont(font);

			StdDraw.textLeft(63, 47, date);
			StdDraw.textLeft(40, 47, time);

			StdDraw.show();
			StdDraw.pause(pause);
		}
	}
}
