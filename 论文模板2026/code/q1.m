%% ===========================================================================
%  【占位示例】本文件仅用于演示附录源码排版，内容与赛题无关。
%  提交前必须整体替换为本队真实程序，并同步修改附录 A 的文件列表。
%  注意：代码中不得出现个人绝对路径、姓名、学校、赛区等信息（格式规范第六条）。
% ===========================================================================
%  问题一示范程序：最小二乘线性拟合 + 留一法交叉验证 + 精度评价
%  运行环境：MATLAB R2016a 及以上（仅用基础函数，无需工具箱）

clear; clc; rng(2026);

%% 1. 生成/读入数据（示例用合成数据，实际请换成赛题附件）
n = 60;
x = linspace(0, 10, n)';
y = 2.5 * x + 1.0 + 0.8 * randn(n, 1);

%% 2. 最小二乘拟合 y = a*x + b
X = [x, ones(n, 1)];
beta = X \ y;                      % 正规方程解
a = beta(1);  b = beta(2);
yhat = X * beta;

%% 3. 精度评价
SSE = sum((y - yhat).^2);
SST = sum((y - mean(y)).^2);
R2  = 1 - SSE / SST;
RMSE = sqrt(SSE / n);

fprintf('拟合结果： y = %.4f * x + %.4f\n', a, b);
fprintf('R^2 = %.4f,  RMSE = %.4f\n', R2, RMSE);

%% 4. 留一法交叉验证（LOOCV），检验模型稳定性
err = zeros(n, 1);
for i = 1:n
    idx = true(n, 1);  idx(i) = false;
    bi = X(idx, :) \ y(idx);
    err(i) = y(i) - X(i, :) * bi;
end
fprintf('LOOCV 平均绝对误差 MAE = %.4f\n', mean(abs(err)));
fprintf('LOOCV 均方根误差 RMSE  = %.4f\n', sqrt(mean(err.^2)));

%% 5. 保存结果（相对路径，便于复现）
if ~exist('result', 'dir'); mkdir('result'); end
save(fullfile('result', 'q1_result.mat'), 'a', 'b', 'R2', 'RMSE');
writematrix([x, y, yhat], fullfile('result', 'q1_fit.csv'));
disp('结果已保存到 result/q1_result.mat 与 result/q1_fit.csv');
