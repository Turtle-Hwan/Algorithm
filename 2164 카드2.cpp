#include <iostream>
#include <list>

int main() {
	int n = 0;
	std::cin >> n;

	std::list<int> card;

	for (int i = 0; i < n; i++) {
		card.push_back(i + 1);
	}


	int moveNum;

	while (card.size() != 1) {
		card.pop_front();
		moveNum = card.front();
		card.pop_front();
		card.push_back(moveNum);

	}

	std::cout << card.front();

}