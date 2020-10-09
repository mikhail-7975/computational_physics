#include <stdio.h>
#include <math.h>

double func1(double x) {
	return 1 / (1 + pow(x, 2));
}

double func2(double x) {
	return pow(x, 1. / 3.) * exp(sin(x));
}

double Integrate_trapeze(double(*func)(double), double left_border, double right_border, double step) {
	double result = 0.;
	double i = 0;
	for (i = left_border; i < (right_border - step); i += step) {
		result += (func(i) + func(i + step)) / 2 * step;
	}
	i += step;
	double dt = i - right_border;
	double a = func(right_border);
	double b = func(i);
	double diff = (a + b) / 2 * dt;
	result -= diff;
	return result;
}

double Integrate_Simpson(double(*func)(double), double left_border, double right_border, double step) {
	double result = 0.;
	double i = 0;
	for (i = left_border; i < (right_border - step); i += step) {
		double a = i;
		double b = i + step; 
		double S_ab = (b - a) / 6 * (func(a) + 4 * func((a + b) / 2) + func(b));
		result += S_ab;
	}
	double a = right_border;
	double b = i + step;
	double S_ab = (b - a) / 6 * (func(a) + 4 * func((a + b) / 2) + func(b));
	result -= S_ab;
	return result;
}


int main() {
	printf("\nfor func1:\n");
	double leftBorder = -1.;
	double rightBorder = 1.;
	double last_sim = 0., last_tr = 0.;
	for (int i = 4; i < pow(2, 22); i *= 2) {
		double step = (rightBorder - leftBorder) / i;
		double I_sim = Integrate_Simpson(func1, leftBorder, rightBorder, step);
		double I_tr = Integrate_trapeze(func1, leftBorder, rightBorder, step);
		
		double delta_sim = I_sim - last_sim;
		double delta_tr = I_tr - last_tr;
		printf("%d\t", i);
		printf("I_tr = %lf, delta = %lf\t", I_tr, delta_tr);
		printf("I_sim = %lf, delta = %lf\t", I_sim, delta_sim);
		printf("I_sim - I_tr = %e\n", I_sim - I_tr);
		last_sim = I_sim;
		last_tr = I_tr;
	}

	printf("\nfor func2:\n");
	last_sim = 0.;
	last_tr = 0.;
	leftBorder = 0.;
	rightBorder = 1.;
	for (int i = 4; i < pow(2, 22); i *= 2) {
		double step = (rightBorder - leftBorder) / i;
		double I_sim = Integrate_Simpson(func2, leftBorder, rightBorder, step);
		double I_tr = Integrate_trapeze(func2, leftBorder, rightBorder, step);

		double delta_sim = I_sim - last_sim;
		double delta_tr = I_tr - last_tr;
		printf("%d\t", i);
		printf("I_tr = %lf, delta = %lf\t", I_tr, delta_tr);
		printf("I_sim = %lf, delta = %lf\t", I_sim, delta_sim);
		printf("I_sim - I_tr = %e\n", I_sim - I_tr);
		last_sim = I_sim;
		last_tr = I_tr;
	}
}

