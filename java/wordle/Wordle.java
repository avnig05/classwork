package Wordle;
/**
 * Wordle.java
 * 
 * Recreates the famous Wordle game by The New York Times.
 * Picks a random 5 letter word from a text file and the
 * game play is very similar to the actual version. The
 * player can play as many times as they want to and are
 * not limited to just one word a day.
 *
 * @author Avni Gandhi
 * @version 1.0
 * @since 3/28/2022
 */
 
import java.awt.Font;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.Scanner;

import javax.swing.JDialog;
import javax.swing.JOptionPane;

public class Wordle {
	/** A String to store the word that the player is trying to find. */
	private String word;

	/** An array of String to store the guesses that have been made. */
	private String[] wordGuess;

	/**
	 * A String to store the letters in the current guess. Can have from 0 to 5
	 * chars
	 */
	private String letters;

	/**
	 * A variety of boolean variables to turn things on and off. These include: show
	 * - when true, will print the current word to the terminal, when false, will
	 * not print the word. readyForKeyInput - when true, will accept keyboard input,
	 * when false, will not accept keyboard input. readyForMouseInput - when true,
	 * will accept mouse input, when false, will not accept mouse input. activeGame
	 * - when false, will only accept action on the RESET button.
	 */
	private boolean show, readyForKeyInput, readyForMouseInput, activeGame, wordInAllowedFile;

	/**
	 * An array to determine how to color the keyboard at the bottom of the
	 * gameboard. 0 for not checked yet, 1 for no match, 2 for partial, 3 for exact
	 */
	private int[] keyBoardColors;
;
	/**
	 * Creates a Wordle object. A 2-args constructor. Initializes all of the
	 * variables by calling the method initAll.
	 * 
	 * @param showIt   if showIt is equal to "show", will print the word to the
	 *                 terminal
	 * @param testWord if this String is found in words5allowed.txt, it will be used
	 *                 to set word.
	 */
	public Wordle(String showIt, String testWord) {
		show = false;
		if (showIt.equalsIgnoreCase("show"))
		{
			show = true;
		}
		initAll(testWord);
	}

	/**
	 * Initializes all fields. Calls openFileAndChooseWord to choose the word. Sets
	 * all of the keyboard colors to light gray to start.
	 * 
	 * @param testWord if this String is found in words5allowed.txt, it will be used
	 *                 to set word.
	 */
	public void initAll(String testWord) {
		wordGuess = new String[6]; // THIS METHOD IS COMPLETE.
		for (int i = 0; i < wordGuess.length; i++) {
			wordGuess[i] = new String("");
		}
		letters = "";
		readyForKeyInput = activeGame = true;
		readyForMouseInput = false;
		keyBoardColors = new int[29];
		word = openFileAndChooseWord("words5.txt", testWord);
	//	word = openFileAndChooseWord("/Users/avnigandhi/eclipse-workspace/Class 11/src/Wordle/words5.txt", testWord);
	}

	/**
	 * The main method, to run the program. The constructor is called, so that all
	 * of the fields are initialized. The canvas is set up, and the GUI (the game of
	 * Wordle) runs.
	 */
	public static void main(String[] args)
	{
		String showIt = new String("");
		String testWord = new String(""); 
		if (args.length >= 1) {
			showIt = args[0];
		}
		if (args.length >= 2) {
			testWord = args[1];
		}
		Wordle run = new Wordle(showIt, testWord);
		run.setUpCanvas();
		run.playGame();
	}

	/**
	 * Sets up the canvas. Enables double buffering so that the gameboard is drawn
	 * offscreen first, then drawn to the gameboard when everything is ready (with
	 * the show method).
	 */
	public void setUpCanvas() {
		StdDraw.setCanvasSize(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT);
		StdDraw.setXscale(0, Constants.SCREEN_WIDTH);
		StdDraw.setYscale(0, Constants.SCREEN_HEIGHT);

		StdDraw.enableDoubleBuffering();
	}

	/**
	 * Runs the game. An endless loop is created, constantly cycling and looking for
	 * user input.
	 */
	public void playGame() {
		boolean keepGoing = true;
		while (keepGoing) {
			if (activeGame)
			{
				drawPanel();
			}
			update();
		}
	}

