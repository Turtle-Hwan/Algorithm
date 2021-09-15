#include <iostream>
#include <string>
#include <sstream> //istringstream 사용 위해.
#include <vector>

int main() {

	std::string sentence;
	std::getline(std::cin, sentence);	//한 줄 입력 받음.

	std::stringstream ss(sentence);		//sstream 으로 토큰화 (공백 기준)

	std::vector<std::string> words;

	std::string a;
	while (ss >> a) {	//ss의 토큰 하나를 a에 저장할 때마다 루프
		words.push_back(a);
	}

	std::cout << words.size();
}