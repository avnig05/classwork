
/**
 * Pegs.java
 * This program is a game of Peg Solitaire, The player is able to press the 
 * mouse anywhere on the surface of the GUI created. Once an active peg has
 * been chosen, the player should then be able to press the destination cell.
 * The active peg jumps and removes the adjacent peg. At any time of the game,
 * the player can reset the the peg board by clicking the reset button. If
 * there are no more moves left and only one peg exists on the board, the 
 * player has won, else the player loses.
 * @author Avni Gandhi
 * @version 1.0
 * @since 1/24/2022
 */
import java.awt.Color;

import java.awt.Font;

public class Pegs {
	/**
	 * The board object. 1 represents a peg on the board, 0 is an empty space, and
	 * -1 would indicate that this cell is not part of the board.
	 */
	private int[][] board;

	/** How long the GUI should pause, before expecting new input. */
	private int pause;

	/**
	 * Current x and y values of the user's choice. The x values count the cells
	 * from the lower left to the right, while the y values count the cells from the
	 * bottom left up.
	 */
	private int xposition, yposition;

	/**
	 * Creates a Pegs object, with the font to be used, current position initially
	 * pause off the board, pause at 50 milliseconds, and the board values
	 * initialized in a 9 x 9 grid.
	 */
	public Pegs() {
		Font font = new Font("Arial", Font.BOLD, 18);
		StdDraw.setFont(font);
		xposition = yposition = -5;
		pause = 50;
		board = new int[][] { { -1, -1, -1, 1, 1, 1, -1, -1, -1 }, { -1, -1, -1, 1, 1, 1, -1, -1, -1 },
				{ -1, -1, -1, 1, 1, 1, -1, -1, -1 }, { 1, 1, 1, 1, 1, 1, 1, 1, 1 }, { 1, 1, 1, 1, 0, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1 }, { -1, -1, -1, 1, 1, 1, -1, -1, -1 }, { -1, -1, -1, 1, 1, 1, -1, -1, -1 },
				{ -1, -1, -1, 1, 1, 1, -1, -1, -1 } };
	}

	/**
	 * Sets up and runs the game of Pegs.
	 * 
	 * @param args An array of String arguments (not used here).
	 */
	public static void main(String[] args) {
		Pegs run = new Pegs();
		run.playGame();
	}

	/**
	 * Do-while loop that calls the possibleMoveSpace method and shows the peg
	 * board. Calculates the coordinates of the peg that has been clicked and find
	 * the coordinates where the peg can move.
	 */
	public void playGame() {
		StdDraw.enableDoubleBuffering();
		boolean done = false;
		do {
			drawBoard();
			if (StdDraw.isMousePressed()) {
				double x = StdDraw.mouseX();
				double y = StdDraw.mouseY();
				int checkx = (int) (10 * x - 0.5);
				int checky = (int) (10 * y - 0.5);
				System.out.println(x + " " + y + " " + checkx + " " + checky);
				if (reset(x, y)) {
					xposition = yposition = -5;
				} else if (possibleMoveSpace(xposition, yposition, checkx, checky)) {
					board[xposition][yposition] = 0;
					board[(xposition + checkx) / 2][(yposition + checky) / 2] = 0;
					board[checkx][checky] = 1;

					StdDraw.show();
					StdDraw.pause(4 * pause);
				} else {
					xposition = checkx;
					yposition = checky;
					StdDraw.show();
					StdDraw.pause(pause);
				}
			}
			StdDraw.show();
			StdDraw.pause(pause);
		} while (!done);
	}

