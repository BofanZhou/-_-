# 2026 全国大学生数学建模竞赛 · 论文模板（合并版）

- **底稿**：latexstudio 官方 `CUMCMThesis` v2.9（`cumcmthesis.cls`，2026/08/26 更新）
- **承诺书已校订**：官方 v2.9 类文件里的承诺书还是旧版文字，本模板已按《论文格式规范（2026年修订稿）》
  的官方样张逐字改好（详见第 5 节末尾）
- **骨架**：原「国赛小班课定制模板」的章节写作结构与写作提示
- **AI 声明**：官方 `cumcm2026.sty` 的 `\CumcmAINotUsed` / `\CumcmAIUsed` 命令
- **参考文献**：`natbib` + `gbt7714-numerical.bst`（GB/T 7714 格式）
- 已实测：TeXLive 2026 下 `latexmk -xelatex main` 完整编译（xelatex→bibtex→xelatex×2），0 错误、0 未解析引用

---

## 1. 目录结构

```
论文模板2026/
├── main.tex                  ← 论文主文件（在这里写）
├── ai-details.tex            ← AI 工具使用详情（支撑材料专用，单独编译）
├── cumcmthesis.cls           ← 官方文档类 v2.9（只按 2026 官方样张校订了承诺书文字，其余未改动）
├── cumcm2026.sty             ← 2026 版式 + AI 声明命令
├── gbt7714-numerical.bst     ← 参考文献样式
├── ref.bib                   ← 参考文献库（替换成你自己的）
├── code/                     ← 源程序（附录要打印全部可运行代码）
│   ├── 1.数据预处理.py        ┐ 这 5 个文件目前是【可运行的占位示例】，
│   ├── q1.m  q2.py  q3.c  q4.cpp  ┘ 提交前必须换成本题真实程序
├── figures/                  ← 放图片（建议 PDF/PNG，文件名用英文）
├── main.pdf                  ← 编译结果预览
└── ai-details.pdf            ← 编译结果预览
```

## 2. 编译方法

必须用 **XeLaTeX**（模板里有 `\RequireXeTeX`，用 pdflatex 会直接报错）。

```bash
latexmk -xelatex main          # 推荐：一条命令，自动跑 bibtex 和多遍
latexmk -c                     # 清理中间文件

# 或者手动四步：
xelatex main  →  bibtex main  →  xelatex main  →  xelatex main
```

编辑器里请把编译链设为 XeLaTeX（TeXstudio：选项 → 构建 → 默认编译器 → XeLaTeX；
VS Code + LaTeX Workshop 用 `latexmk (xelatex)` 配方）。

AI 使用详情单独编译：

```bash
xelatex ai-details
# 然后把 ai-details.pdf 重命名为「AI工具使用详情.pdf」
```

**字体要求**：类文件里写死了 `\setmainfont{Times New Roman}` 与 `\setsansfont{Arial}`，
中文用 ctex 默认字体（Windows = 宋体/黑体/楷体，Linux/Mac = Fandol）。
Windows / macOS / Overleaf 都直接可用；**裸 Linux 的 TeX Live 若没有 Times New Roman、Arial 会直接编译失败**，
这时把 `cumcmthesis.cls` 里那两行改成本机已有字体（或加 `\IfFontExistsTF` 兜底）即可。

## 3. 电子版 vs 纸质版

| 用途 | 文档类写法 |
|---|---|
| 电子版提交（摘要页为第一页） | `\documentclass[withoutpreface,bwprint]{cumcmthesis}` ← **默认已设好** |
| 纸质打印（含承诺书 + 编号页） | `\documentclass[bwprint]{cumcmthesis}` |

纸质版实测：第 1 页承诺书（无页码）→ 第 2 页编号专用页（无页码）→ 第 3 页摘要页印页码「1」，
完全符合规范第三条（论文从摘要页开始、页脚中部、阿拉伯数字从 1 连续编号）。
**电子版不要有承诺书和编号页**，所以电子版用默认的 `withoutpreface` 就行。

## 4. AI 工具使用声明（`main.tex` 里搜索「AI 工具使用声明（必须）」）

2026 年规定：声明必须放在 **参考文献之前**，两句 **二者择一**，必须写出完整原句。

```latex
% 情形一：未使用 —— 保留这一行
\CumcmAINotUsed

% 情形二：使用了 —— 注释掉上面那行，解注释这一行并填用途
%\CumcmAIUsed{语言润色、代码调试}
```

- 渲染结果（未使用）：`本参赛队在竞赛过程中未使用任何 AI 工具。`
- 渲染结果（使用）：`本参赛队在竞赛过程中使用了 AI 工具，主要用于语言润色、代码调试，详细使用情况见支撑材料。`
- **若使用了 AI**，还必须在支撑材料里放单独的 `AI工具使用详情.pdf`（用 `ai-details.tex` 生成）。
- ⚠️ 不要把「AI 工具使用详情」写进论文正文（原小班课模板把它放在正文里，是不对的，本模板已移出）。
- ⚠️ 不要只留一个空的「AI工具使用声明」标题。

