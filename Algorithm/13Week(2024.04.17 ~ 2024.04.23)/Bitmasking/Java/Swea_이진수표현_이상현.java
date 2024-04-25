import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());
        
        for (int t = 0; t < T; t++) {
            String[] arr = br.readLine().split(" ");
            int N = Integer.parseInt(arr[0]);
            int M = Integer.parseInt(arr[1]);
            boolean flag = true;
        
            String bin_M = Integer.toBinaryString(M);
            
            if (bin_M.length() >= N) {
                int length = bin_M.length();
                for (int i = length - 1; i >= length - N; i--) {
                    if (bin_M.charAt(i) == '0') {
                        flag = false;
                        break;
                    }
                }
            } else {
                flag = false;
            }
            
            if (flag) {
                System.out.println(
                        String.format("#%d ON", t + 1)
                    );
            } else {
                System.out.println(
                        String.format("#%d OFF", t + 1)
                    );
            }
        }
    }
}