	/**
	 * Draws the peg solitaire board. Draws the win or lose message when the game is
	 * finished.
	 */
	public void drawBoard() {
		StdDraw.setPenColor(new Color(0, 0, 0));
		StdDraw.filledSquare(0.5, 0.5, 0.5);
		StdDraw.setPenColor(new Color(120, 120, 120));
		StdDraw.filledSquare(0.5, 0.5, 0.475);
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				if (board[i][j] != -1) {
					drawCell(i, j);
				}
			}
		}
		drawResetButtons();
		if (gameIsFinished()) {
			drawWinOrLoseMessage();
		}

	}

	/**
	 * Draws the reset buttons at the bottom of the GUI.
	 */
	public void drawResetButtons() {
		StdDraw.setPenColor(new Color(0, 0, 0));
		StdDraw.filledRectangle(0.8, 0.25, 0.125, 0.05);
		StdDraw.setPenColor(new Color(255, 255, 255));
		StdDraw.text(0.8, 0.25, "RESET 7 x 7");

		StdDraw.setPenColor(new Color(0, 0, 0));
		StdDraw.filledRectangle(0.8, 0.12, 0.125, 0.05);
		StdDraw.setPenColor(new Color(255, 255, 255));
		StdDraw.text(0.8, 0.12, "RESET 9 x 9");
	}

	/**
	 * Draws the win or lose message when the game is finished. If the number of
	 * pegs on the board is 1, the you win message is drawn.
	 */
	public void drawWinOrLoseMessage() {
		if (countPegs() == 1) {
			StdDraw.setPenColor(new Color(0, 0, 0));
			StdDraw.filledRectangle(0.2, 0.8, 0.125, 0.05);
			StdDraw.setPenColor(new Color(255, 255, 255));
			StdDraw.text(0.2, 0.8, "YOU WIN!");
		} else {
			StdDraw.setPenColor(new Color(0, 0, 0));
			StdDraw.filledRectangle(0.2, 0.8, 0.125, 0.05);
			StdDraw.setPenColor(new Color(255, 255, 255));
			StdDraw.text(0.2, 0.8, "YOU LOSE!");
		}

	}

	/**
	 * Resets the board depending on the users choice. If the user chooses the 7 by
	 * 7 box, the peg board is changed and vice versa.
	 */
	public boolean reset(double x, double y) {
		if ((x >= 0.625 && x <= 0.925) && (y >= 0.2 && y <= 0.3)) {
			board = new int[][] { { -1, -1, -1, -1, -1, -1, -1, -1, -1 }, { -1, -1, -1, 1, 1, 1, -1, -1, -1 },
					{ -1, -1, -1, 1, 1, 1, -1, -1, -1 }, { -1, 1, 1, 1, 1, 1, 1, 1, -1 },
					{ -1, 1, 1, 1, 0, 1, 1, 1, -1 }, { -1, 1, 1, 1, 1, 1, 1, 1, -1 },
					{ -1, -1, -1, 1, 1, 1, -1, -1, -1 }, { -1, -1, -1, 1, 1, 1, -1, -1, -1 },
					{ -1, -1, -1, -1, -1, -1, -1, -1, -1 } };
			return true;
		} else if ((x >= 0.625 && x <= 0.925) && (y >= 0.07 && y <= 0.17)) {
			board = new int[][] { { -1, -1, -1, 1, 1, 1, -1, -1, -1 }, { -1, -1, -1, 1, 1, 1, -1, -1, -1 },
					{ -1, -1, -1, 1, 1, 1, -1, -1, -1 }, { 1, 1, 1, 1, 1, 1, 1, 1, 1 }, { 1, 1, 1, 1, 0, 1, 1, 1, 1 },
					{ 1, 1, 1, 1, 1, 1, 1, 1, 1 }, { -1, -1, -1, 1, 1, 1, -1, -1, -1 },
					{ -1, -1, -1, 1, 1, 1, -1, -1, -1 }, { -1, -1, -1, 1, 1, 1, -1, -1, -1 } };
			return true;
		}
		return false;
	}

	/**
	 * Draws the pegs on the peg board.
	 */
	public void drawCell(int x, int y) {
		StdDraw.setPenColor(new Color(0, 0, 0));
		StdDraw.filledSquare(0.1 + 0.1 * x, 0.1 + 0.1 * y, 0.055);
		StdDraw.setPenColor(new Color(255, 255, 255));
		StdDraw.filledSquare(0.1 + 0.1 * x, 0.1 + 0.1 * y, 0.0425);
		StdDraw.setPenColor(new Color(200, 200, 200));
		StdDraw.filledCircle(0.1 + 0.1 * x, 0.1 + 0.1 * y, 0.02);
		if (x == xposition && y == yposition && board[x][y] == 1) {
			StdDraw.setPenColor(new Color(0, 0, 0));
			StdDraw.filledSquare(0.1 + 0.1 * x, 0.1 + 0.1 * y, 0.05);
			StdDraw.setPenColor(new Color(230, 30, 30));
			StdDraw.filledCircle(0.1 + 0.1 * x, 0.1 + 0.1 * y, 0.04);
		}
		if (possibleMoveSpace(xposition, yposition, x, y)) {
			StdDraw.setPenColor(new Color(0, 0, 0));
			StdDraw.filledSquare(0.1 + 0.1 * x, 0.1 + 0.1 * y, 0.05);
			StdDraw.setPenColor(new Color(230, 30, 30));
			StdDraw.filledCircle(0.1 + 0.1 * x, 0.1 + 0.1 * y, 0.03);
		}
		if (board[x][y] == 1) {
			// StdDraw.picture(0.1 + 0.1 * x, 0.1 + 0.1 * y,"peg.png");
			StdDraw.picture(0.1 + 0.1 * x, 0.1 + 0.1 * y, "/Users/avnigandhi/eclipse-workspace/Class 11/src/peg.png");
		}
	}

	/**
	 * Checks if the peg that is chosen by the user can be moved to another location
	 * on the peg board.
	 */
	public boolean possibleMoveSpace(int x, int y, int xval, int yval) {
		if (xval < 0 || xval >= board.length || yval < 0 || yval >= board.length) {
			return false;
		}
		if (board[xval][yval] != 0) {
			return false;
		}
		if (board[(xval + x) / 2][(yval + y) / 2] != 1) { // The middle location or next to selected peg should be 1
			return false;
		}
		if (board[x][y] != 1) {
			return false;
		}
		if ((Math.abs(x - xval) == 2 && y == yval) || (Math.abs(y - yval) == 2 && x == xval)) {
			return true;
		}
		return false;
	}

	/**
	 * Checks to see if the game is finished by checking if the pegs on the board
	 * can be moved.
	 */
	public boolean gameIsFinished() {
		if (countPegs() == 1) {
			return true;
		}
		for (int x = 0; x < board.length; x++) {
			for (int y = 0; y < board[x].length; y++) {
				if (board[x][y] == 1) {
					if (possibleMoveSpace(x, y, x + 2, y) || possibleMoveSpace(x, y, x - 2, y)
							|| possibleMoveSpace(x, y, x, y + 2) || possibleMoveSpace(x, y, x, y - 2)) {
						return false;
					}
				}
			}
		}
		return true;
	}

	/**
	 * Counts the number of pegs on the board.
	 */
	public int countPegs() {
		int count = 0;
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				if (board[i][j] == 1) {
					count++;
				}
			}
		}
		return count;
	}
}