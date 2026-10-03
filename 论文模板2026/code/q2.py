# -*- coding: utf-8 -*-
# =============================================================================
#  【占位示例】本文件仅用于演示附录源码排版，内容与赛题无关。
#  提交前必须整体替换为本队真实程序，并同步修改附录 A 的文件列表。
# =============================================================================
"""问题二示范程序：熵权法确定权重 + TOPSIS 综合评价排序"""

import numpy as np


def entropy_weight(X):
    """熵权法求指标权重。X: (n 个方案, m 个指标)，均为效益型且 >= 0。"""
    P = X / X.sum(axis=0, keepdims=True)           # 归一化为比重
    P = np.clip(P, 1e-12, None)                    # 防止 log(0)
    E = -np.sum(P * np.log(P), axis=0) / np.log(X.shape[0])   # 信息熵
    return (1 - E) / np.sum(1 - E)                 # 差异系数越大权重越大


def topsis(X, w=None, benefit=None):
    """TOPSIS：返回每个方案的综合得分（越接近 1 越好）。"""
    X = np.asarray(X, dtype=float)
    n, m = X.shape
    if w is None:
        w = entropy_weight(X)
    if benefit is None:
        benefit = np.ones(m, dtype=bool)

    # 1) 向量归一化
    Z = X / np.sqrt((X ** 2).sum(axis=0, keepdims=True))
    # 2) 加权
    V = Z * w
    # 3) 正、负理想解（成本型指标取反）
    best = np.where(benefit, V.max(axis=0), V.min(axis=0))
    worst = np.where(benefit, V.min(axis=0), V.max(axis=0))
    # 4) 到正/负理想解的欧氏距离
    d_best = np.sqrt(((V - best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((V - worst) ** 2).sum(axis=1))
    # 5) 相对贴近度
    return d_worst / (d_best + d_worst)


def main():
    rng = np.random.default_rng(2026)
    X = np.abs(rng.normal(1.0, 0.3, size=(6, 4)))     # 6 个方案、4 个效益型指标
    X = np.round(X, 3)
    w = entropy_weight(X)
    score = topsis(X, w)

    print("指标权重：", np.round(w, 4))
    for i in np.argsort(-score):
        print("方案 {}：得分 {:.4f}".format(i + 1, score[i]))
    print("最优方案：第 {} 个".format(int(np.argmax(score)) + 1))


if __name__ == "__main__":
    main()
