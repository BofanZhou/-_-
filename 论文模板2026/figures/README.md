# 图片目录

把论文用到的图片放在这里。

约定：
- 文件名用**英文/数字**，不要用中文；命名要有意义（如 `flowchart.pdf`、`error_curve.png`），
  不要用 `1.png`、`2.png` 这种顺序命名。
- 矢量图优先用 **PDF**（用 MATLAB / Python 直接导出 PDF，或 `savefig('x.pdf')`）；
  位图用 **PNG**。尽量不用 EPS、BMP。
- 插入示例（`main.tex` 里已写好注释版）：

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/flowchart.pdf}
    \caption{本文总体建模思路}
    \label{fig:flowchart}
\end{figure}

如图~\ref{fig:flowchart}~所示，……
```

- 并排子图用 `subcaption`（类文件已加载）：

```latex
\begin{figure}[H]
    \centering
    \begin{subfigure}{0.48\textwidth}
        \centering
        \includegraphics[width=\linewidth]{figures/a.pdf}
        \caption{子图 A}
        \label{fig:sub-a}
    \end{subfigure}
    \hfill
    \begin{subfigure}{0.48\textwidth}
        \centering
        \includegraphics[width=\linewidth]{figures/b.pdf}
        \caption{子图 B}
        \label{fig:sub-b}
    \end{subfigure}
    \caption{对比结果}
    \label{fig:compare}
\end{figure}
```
