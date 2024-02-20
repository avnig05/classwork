
/**
 * GeneFinder.java
 * 
 * Creates specific proteins from the original DNA strand by
 * converting the codons to amino acids. Finds the start
 * codon (ATG) and prints out the partial DNA sequence until
 * one of the stop codons is reached (TAA, TAG, TGA). Uses the
 * ArrayQueue class and Queue interface methods. No arrays or
 * arraylists are used in the make of this program.
 *
 * @author Avni Gandhi
 * @version 1.0
 * @since 3/10/2022
 */

import java.util.Scanner;

public class GeneFinder {
	private ArrayQueue<String> queue;
	private String fileName;
	private int count;

	public GeneFinder(String file) {
		queue = new ArrayQueue<String>();
		fileName = file;

	}

	public static void main(String[] args) {
		GeneFinder run = new GeneFinder("/Users/avnigandhi/eclipse-workspace/Class 11/src/dna.txt");
		// GeneFinder run = new GeneFinder("dna.txt");
		run.findProteins();
	}

	public void findProteins() {
		openFileAndProcessIt();
	}

	/**
	 * Opens the file and processes the text file by listing out the codons in rows
	 * of twelve. Then prints out the partial DNA sequence starting from the start
	 * codon to the end codon. Lastly prints out the amino acid sequence.
	 */
	public void openFileAndProcessIt() {
		Scanner infile = OpenFile.openToRead(fileName);
		String line = "";
		String codon = "";
		int counter = 0;
		int status = 0; // 0 - not started; 1 - started; 2 - completed;
		System.out.println("\n\n");
		while (infile.hasNext()) {
			line = infile.nextLine();
			for (int i = 0; i < line.length(); i++) {
				codon += line.substring(i, i + 1);
				if (codon.length() == 3) {
					if (codon.equals("ATG") && status == 0) {
						queue.add(codon);
						count++;
						status = 1;
					} else if ((codon.equals("TAG") || codon.equals("TAA") || codon.equals("TGA")) && status == 1) {
						queue.add(codon);
						status = 2;
					} else if (status == 1) {
						queue.add(codon);
					}

					System.out.print(codon + " ");
					codon = "";
					counter++;
					if (counter % 12 == 0) {
						System.out.println();
					}
					if (status == 2) {
						queue = printAndRebuild(queue);
						createAminoAcids(queue);
						status = 0;
						counter = 0;
					}
				}
			}
		}
		System.out.println("\n\n");
	}

	/**
	 * Prints the ArrayQueue of Strings (codons) and puts it back together in a new
	 * ArrayQueue. This ArrayQueue is returned.
	 * 
	 * @param q The ArrayQueue to be printed and rebuilt
	 * @return The ArrayQueue, containing the same Strings (codons) as the original
	 */
	public ArrayQueue<String> printAndRebuild(ArrayQueue<String> q) {
		ArrayQueue<String> temp = new ArrayQueue<String>();
		System.out.print("\n\n" + count + ": ");
		while (!q.isEmpty()) {
			temp.add(q.peek());
			System.out.print(q.remove());
		}
		System.out.println();
		return temp;
	}

	/**
	 * Creates a new ArrayQueue of amino acids from the codons in the ArrayQueue
	 * passed in.
	 * 
	 * @param q The ArrayQueue to be used to create the ArrayQueue of amino acids
	 * @return The ArrayQueue created, of amino acids.
	 */
	public ArrayQueue<String> createAminoAcids(ArrayQueue<String> q) {
		ArrayQueue<String> temp = new ArrayQueue<String>();
		System.out.print(count + ": ");
		while (!q.isEmpty()) {
			temp.add(q.peek());
			if (!GeneTools.codonToAminoAcid(q.peek()).equals("X")) {
				System.out.print(GeneTools.codonToAminoAcid(q.peek()));
			}
			q.remove();
		}
		System.out.println("\n");
		return temp;

	}
}