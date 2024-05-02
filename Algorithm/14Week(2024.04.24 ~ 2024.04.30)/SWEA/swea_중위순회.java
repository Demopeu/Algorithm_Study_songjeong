import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static char arr[];
    
    public static void main(String[] args) throws IOException {
    	for (int t = 0; t < 10; t++) {
    		int N = Integer.parseInt(br.readLine());
    		arr = new char[N + 1];
    		sb.append("#");
    		sb.append(t + 1 + " ");
    		
    		for (int i = 0; i < N; i++) {
    			String[] inputs = br.readLine().split(" ");
    			arr[i + 1] = inputs[1].charAt(0);
    		}
    		inorder(1, N);
    		sb.append("\n");
    	}
    	System.out.println(sb);
        br.close();
    }
    
    static void inorder(int node, int N) throws IOException {
    	if (node <= N) {
    		inorder(2 * node, N);
        	sb.append(arr[node]);
        	inorder(2 * node + 1, N);
    	}
    }
}