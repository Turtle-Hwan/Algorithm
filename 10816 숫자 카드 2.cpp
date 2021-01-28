#include <iostream>
#include <unordered_map>
#include <vector>

int main()		//map 이용 : 시간초과  unordered_map : 상수시간에 검색 가능. (.tie 로 입출력 속도를 높이면 map도 가능)
{
	int N, M;

	std::cin >> N;

	std::unordered_map<int, int> card;
	int k;
	for (int i = 0; i < N; i++)
	{
		std::cin >> k;
		card[k] = card[k] + 1;
	}


	std::cin >> M;

	std::vector<int> answer;
	for (int i = 0; i < M; i++)
	{
		std::cin >> k;
		answer.push_back(card[k]);
	}

	for (int i : answer)
	{
		std::cout << i << " ";
	}
}

