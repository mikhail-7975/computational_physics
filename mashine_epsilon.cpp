#include <stdio.h>

float findEps_float() {
	float eps = 1.;
	printf("size = %d bytes", sizeof(eps));
	int i = 0;
	while (1.0f + eps / 2.0f != 1.0f) {
		eps /= 2.0f;
		i++;
	}
	printf("i = %d bit in mantissa", i);
	return eps;
}

double findEps_double() {
	double eps = 1.;
	printf("size = %d bytes", sizeof(eps));
	int i = 0;
	while (1. + eps / 2. != 1.) {
		eps /= 2.;
		i++;
	}
	printf("i = %d bit in mantissa", i);
	return eps;
}

int main() {
	printf("eps_float = %e\n", float(findEps_float()));
	printf("eps_double = %e\n", findEps_double());
}