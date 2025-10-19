#include <iostream>
#include <cmath>
#include <string>


double R1(double x, double y, double z) {
    return x + 3*y + z*z - 4.16;
}
double R2(double x, double y, double z) {
    return 2*x + 2*y*y + z - 4.4;
}
double R3(double x, double y, double z) {
    return 3*x - y + 2*z*z - 2.32;
}

double errorFunction(double x, double y, double z) {
    return 0.5 * (pow(R1(x,y,z),2) + pow(R2(x,y,z),2) + pow(R3(x,y,z),2));
}

void getGradient(double x, double y, double z, double& dx, double& dy, double& dz) {
    dx = R1(x, y, z)*1 + R2(x, y, z)*2 + R3(x, y, z)*3;
    dy = R1(x, y, z)*3 + R2(x, y, z)*4*y + R3(x, y, z)*(-1);
    dz = R1(x, y, z)*2*z + R2(x, y, z)*1 + R3(x, y, z)*4*z;
}

void solveSystem(double& x, double& y, double& z, double tol) {
    double step = 0.01;
    int maxK = 5000;
    for (int k = 0; k < maxK; ++k) {
        double gx, gy, gz;
        getGradient(x, y, z, gx, gy, gz);
        double gradNorm = std::sqrt(gx*gx + gy*gy + gz*gz);

        if (k % 100 == 0)
            std::cout << "# " << k << " | x=" << x << " y=" << y << " z=" << z << " ||grad||=" << gradNorm
                      << " error=" << errorFunction(x,y,z) << std::endl;

        if (gradNorm < tol) break;
        x -= step * gx;
        y -= step * gy;
        z -= step * gz;
    }
}

int main() {
    setlocale(LC_ALL, "Ukrainian");
    double x = 1.0, y = 1.0, z = 1.0, tol = 0.0001;
    std::cout << "Розв'язання нелінійної системи градієнтом\n";
    std::cout << "Початкові значення: x=" << x << " y=" << y << " z=" << z << std::endl;
    solveSystem(x, y, z, tol);
    std::cout << "\nЗнайдено:\nx = " << x << "\ny = " << y << "\nz = " << z << std::endl;
    std::cout << "\nПеревірка:\n";
    std::cout << "R1 = " << R1(x,y,z) << "\n";
    std::cout << "R2 = " << R2(x,y,z) << "\n";
    std::cout << "R3 = " << R3(x,y,z) << "\n";
    std::cout << "\nСумарна нев'язка: " << errorFunction(x,y,z)*2 << std::endl;
    return 0;
}
