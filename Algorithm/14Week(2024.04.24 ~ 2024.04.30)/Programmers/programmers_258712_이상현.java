import java.util.HashMap;

class Solution {
    static StringBuilder sb = new StringBuilder();
    
    public int solution(String[] friends, String[] gifts) {
        int N = friends.length;
    	int[][] gift_table = new int[N][N];
    	int[][] gift_score_table = new int[N][3];
    	int[] result = new int[N];
    	HashMap<String, Integer> name_table = new HashMap<>();
    	
    	for (int i = 0; i < N; i++) {
    		name_table.put(friends[i], i);
    	}
    	
    	for (String gift: gifts) {
    		String[] temp = gift.split(" ");
    		gift_table[name_table.get(temp[0])][name_table.get(temp[1])]++;
    	}
    	
    	for (int i = 0; i < N; i++) {
    		for (int j = 0; j < N; j++) {
    			gift_score_table[i][0] += gift_table[i][j];
    			gift_score_table[i][1] += gift_table[j][i];
    		}
    		gift_score_table[i][2] = gift_score_table[i][0] - gift_score_table[i][1];
    	}
    	
    	for (int i = 0; i < N - 1; i++) {
    		for (int j = i + 1; j < N; j++) {
    			if (gift_table[i][j] > gift_table[j][i]) {
    				result[i]++;
    			} else if (gift_table[i][j] < gift_table[j][i]) {
    				result[j]++;
    			} else {
    				if (gift_score_table[i][2] > gift_score_table[j][2]) {
    					result[i]++;
    				} else if (gift_score_table[i][2] < gift_score_table[j][2]) {
    					result[j]++;
    				}
    			}
    		}
    	}
    	
    	int answer = 0;
    	for (int score: result) {
    		if (score > answer) {
    			answer = score;
    		}
    	}
        return answer;
    }
}