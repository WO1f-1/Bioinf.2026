**Python基础**： #Jupyter_Lab 
**Python进阶**： #Pycharm 

 #变量 ：存放数据值
	#字符串 ：单、双、三引号均可
	#变量名 :区分大小写，只能包含数字，字母以及下划线，不可使用关键字。
	![[QQ_1772168444650.png]]
**变量赋值规则**：
	常规：```a = 1```
	**多个变量赋不同值：**```x,y,z = 1,2,3```
		#解包 ：```(1，2，3)tuple```
	**互换两个变量值：**
	```a = 1
	b = 2
	a,b = b,a
	print(a)
	print(b)
	``` #解包 
**Python数据类型：**

| 分类  | 具体类型     | 核心特点                                |
| --- | -------- | ----------------------------------- |
| 数值型 | int      | 无小数，如 `10` `-5`                     |
|     | float    | 带小数，如 `3.14` `2.0`                  |
|     | complex  | 含实部和虚部，如 `1+2j`                     |
| 字符串 | str      | 字符序列，单 / 双 / 三引号包裹，如 `"hello"`      |
| 布尔型 | bool     | 仅 `True`/`False`，用于逻辑判断             |
| 容器型 | list     | 有序、可变，方括号包裹，如 `[1, "a"]`            |
|     | tuple    | 有序、不可变，圆括号包裹，如 `(1, "a")`           |
|     | dict     | 键值对、无序、可变，花括号包裹，如 `{"name": "Tom"}` |
|     | set      | 无序、无重复，花括号 /`set()` 创建，如 `{1, 2}`   |
| 空值  | Nonetype | 仅 `None`，表示空值 / 无返回                 |
#字符串 ：raw字符串
```
s2 =  r"raw \nstring" # raw string
s3 = "raw \nstring" # normal string
print(s2)
print(s3)
```
	在raw字符串中，会将“双引号“中的内容识别为一个整体（文本）来看待，不执行换行操作，而normal字符串中依旧会执行\n 换行。
	tips：\n 换行符，\t 制表符。
**常用方法：**
	 #find ：寻找字符串中特定元素的位数（从0起）
```
#find
#abcdefg
#0123456
"abcdefg".find('b')
```
![[08059f58782674d22cd9943d01628daf 1.png]]
	 #count :寻找字符串中特定元素数量（≥0）
```
s = "abcdefga"
s.count("a")
```
![[QQ_1772170781165.png]]
	 #replace ：替换字符串中的特殊元素
```
s.replace('a','0')
```
![[QQ_1772170913485.png]]
	 #startswith ：判断字符串的第零个元素，输出值类型为布尔
```
s.startswith('a')
s.startswith('A')
s.startswith('')
```
![[QQ_1772172610439.png]]
		可见 #startswith 区分大小写，而且在判断值为空的情况下仍输出“True”
	 #endswith ：同理，相反
	 #upper ： 小写转大写，一般用于基因组测序中将测序质量不好的碱基（小写）转换为大写
	 ```
	 s.upper()
	 ```
	#lower ：同理，相反
	#split ：选中字符串里面的某个元素（可选择多个字符），作为分隔符将字符串拆开，输出类型是list（生成一个列表）
	   ```
	   s.split('e')
	   ```
	   ![[85fbfba39c13dcf07a9a6f9426060b81.png]]
	```
	   "1,2,3,4".split(",")
	```
	   输出结果为
	```
	   ['1','2','3','4']
	```
	 #join ：把上方list中的元素全部用某个字符连接起来
![[a8aafae40ecd0556772a2506ad4475fe 1.png]]
	#strip ：去掉字符串的换行符以及空白符号
```
"\nacctgtgtgtaaacccc    \n".strip()
```
输出结果为：
```
acctgtgtgtaaacccc
```
#切片 ：对字符串进行处理
![[Pasted image 20260227160403.png]]
![[Pasted image 20260227160525.png]]
![[Pasted image 20260227160610.png]]
** #格式化字符串 ：**
	#Percent方法 ：一种在字符串中轮流插入特定值的方法
![[Pasted image 20260227162346.png]]
	#format方法 ：原理同上
```
print("{}是{}和{}的和".format(a,b,c))
print("{a}是{b}和{c}的和".foramt(a=a,b=b,c=c))
```
此处a=a，前面的a对应前半部分的后赋值
	#fstring方法 ：原理与 #format方法 相同，但更简洁
```
a = 3
b = 2
c = 1
print(f"{a}是{b}和{c}的和")
```
	这里能直接让浮点数（int）转换为字符串（str）
**序列：**
	#新建列表 ：用 #split 方法
```
'1,2.0,a'.split(',')
```
输出值为：['1','2.0','a']
	 #list ：将 #tuple 转换为 #list 
```
t = ('a','b','c')
list(t) 
```
输出值为：['a','b','c']
```
list(range(0,3))
```
输出值为：[0,1,2]
```
list('abc')
```
输出值为：['a','b','c']
	#切片 ：说白了就是在list里面取值
```
print(ls[1])
print(ls[-1])
print(ls[1:3])
```
![[QQ_1772182508961.png]]
**修改元素：**
![[QQ_1772182789732.png]]
	#append方法 ：在 #list 末尾追加一个元素
	#remove方法 ：去掉 #list 里面的特定元素
	#pop方法 ：去掉 #list 最后一个值，并且将这个值赋给另外一个变量
![[Pasted image 20260227170627.png]]



