#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main() {
	char word[101];

	scanf("%s", word);

	int idx = 0;
	int count = 0;

	while (word[idx] != '\0') {
		count++;

		if (word[idx] == 'c') {
			if (word[++idx] == '=') idx++;
			else if (word[idx] == '-') idx++;
		}
		else if (word[idx] == 'd') {
			if (word[++idx] == '-') idx++;
			else if (word[idx] == 'z') {
				if (word[++idx] == '=') idx++;
				else count++;
			}
		}
		else if (word[idx] == 'l' || word[idx] == 'n') {
			if (word[++idx] == 'j') idx++;
		}
		else if (word[idx] == 's' || word[idx] == 'z') {
			if (word[++idx] == '=') idx++;
		}
		else idx++;
	}

	printf("%d", count);

	return 0;
}