**集成开发环境- #IDE**：
	首选 #Pycharm ：纯代码工作； #Jupyter_Lab ：主要做数据处理。
**前期准备工作**:
	1.安装 #Python :Python 3.14.3 with add python.exe to #PATH 
	2. #Python 的包管理工具：
		#pip ：查询、安装、卸载以及自动配置环境依赖功能；
		#venv ：创建 #Python 的虚拟环境；
		#conda ：以上，以及命令行工具安装等（机器学习，数据科学）。
	3. #conda 环境配置：
		1.清华大学镜像站：[清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/)
		2.Miniconda3-py313_25.11.1-1-Windows-x86_64
	4.**Install** #Jupyter_Lab:
		Windows 下 #Jupyter_Lab 生信环境配置笔记（Python 3.14.3）
 
			一、环境说明
				系统：Windows 10/11
				使用 Python 版本：3.14.3（系统自带）
				不使用 Miniconda 环境（避免版本冲突）
				用途：生信入门、数据处理、基础绘图
			 二、安装前检查
				打开 CMD（Win+R → 输入 cmd → 回车），输入：
```
python --version
```
				 必须显示：Python 3.14.3
			三、安装 JupyterLab + 生信基础包
				 在 CMD 中依次执行：
				 1. 升级 pip
```
python -m pip install --upgrade pip
```
				 2. 安装必需工具（一次性安装）
```
pip install jupyterlab numpy pandas matplotlib seaborn biopython
```
			四、启动 JupyterLab
				 在 CMD 中输入：
```
jupyter lab
```
				浏览器会自动打开界面。
			五、日常使用流程（固定步骤）
				 1. 打开 CMD
				2. 输入 jupyter lab 
				3. 在浏览器中开始分析
				4. 关闭时：先关浏览器，再按 Ctrl + C 关闭 CMD
			六、环境测试代码（新建 Notebook 运行）
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("环境配置成功！")
print("numpy 版本：", np.__version__)
print("pandas 版本：", pd.__version__)
```
			七、常见问题
				1. 报错 ModuleNotFoundError（找不到包）
					- 原因：环境不一致
					- 解决：必须从 CMD 启动，不要用其他终端
				2. 打不开浏览器
					- 复制 CMD 里的网址手动粘贴进浏览器
				3. 包安装失败
					- 重新运行安装命令即可
			 八、后续可安装内容（进阶用）
				- 热图：seaborn（已装）
				- 基因序列处理：biopython（已装）
				- R 语言：R + RStudio（不需要 Linux）

	下次要启动 #Jupyter_Lab 直接就在 #CMD 输入:
```
jupyter lab
```
	至此现在的环境里已经有(2026年2月26日)：
		- JupyterLab：运行平台​
		- numpy：数值计算​
		- pandas：数据表格（表达矩阵、CSV 文件）​
		- matplotlib：基础画图​
		- seaborn：热图、统计图​
		- biopython：生信序列处理