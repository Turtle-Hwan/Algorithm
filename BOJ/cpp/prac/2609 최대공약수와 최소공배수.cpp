#include <iostream>

int gcd (int a, int b) {	//�ִ����� - ��Ŭ���� ȣ���� �̿�

	if (a < b) {
		int temp = a;
		a = b;
		b = temp;
	}

	int q = 1;
	int r = 1;

	while (r != 0) {
		q = a / b;
		r = a % b;

		a = b;
		b = r;
	}

	return a;

}


int lcm (int a, int b) {	//�ּҰ���� - gcd �̿� or ������ ��..?
	//gcd �̿�
	//return (a * b) / gcd(a, b);

	
	//������
	int ia = 2;
	int ib = 2;
	int aa = a;
	int bb = b;
	while (aa != bb) {
		if (aa > bb) {
			bb = b * ib;
			ib++;
		}
		else if (aa < bb) {
			aa = a * ia;
			ia++;
		}
		else {
			break;
		}
	}
	return aa;
	
}



int main() {	
	int a, b;
	std::cin >> a >> b;

	std::cout << gcd(a, b) << std::endl;

	std::cout << lcm(a, b);

}