#include <iostream>
#include <string>

using namespace std;

int make_key(int day, int month, int year) {
	return year * 10000 + month * 100 + day;
}

class Student {
public:
	string name;
	int birthday;

	Student(string name, int day, int month, int year) {
		copy_name(name);
		birthday = make_key(day, month, year);
	}

	void copy_name(string name) {
		this->name = name;
	}
};

int main() {
	int N;
	Student min_std = {"", 00, 00, 0000}, max_std = {"", 99, 99, 9999};

	cin >> N;

	while (N--) {
		string name;
		int day, month, year;

		cin >> name >> day >> month >> year;

		int key = make_key(day, month, year);

		if (key > min_std.birthday)
			min_std = Student {name, day, month, year};
		if (key < max_std.birthday)
			max_std = Student {name, day, month, year};
	}

	cout << min_std.name << '\n' << max_std.name;

	return 0;
}