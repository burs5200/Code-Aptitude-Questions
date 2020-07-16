
import java.io.*;
import java.util.Scanner;

class Solution {
	
  public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		long X = sc.nextLong();
		long S = sc.nextLong();
		
		long A = (S-X);
		if (A%2 == 1) {
		    System.out.println("none");
		    return;
		}
		A = A >> 1;
		
		int answers = 1;
		for(int i = 1; i <= 64; i++) {
		    int xi =(int) (X & 1); // obtain LSB of XOR
		    int ai = (int) (A & 1); // obtain LSB of AND
		    
		    // XOR bit is 1, AND bit is 0 which means two number bits can be either 0 and 1 OR 1 and 0
		    if (xi == 1 && ai == 0){
                
                answers *= 2;
                System.out.println("Answers = " +answers);
            } 
		    // XOR bit is 1, AND bit is 1 , which means there can't be such numbers
		    else if (xi == 1 && ai == 1) {
		        System.out.println("none");
		        return;
		    }
		    // XOR bit is 0, AND bit is 0, there can be only one choice: 0 and 0, 
		    // XOR bit is 0, AND bit is 1, there can be only one choice: 1 and 1
            X = X >> 1;
            System.out.println("X= " + X);
            A = A >> 1;
            System.out.println("A="+A);
		}
		System.out.println(answers + " Pairs");
	}
}