#include <stdio.h>
#include <math.h>


#define M 1.
#define A 1.

const double U0 = 10.;
const double plankConst = 1;//(6, 62607015 * pow(10, -34));

double equestion_func(double E) {
	double ksi = E;//(-E) / U0;
	double constant = 2 * M * pow(A, 2) * U0 / pow(plankConst, 2);
	return 1. / (tan(sqrt(constant * (1 - ksi)))) - sqrt(1 / ksi - 1);
}

double test_equestion_func(double E) {
	return pow(E, 3) + 0.5;
}

double test_equestion_func_der1(double E) {
	return 3 * pow(E, 2);
}

double dichotomy_method(double _leftBoard, double _rigthBoard, double(*func)(double)) {
	double delta0 = 2.;
	double delta = pow(10, -6);
	int N = static_cast<int>(log(delta0 / delta) / log(2));
	double leftBoard = _leftBoard;
	double rightBoard = _rigthBoard;
	double f_left = func(leftBoard);
	double f_right = func(rightBoard);
	
	if (f_left * f_right > 0)
		return NAN;
	
	printf("dichotomy method N = %d\n", N);

	for (int i = 0; i < N; i++) {
		double mid = (leftBoard + rightBoard) / 2;
		double f_mid = func(mid);
		if (fabs(f_mid) < delta) {
			return  mid;
		}
		if (f_mid * f_left < 0) {
			rightBoard = mid;
		} else {
			leftBoard = mid;
		}
	}
	return (leftBoard + rightBoard) / 2;
}

/*========================================================================================*/

double iteration_method(double(*func)(double), double lambda, double first_x) {
	double delta = pow(10, -6);
	double x = first_x + 10.;
	double x_old = first_x;
	int i = 0;
	while (1) {
		x = x_old - lambda * func(x_old);
		i++;
		if (fabs(x - x_old) < delta) {
			printf("iteration method N = %d\n", i);
			break;
		}
		x_old = x;
	}
	return x; 
}

double derivationInPoint(double(*func)(double), double x) {
	double delta = pow(10, -6);
	double a = func(x + delta);
	double b = func(x);
	return (a - b) / delta;
}

double newton_method(double(*func)(double), double first_x) {
	double delta = pow(10, -6);
	double x = first_x + 10.;
	double x_old = first_x;
	int i = 0;
	while (1) {
		printf("%lf\n", derivationInPoint(func, x_old));
		x = x_old - func(x_old) / derivationInPoint(func, x_old);//func_der1(x_old);
		i++;
		if (fabs(x - x_old) < delta) {
			printf("newton method N = %d\n", i);
			break;
		}
		x_old = x;
	}
	return x;
}

int main() {
	printf("dichotomy_method result = %lf\n", dichotomy_method(0.0001, 0.9999, equestion_func));
	printf("iteration_method result = %lf\n", iteration_method(equestion_func, 0.05, 0.1));
	printf("newton_method result = %lf\n", newton_method(equestion_func, 0.99));
	return 0;
}