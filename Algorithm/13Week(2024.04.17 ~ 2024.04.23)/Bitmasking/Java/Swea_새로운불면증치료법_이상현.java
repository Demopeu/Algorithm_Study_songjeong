import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());
        
        for (int t = 0; t < T; t++) {
            int N, memo, cnt, current;
            N = memo = Integer.parseInt(br.readLine());
            cnt = current = 0;
            
            while (current != (1 << 10) - 1) {
                String temp = Integer.toString(N);
                
                for (int i = 0; i < temp.length(); i++) {
                    int num = temp.charAt(i) - '0';
                    current = current | (1 << num);
                }
                
                cnt = cnt + 1;
                N = N + memo;
            }
            
            System.out.println(
                String.format("#%d %d", t + 1, N - memo)
            );
        }
    }
}