#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

constexpr size_t NODE_MAX = 5000;

struct Node{
	int data;
	Node*next;
	Node(int data):data(data),next(nullptr) {}
};

class LinedList {
	Node*head;
	vector<Node*> nodeArr;
	int nodeCnt;

public:

	LinedList() : head(nullptr),nodeCnt(0) {
		nodeArr.resize(NODE_MAX, nullptr);
	}

	void insert(int(idx), int(data)) {

		nodeArr[nodeCnt] = new Node(data);
		Node*newNode = nodeArr[nodeCnt++];

		if (idx == 0) {
			if (head != nullptr){
				newNode->next = head;
				head = newNode;
			}else {
				head = newNode;
			}
		}
		else {
			Node* cur = head;
			for (int i = 1; i < idx; i++){
				cur = cur->next;
			}

			Node*nextNodeAd= cur->next;
			newNode->next = nextNodeAd;
			cur->next = newNode;
		}
		//Node*cur = head;
		//while (true){
			//cout << cur->data << " ";
			//cur = cur->next;
			//if (cur == nullptr) {
			//	cout << '\n';
			//	break;
			//}
		//}
		
	}

	void remove(int(idx)) {
		Node* cur = head;
		if (idx == 0) {
			head = cur->next;
			return;
		}
		for (int i = 0; i < idx-1; i++){
				cur = cur->next;
			}
		Node*targetNode = cur->next;
		cur->next = targetNode->next;

		//Node*now = head;
		//while (true) {
		//	cout << now->data << " ";
		//	now = now->next;
		//	if (now == nullptr) {
		//		cout << '\n';
		//		break;
		//	}
		//}
	}

	void change(int(idx), int(data)) {
		Node*cur = head;
		if (idx == 0) {
			head->data = data;
			return;
		}
		for (int i = 0; i < idx; i++)
		{
			cur = cur->next;
		}
		cur->data = data;
	}

	void print(int(idx),int(lenList)) {
		if (idx > lenList) {
			cout << -1;
		} else {
			Node*cur = head;
			if (idx == 0) {
				cout << head->data;
				return;
			}
			for (int i = 0; i < idx; i++){
				cur = cur->next;
			}
			cout << cur->data;
		}
	}
};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int T;
	cin >> T;
	for (int testcase = 1; testcase < T+1; testcase++){
		int N, M, L,lengthList = 0;
		LinedList list;
		cin >> N >> M >> L;
		cout << "#" << testcase << " ";

		for (int i = 0; i < N; i++){
			int data;
			cin >> data;
			list.insert(i, data);
			lengthList++;
		}
		for (int i = 0; i < M; i++){
			char cmd;
			int x, y;
			cin >> cmd;
			switch (cmd){
			case 'I':
				cin >> x >> y;
				list.insert(x, y);
				//cout << "insert ok!" << '\n';
				lengthList++;
				break;
			case 'D':
				cin >> y;
				list.remove(y);
				//cout << "remove ok!" << '\n';
				lengthList--;
				break;
			case 'C':
				cin >> x >> y;
				list.change(x, y);
				//cout << "change ok!" << '\n';
				break;
			}
		}
		list.print(L,lengthList);
		cout << '\n';
	}
	return 0;
}