## 5. 已经替你处理好的 2026 规范要点

| 规范要求 | 本模板处理方式 |
|---|---|
| 电子版第一页必须是摘要页，不要承诺书/编号页 | `withoutpreface` 选项 |
| 页码从摘要页开始、页脚中部、从 1 连续编号 | 类文件 `\maketitle` 内 `\setcounter{page}{1}` + `plain` 页式 |
| 不要目录 | `\tableofcontents` 保持注释 |
| 正文不超过 30 页 | 写完后数页数（`pdfinfo main.pdf`） |
| AI 声明在参考文献之前 | 已固定在 `\bibliography` 之前 |
| 附录含支撑材料文件列表 + 全部源码 | 附录 A 文件列表、附录 B 源码（`\lstinputlisting` 已备好，解注释即用） |
| 全文不得出现姓名/学校/赛区 | 电子版只填标题；`\schoolname` 等信息只在纸质版生效 |
| 参考文献规范 | 正文用 `\cite{key}`，样式 `gbt7714-numerical`（GB/T 7714） |
| 摘要（含标题与关键词）原则上 ≤ 1 页 | 模板按一页预留，摘要自己控制篇幅 |
| 电子版必须是**单个** PDF/Word、不压缩、≤ 20MB | 编译后只提交 `main.pdf`（可改名），不要再打包压缩 |
| 支撑材料压成 RAR/ZIP、≤ 20MB、文件列表放附录 | 附录 A 已备好文件列表；支撑材料单独打包提交 |
| 附录页数不限，但必须与正文一起打印装订 | 附录写在同一份 PDF 里即可 |

> **两个易踩的坑**
>
> 1. **承诺书文字**：官方 v2.9 类文件的承诺书是旧版（漏掉"在竞赛中必须合法合规地使用文献资料和
>    软件工具…"一整段，"交流平台"表述也停留在旧年，链接是 http）。本模板已按
>    《论文格式规范（2026 年修订稿）》的官方样张逐字校订 `cumcmthesis.cls` 的
>    `\mcm@commit@string@contents`。**电子版不含承诺书，只有纸质版才用到。**
> 2. **"关键字"还是"关键词"**：规范第八条明确字号、字体、行距、颜色等不做统一要求，
>    官方类文件用"关键字"，原小班课模板改成过"关键词"，两者都不违规。
>    想跟多数论文一致，在 `main.tex` 导言区加：
>    `\makeatletter\renewcommand*{\mcm@cap@keywordsname}{关键词}\makeatother`
>
> 另外：`main.tex` 里没有 `\cite`，所以「参考文献」暂时是空的 —— 这是正常的，
> 你引用文献后就会出现。临时想看到所有条目，可解注释 `\nocite{*}`。

## 6. 写作提示（骨架里已埋好）

`main.tex` 的章节结构来自原小班课模板，每节都有 `【】` 提示：

1. 引言（问题背景 / 研究意义 / 问题重述）
2. 总体分析（含 TikZ 流程图骨架）
3. 模型假设
4. 符号说明
5. 问题一~四 的模型建立与求解（具体分析 / 数据预处理 / 模型建立 / 模型求解 / 结果分析）
6. 模型的分析与检验（灵敏度分析 / 误差分析 / 模型对比）
7. 模型的评价、改进与推广（优点 / 缺点 / 改进 / 推广）
8. AI 工具使用声明
9. 参考文献
10. 附录（支撑材料文件列表 / 源程序代码）

> 「问题四」整节是占位。若赛题只有三问（A/B/C 常见情况），请把该节连同前面的 `\newpage` 一起删掉。

写完后记得**把 `【】` 全部删干净**（包括提示文字），提交前全文搜索 `【` 检查一遍。

## 7. 附录打印源码

`main.tex` 附录 B 里每个 `\lstinputlisting` 都已写好路径，把注释去掉即可：

```latex
\subsection{问题二求解（Python）}
\lstinputlisting[language=python]{code/q2.py}
```

代码量大时全部解注释 —— 规范要求附录打印**全部完整、可运行的源程序**，
缺少必要源码、程序跑不通或结果与论文不符，都可能被取消评奖资格。
记得同时更新附录 A 的文件列表表格。

⚠️ `code/` 里现在放的是**可运行的占位示例**（数据预处理 / 线性回归 / TOPSIS / 数值积分 / 背包 DP），
只是为了让你看到源码在附录里的排版效果，**必须换成本题真实程序**；
而且代码里不能出现个人绝对路径、姓名、学校、赛区信息（规范第六条，会被取消评奖资格）。
