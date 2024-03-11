import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = in.readLine().split(" ");
		int m = Integer.parseInt(str[0]);
		int n = Integer.parseInt(str[1]);
		
		String[][] chess = new String[m][n];
		
		for (int i=0; i<m; i++) {
			str = in.readLine().split("");
			chess[i] = str;
		}
		in.close();
		
		String[] bw = {"B","W"};
		
		int min = 64;
		int count; 
		
		for (int i = 0; i<m-7; i++) {
			for (int j = 0; j<n-7; j++) {
				count = 0;
				for (int k = i; k<i+8; k++) {
					for (int l = j; l<j+8; l++) {
						//System.out.println(bw[(k+l)%2]);
						if (chess[k][l].equals(bw[(k+l)%2]) == false) {
							count++;
						}
					}
				}
				if (count < min) min = count;
				
				count = 0;
				for (int k = i; k<i+8; k++) {
					for (int l = j; l<j+8; l++) {
						//System.out.println(bw[(k+l+1)%2]);
						if (chess[k][l].equals(bw[(k+l+1)%2]) == false) {
							count++;
						}
					}
				}
				if (count < min) min = count;
			}
		}
		System.out.println(min);
	}
}