	/**
	 * If the testWord is valid, it is used as the "goal word". If it is not, then
	 * the text file is opened, and a word is chosen at random from the list to be
	 * the "goal word". If the field variable show is true, it will print the chosen
	 * word to the terminal window.
	 * 
	 * @param inFileName this file is to be opened, and a random word is to be
	 *                   chosen from it.
	 * @param testWord   if this String is found in words5allowed.txt, it will be
	 *                   used to set word.
	 * @return the word chosen as the "goal word".
	 */
	public String openFileAndChooseWord(String inFileName, String testWord) {
		ArrayList<String> words = new ArrayList<String>();
		Scanner infile = OpenFile.openToRead(inFileName);
		String line1 = "";
		while (infile.hasNext()) {
			line1 = infile.nextLine().toUpperCase();
			words.add(line1);
		}

		ArrayList<String> wordsAllowed = new ArrayList<String>();
		Scanner infile2 = OpenFile.openToRead("words5allowed.txt");
//		Scanner infile2 = OpenFile.openToRead("/Users/avnigandhi/eclipse-workspace/Class 11/src/Wordle/words5allowed.txt");
		String line2 = "";
		while (infile2.hasNext()) {
			line2 = infile2.nextLine().toUpperCase();
			wordsAllowed.add(line2);
			if(testWord.toUpperCase().equals(line2))
			{
				if(show)
				{
					System.out.println(testWord);
				}
				return testWord;
			}
		}
		int index = (int) (Math.random() * words.size());
		String result = words.get(index);
		if(show)
		{
			System.out.println(result);
		}
		return result;
	}

	/**
	 * Draws the entire game panel. This includes the guessed words, the current
	 * word being guessed, and all of the letters in the "keyboard" at the bottom of
	 * the gameboard. The correct colors will need to be chosen for every letter.
	 */
	public void drawPanel() {
		StdDraw.clear(StdDraw.WHITE);
		Font font = new Font("Arial", Font.BOLD, 12);
		StdDraw.setFont(font);
		StdDraw.picture(Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT - 30, "wordle.png");
		StdDraw.setPenColor(StdDraw.LIGHT_GRAY);
		int place = 0;
		for (int[] pair : Constants.KEYPLACEMENT) {
			if (place == 19 || place == 27 || place == 28) {
				StdDraw.picture(pair[0], pair[1], "keyBackgroundBig.png");
			} 
			else {
				StdDraw.picture(pair[0], pair[1], "keyBackground.png");
			}
			StdDraw.setPenColor(StdDraw.BLACK);
			StdDraw.text(pair[0], pair[1], Constants.KEYBOARD[place]);
			place++;
		}
		drawAllLettersGuessed();
		StdDraw.show();
		StdDraw.pause(Constants.DRAW_DELAY);
		checkIfWonOrLost();
	}

	/**
	 * This method is called by drawPanel, and draws all of the letters in the
	 * guesses made by the user.
	 */
	public void drawAllLettersGuessed() {
		for (int row = 0; row < 6; row++) {
			for (int col = 0; col < 5; col++) {
				if (wordGuess[row].length() != 0)
				{
					int keyPlace = getKeyPlace(wordGuess[row].charAt(col));
					if(wordGuess[row].charAt(col) == word.charAt(col))
					{
						StdDraw.picture(209 + col * 68, 650 - row * 68, "letterFrameGreen.png");
						colorCodeKeyboard(keyPlace, "keyBackgroundGreen.png");
					}
					else if(word.indexOf(wordGuess[row].charAt(col)) > -1)
					{	
						boolean isYellow = findCellColor(row, col);
						if (isYellow) {
							StdDraw.picture(209 + col * 68, 650 - row * 68, "letterFrameYellow.png");
							colorCodeKeyboard(keyPlace, "keyBackgroundYellow.png");
						} else {
							StdDraw.picture(209 + col * 68, 650 - row * 68, "letterFrameDarkGray.png");
						}
					}
					else
					{
						StdDraw.picture(209 + col * 68, 650 - row * 68, "letterFrameDarkGray.png");
						colorCodeKeyboard(keyPlace, "keyBackgroundDarkGray.png");
					}
				} else {
					StdDraw.picture(209 + col * 68, 650 - row * 68, "letterFrame.png");
				}
			}
		}
		if (wordGuess[wordGuess.length - 1].length() == 5) {
			activeGame = false;
		}
		Font font = new Font("Arial", Font.BOLD, 34);
		StdDraw.setFont(font);
		int guessNumber = 0;
		for (int i = 0; i < wordGuess.length; i++) {
			if (wordGuess[i].length() > 0) {
				for (int j = 0; j < wordGuess[i].length(); j++) {
					StdDraw.text(209 + j * 68, 644 - i * 68, "" + wordGuess[i].charAt(j));
				}
			}
			if (wordGuess[i].length() == 5) {
				guessNumber = i + 1;
			}
		}
		
		for (int i = 0; i < letters.length(); i++) {
			StdDraw.text(209 + i * 68, 644 - guessNumber * 68, "" + letters.substring(i, i + 1));
		}
	}

