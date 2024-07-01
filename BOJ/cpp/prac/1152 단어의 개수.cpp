#include <iostream>
#include <string>
#include <sstream> //istringstream ��� ����.
#include <vector>

int main() {

	std::string sentence;
	std::getline(std::cin, sentence);	//�� �� �Է� ����.

	std::stringstream ss(sentence);		//sstream ���� ��ūȭ (���� ����)

	std::vector<std::string> words;

	std::string a;
	while (ss >> a) {	//ss�� ��ū �ϳ��� a�� ������ ������ ����
		words.push_back(a);
	}

	std::cout << words.size();
}