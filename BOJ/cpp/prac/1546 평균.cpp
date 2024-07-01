#include <iostream>

int main() {
	int n;
	std::cin >> n;

	int score[1000];
	for (int i = 0; i < n; i++) {
		std::cin >> score[i];
	}

	double maxScore = 0;
	for (int i = 0; i < n; i++) {
		if (maxScore < score[i]) {
			maxScore = score[i];			
		}
	}

	double score_sum = 0;
	for (int i = 0; i < n; i++) {
		score_sum = score_sum + score[i];
	}

	double average = score_sum / (maxScore * n) * 100;
	std::cout << average;
}