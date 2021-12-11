#https://www.acmicpc.net/problem/10757

#include <stdio.h>
#include <stdlib.h>

int main()
{
	char a[10001], b[10001];
	char newA[10001] = { '\0' }, newB[10001] = { '\0' }, result[10002] = { '\0' }, newResult[10002] = { '\0' };
	int alen = 0 , blen = 0, target = 0;
	int c[10002] = { 0 };

	scanf("%s %s", a, b);

	for (int x = 0; x < 10000; x++) {
		if (*(a + x) == '\0') {
			break;
		}
		else {
			alen++;
		}
	}

	for (int x = 0; x < 10000; x++) {
		if (*(b + x) == '\0') {
			break;
		}
		else {
			blen++;
		}
	}

	for (int x = 0; x < alen; x++) {
		*(newA + x) = *(a + alen - x - 1);
	}

	for (int x = 0; x < blen; x++) {
		*(newB + x) = *(b + blen - x - 1);
	}

	if (alen > blen)target = alen;
	else target = blen;

	for (int x = 0; x < target; x++) {
		int targetA = *(newA + x) - 48;
		int targetB = *(newB + x) - 48;
		if (targetA < 0 || targetA > 9) {
			targetA = 0;
		}
		if (targetB < 0 || targetB > 9) {
			targetB = 0;
		}


		int tmp = targetA + targetB + *(c + x);

		if (tmp > 9) {
			*(c + x + 1) = 1;
			tmp -= 10;
		}

		*(result + x) = tmp + 48;
	}

	if (*(c + target) == 1) {
		*(result + target) = '1';
		target++;
	}

	for (int x = 0; x < target; x++) {
		*(newResult + x) = *(result + target - x - 1);
	}

	printf("%s", newResult);

}