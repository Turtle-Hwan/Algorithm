#include <iostream>
#include <unordered_map>
#include <vector>

int main()		//map �̿� : �ð��ʰ�  unordered_map : ����ð��� �˻� ����. (.tie �� ����� �ӵ��� ���̸� map�� ����)
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

