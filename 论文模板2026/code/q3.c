/* ===========================================================================
 *  【占位示例】本文件仅用于演示附录源码排版，内容与赛题无关。
 *  提交前必须整体替换为本队真实程序，并同步修改附录 A 的文件列表。
 *  编译：gcc -O2 -o q3 q3.c -lm     或   cl q3.c
 * ===========================================================================
 *  问题三示范程序：复化 Simpson 公式求定积分，并给出与真值的误差
 *      ∫_0^π sin(x) dx = 2
 */

#include <stdio.h>
#include <math.h>

/* 被积函数 f(x) = sin(x) */
static double f(double x)
{
    return sin(x);
}

/* 复化 Simpson 公式：把 [a,b] 等分为 n（偶数）段 */
static double simpson(double a, double b, int n)
{
    int i;
    double h = (b - a) / n;
    double s = f(a) + f(b);

    for (i = 1; i < n; i++) {
        s += (i % 2 == 0 ? 4.0 : 2.0) * f(a + i * h);
    }
    return s * h / 3.0;
}

int main(void)
{
    const double a = 0.0, b = 3.14159265358979323846;   /* [0, pi] */
    const double exact = 2.0;                           /* 解析真值 */
    int n;

    printf("  n        Simpson 近似值        绝对误差\n");
    printf("----------------------------------------------\n");

    for (n = 4; n <= 256; n *= 2) {
        double approx = simpson(a, b, n);
        printf("%4d      %.12f      %.3e\n", n, approx, fabs(approx - exact));
    }

    /* 误差应随 n 加倍下降约 16 倍，说明收敛阶为 O(h^4) */
    return 0;
}