	private boolean findCellColor(int row, int col) {
		boolean isYellow = false;
		char c1 = wordGuess[row].charAt(col);
		for (int ii = 0; ii < 5; ii++) {
			char c2 = word.charAt(ii);
			char c3 = wordGuess[row].charAt(ii);
			if ((c2 != c3) && (c1 == c2)) {
				isYellow = true;
			} else if (c1 == c2) {
				isYellow = false;
			}
		}
		for (int ii = 4; ii >= 0; ii--) {
			char c2 = word.charAt(ii);
			char c3 = wordGuess[row].charAt(ii);
			if ((c2 != c3) && (c1 == c2)) {
				isYellow = true;
			} else if (c1 == c2) {
				isYellow = false;
			}
		}
		return isYellow;
	}

	private void colorCodeKeyboard(int currPlace, String imageName) {
		int place = 0;
		for (int[] pair : Constants.KEYPLACEMENT) {
			if (place == currPlace) {
				StdDraw.picture(pair[0], pair[1], imageName);
				StdDraw.setPenColor(StdDraw.BLACK);
				StdDraw.text(pair[0], pair[1], Constants.KEYBOARD[place]);
			} 
			place++;
		}		
	}
	
	private int getKeyPlace(char c) {
		for (int ii=0; ii < Constants.KEYBOARD.length; ii++) {
			if (c == Constants.KEYBOARD[ii].charAt(0)) {
				return ii;
			}
		}
		return -1;
	}
	/**
	 * Checks to see if the game has been won or lost. The game is won if the user
	 * enters the correct word with a guess. The game is lost when the user does not
	 * enter the correct word with the last (6th) guess. An appropriate message is
	 * displayed to the user in the form of a JOptionPane with JDialog for a win or
	 * a loss.
	 */
	public void checkIfWonOrLost() {
		String lastWord = "";
		for (int i = 0; i < wordGuess.length; i++) {
			if (wordGuess[i].length() == 5) {
				lastWord = wordGuess[i]; 
			}
		}
		if (lastWord.length() == 5) {
			if (lastWord.equals(word)) {
				activeGame = false;
				JOptionPane pane = new JOptionPane(lastWord + " is the word!  Press RESET to begin again");
				JDialog d = pane.createDialog(null, "CONGRATULATIONS!");
				d.setLocation(365, 250);
				d.setVisible(true);
			} else if (wordGuess[wordGuess.length - 1].length() == 5) {
				activeGame = false;
				JOptionPane pane = new JOptionPane(word + " was the word!  Press RESET to begin again");
				JDialog d = pane.createDialog(null, "Sorry!");
				d.setLocation(365, 250);
				d.setVisible(true);
			}
		}
	}


	/**
	 * This method is constantly looking for keyboard or mouse input from the user,
	 * and reacting to this input.
	 */
	public void update() {
		if (activeGame) {
			respondToKeys();
		}
		respondToMouse();
	}

