#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX_NAME 16

int make_key(int day, int month, int year) {
	return year * 10000 + month * 100 + day;
}

class Student {
public:
	char name[MAX_NAME];
	int birthday;

	Student(const char name[], int day, int month, int year) {
		copy_name(name);
		birthday = make_key(day, month, year);
	}

	void copy_name(const char name[]) {
		int i = 0;

		while (name[i] != '\0')
			this->name[i++] = name[i];

		this->name[i] = '\0';
	}
};

int main() {
	int N;
	Student min_std = {"", 00, 00, 0000}, max_std = {"", 99, 99, 9999};

	scanf("%d", &N);

	while (N--) {
		char name[MAX_NAME];
		int day, month, year;

		scanf("%s %d %d %d", name, &day, &month, &year);

		int key = make_key(day, month, year);

		if (key > min_std.birthday)
			min_std = Student {name, day, month, year};
		if (key < max_std.birthday)
			max_std = Student {name, day, month, year};
	}

	printf("%s\n%s", min_std.name, max_std.name);

	return 0;
}