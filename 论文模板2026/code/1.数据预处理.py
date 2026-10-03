# -*- coding: utf-8 -*-
# =============================================================================
#  【占位示例】本文件仅用于演示附录源码排版，内容与赛题无关。
#  提交前必须整体替换为本队真实程序，并同步修改附录 A 的文件列表。
#  注意：代码中不得出现个人绝对路径、姓名、学校、赛区等信息（格式规范第六条）。
# =============================================================================
"""数据预处理：缺失值 / 异常值 / 重复值 / 标准化 / 标签编码 / 数据集划分"""

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split

DATA_PATH = os.path.join("data", "raw.csv")      # 只用相对路径
CLEAN_PATH = os.path.join("data", "clean.csv")


def load_data(path=DATA_PATH):
    """有真实数据就读真实数据；没有则生成示例数据，保证脚本可独立运行。"""
    if os.path.exists(path):
        return pd.read_csv(path)
    rng = np.random.default_rng(2026)
    return pd.DataFrame({
        "x_num1": rng.normal(60, 10, 300),
        "x_num2": rng.normal(200, 30, 300),
        "x_cat": rng.choice(["A", "B", "C"], 300),
        "y": rng.integers(0, 2, 300),
    })


def clean(df):
    df = df.copy()
    num_cols = df.select_dtypes(include=[np.number]).columns.drop("y")

    # 1) 缺失值：数值列用中位数填补（中位数比均值抗异常值）
    print("填补前缺失值个数：", int(df[num_cols].isna().sum().sum()))
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # 2) 异常值：IQR 法，超出 [Q1-1.5IQR, Q3+1.5IQR] 的样本直接剔除
    q1, q3 = df[num_cols].quantile(0.25), df[num_cols].quantile(0.75)
    iqr = q3 - q1
    keep = ((df[num_cols] >= q1 - 1.5 * iqr) & (df[num_cols] <= q3 + 1.5 * iqr)).all(axis=1)
    print("剔除异常值样本数：", int((~keep).sum()))
    df = df[keep]

    # 3) 重复值
    print("删除重复值数量：", int(df.duplicated().sum()))
    df = df.drop_duplicates()

    # 4) 极差标准化（量纲统一到 [0, 1]）
    df[num_cols] = MinMaxScaler().fit_transform(df[num_cols])

    # 5) 分类型特征做标签编码
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = LabelEncoder().fit_transform(df[col])
    return df


def main():
    df = clean(load_data())
    train, test = train_test_split(df, test_size=0.2, random_state=2026)
    print("清洗后样本数：{}，训练集 {}，测试集 {}".format(len(df), len(train), len(test)))
    print(df.head())

    if os.path.dirname(CLEAN_PATH):
        os.makedirs(os.path.dirname(CLEAN_PATH), exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False)
    print("已保存：", CLEAN_PATH)


if __name__ == "__main__":
    main()