	/**
	 * Responds to input from the keyboard. Will call the method processGuess when
	 * the user has entered a word to guess.
	 */
	public void respondToKeys() {
		if (readyForKeyInput && StdDraw.hasNextKeyTyped() && StdDraw.isKeyPressed(KeyEvent.VK_BACK_SPACE)
				&& letters.length() > 0) {
			letters = letters.substring(0, letters.length() - 1);
			readyForKeyInput = false;
		} else if (readyForKeyInput && StdDraw.hasNextKeyTyped() && StdDraw.isKeyPressed(KeyEvent.VK_ENTER)
				&& letters.length() == 5) {
			processGuess();
			readyForKeyInput = false;
		} else if (readyForKeyInput && StdDraw.hasNextKeyTyped() && letters.length() < 5) {
			String letter = "" + StdDraw.nextKeyTyped();
			letter = letter.toUpperCase();
			if (letter.charAt(0) >= 'A' && letter.charAt(0) <= 'Z') {
				letters += letter;
			}
			readyForKeyInput = false;
		} else {
			while (StdDraw.hasNextKeyTyped()) {
				StdDraw.nextKeyTyped();
			}
			if (!StdDraw.hasNextKeyTyped()) {
				readyForKeyInput = true;
			}
		}
	}

	/**
	 * Responds to input from the mouse, simulating the typing of keys on the
	 * "keyboard" at the bottom of the game panel. Will call the method processGuess
	 * when the user has entered a word to guess.
	 */
	public void respondToMouse() {
		if (readyForMouseInput && StdDraw.isMousePressed()) {
			for (int i = 0; i < Constants.KEYPLACEMENT.length; i++) {
				if (StdDraw.mouseX() > Constants.KEYPLACEMENT[i][0] - 22
						&& StdDraw.mouseX() < Constants.KEYPLACEMENT[i][0] + 22
						&& StdDraw.mouseY() > Constants.KEYPLACEMENT[i][1] - 29
						&& StdDraw.mouseY() < Constants.KEYPLACEMENT[i][1] + 29) {
					if (i == 28) {
						initAll("");
						activeGame = true;
					} else if (activeGame && i == 27 && letters.length() > 0) 
					{
						letters = letters.substring(0, letters.length() - 1);
					} else if (activeGame && i == 19 && letters.length() == 5) {
						processGuess();
					} else if (activeGame && i != 19 && i != 27 && i != 28 && letters.length() < 5) {
						String letter = Constants.KEYBOARD[i].toUpperCase();
						letters += letter;
					}
				}
			}
			readyForMouseInput = false;
		} else if (!StdDraw.isMousePressed()) {
			readyForMouseInput = true;
		}
	}

	/**
	 * Processes the guess made by the user. This method will only be called if the
	 * field variable letters has length 5. The guess in letters will need to be
	 * checked against the words in words5allowed.txt. The method inAllowedWordFile
	 * will be called for this task. If the guess in letters does not exist in the
	 * text file, a message is displayed to the user in the form of a JOptionPane
	 * with JDialog.
	 */
	public void processGuess() {
		if (!inAllowedWordFile(letters.toUpperCase())) {
			JOptionPane pane = new JOptionPane(letters.toUpperCase() + " not in word list");
			JDialog d = pane.createDialog(null, "INVALID INPUT");
			d.setLocation(365, 250);
			d.setVisible(true);			
			return;
		}
		
		int guessNumber = 0;
		for (int i = 0; i < wordGuess.length; i++) {
			if (wordGuess[i].length() == 5)
			{
				guessNumber = i + 1;
			}
		}
		wordGuess[guessNumber] = letters.toUpperCase();
		letters = "";
	}

	/**
	 * Checks to see if the word in the parameter list is found in the text file
	 * words5allowed.txt Returns true if the word is in the file, false otherwise.
	 * 
	 * @param possibleWord the word to looked for in words5allowed.txt
	 * @return true if the word is in the text file, false otherwise
	 */
	public boolean inAllowedWordFile(String possibleWord) {
		Scanner reader = OpenFile.openToRead("words5allowed.txt");
		//Scanner reader = OpenFile.openToRead("/Users/avnigandhi/eclipse-workspace/Class 11/src/Wordle/words5allowed.txt");
		while (reader.hasNext()) {
			String line = reader.nextLine().toUpperCase();
			if (possibleWord.equals(line)) {
				return true;
			}
		}
		return false;
	}
}