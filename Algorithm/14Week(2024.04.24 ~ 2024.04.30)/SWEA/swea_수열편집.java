import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Solution {
	static int NODE_MAX = 2000;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    public static class Node {
    	int data;
    	Node next;
    	
    	public Node(int data) {
    		this.data = data;
    		this.next = null;
    	}
    }
    
    public static class LinkedList {
    	Node head;
    	Node tail;
    	Node[] nodeArr;
    	int nodeCnt;
    	
    	public LinkedList() {
    		head = null;
    		tail = null;
    		nodeArr = new Node[NODE_MAX];
    		nodeCnt = 0;
    	}
    	
    	Node getNewNode(int data) {
    		nodeArr[nodeCnt] = new Node(data);
    		return nodeArr[nodeCnt++];
    	}
    	
    	void insert(int idx, int data) {
    		Node newNode = getNewNode(data);
    		
    		if (idx == 0) {
    			newNode.next = head;
    			head = newNode;
    			return;
    		}
    		
    		Node cur = head;
    		
    		for (int i = 0; i < idx - 1; i++) {
    			cur = cur.next;
    		}
    		
    		Node target = cur.next;
    		newNode.next = target;
    		cur.next = newNode;
    	}
    	
    	void add(int data) {
    		Node newNode = getNewNode(data);
    		
    		if (tail == null) {
    			head = newNode;
    			tail = newNode;
    			newNode.next = null;
    			return;
    		}
    		
    		Node cur = tail;
    		tail.next = newNode;
    		tail = newNode;
    	}
    	
    	void delete(int idx) {
    		if (idx == 0) {
    			head = head.next;
    			return;
    		}
    		
    		Node cur = head;
    		
    		for (int i = 0; i < idx - 1; i++) {
    			cur = cur.next;
    		}
    		
    		Node target = cur.next;
    		cur.next = target.next;
    	}
    	
    	void change(int idx, int data) {
    		Node cur = head;
    		
    		if (idx == 0) {
    			cur.data = data;
    			return;
    		}
    		
    		for (int i = 0; i < idx; i++) {
    			cur = cur.next;
    		}
    		
    		cur.data = data;
    	}
    	
    	void solve(int idx) throws IOException {
    		Node cur = head;
    		
    		for (int i = 0; i < idx && cur != null; i++) {
    			cur = cur.next;
    		}
    		
    		if (cur == null) {
    			bw.write("-1");
    		} else {
    			bw.write(cur.data + "");
    		}
    	}
    }
	
	public static void main(String[] args) throws Exception {
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < T; tc++) {
			String[] temp = br.readLine().split(" ");
			
			int N = Integer.parseInt(temp[0]);
			int M = Integer.parseInt(temp[1]);
			int L = Integer.parseInt(temp[2]);
			
			String[] arr = br.readLine().split(" ");
			LinkedList list = new LinkedList();
			
			for (int i = 0; i < N; i++) {
				list.add(Integer.parseInt(arr[i]));
			}
			
			for (int i = 0; i < M; i++) {
				String[] commandArr = br.readLine().split(" ");
				char cmd = commandArr[0].charAt(0);
				
				switch (cmd) {
					case 'I': {
						int idx = Integer.parseInt(commandArr[1]);
						int data = Integer.parseInt(commandArr[2]);
						list.insert(idx, data);
						break;
					}
					case 'D': {
						int idx = Integer.parseInt(commandArr[1]);
						list.delete(idx);
						break;
					}
					case 'C': {
						int idx = Integer.parseInt(commandArr[1]);
						int data = Integer.parseInt(commandArr[2]);
						list.change(idx, data);
						break;
					}
				}
			}
			bw.write("#");
			bw.write((tc + 1) + " ");
			list.solve(L);
			bw.write("\n");
		}
		
		bw.flush();
		br.close();
		bw.close();
	}
}