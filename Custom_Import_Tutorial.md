# 将自己的谱面导入Dynamite中游玩

> [English ver.](./Custom_Import_Tutorial_EN.md)

## 第一步

将自己的谱面文件、音乐、预览音频和背景图等放入`data`(Android)/`Documents`(iOS)文件夹
* 目前已知游戏可以识别`.mp3`格式的音频和`.jpg`/`.png`格式的图片，若文件无法识别请考虑转换文件格式
* 具体导入方法请参考[主README](./README.md)中的步骤

## 第二步(Step 2)

在__rena_index_file中添加一条谱面信息

文件结构：
```
B.<UUID>
Y?<谱面是否隐藏?>
R?<谱面是否为Ranked?>
N?<显示的曲名>
S?<音频文件路径>
C?<曲绘文件路径>
P?<预览音频文件路径>
U?<谱师>
W?<曲师>
I?<谱面信息>
H?<谱面难度1>;<谱面难度2>; ...
M?<谱面文件1>;<谱面文件2>; ...
E.
```
* UUID一栏可以取任何值
  * 推荐随机生成一个24位的ID
  * UUID的值与分数记录相关联，重复的UUID将会导致分数被错误关联，而空的UUID将导致分数无法记录
* 所有文件路径都是相对于`data`/`Documents`文件夹的相对路径
  * 路径中不可存在分号（`;`），除分号外的所有符号在导入时均会被视为路径内容</br>
    例如，若谱面文件名为`SECRET;WEAPON_M.xml`，则无论谱面信息写成`M?SECRET;WEAPON_M.xml;`还是`M?"SECRET;WEAPON_M.xml";`均无法使谱面被正常读取，请删除文件名中的分号
  * 路径中的斜杠`/`不可以用反斜杠`\`代替

* 目前存在部分谱面导入文件后preview和难度等级无法在预览页显示的情况
  * 此bug具体原理尚不明确
  * 目前已知可将谱面放在**名称长度大于等于6个字符的文件夹里**读取以避免这种情况

* 多难度谱面文件和谱面标级按顺序对应
  * 当谱面难度的数量少于谱面文件时，最后的多余谱面文件将被忽略
  * 当谱面难度的数量多于谱面文件时，将会导致Bug

* 难度名和等级可以自定义
  * 难度名和等级可以使用任意非逗号（`,`）和分号（`;`）的字符
  * 除Casual、Normal、Hard、Mega和Giga（不区分大小写）外，任何难度都会被显示为Tera的外观

* Ranked属性和谱面隐藏属性若为否，应直接省略该行，该行取任何值都会导致被识别为“是”
  * 即使写入例如`R?`或`R?0`的语句，该属性依然会被识别为“是”

示例：
```
B.5e36976860231240c3320ed7
R?1
N?ouroboros -twin stroke of the end-
S?ouroboros -twin stroke of the end-(Homeee VS TangScend)/ouroboros -twin stroke of the end-.mp3.rnx
C?ouroboros -twin stroke of the end-(Homeee VS TangScend)/ouroboros -twin stroke of the end-.jpg.rnx
P?ouroboros -twin stroke of the end-(Homeee VS TangScend)/ouroboros -twin stroke of the end-_preview.mp3.rnx
U?Homeee VS TangScend
W?Cranky VS MASAKI
I?Pattern Design: Homeee VS TangScend\n(Details: Casual/Hard by TangScend, Normal/Mega by Homeee)
H?CASUAL,5;NORMAL,7;HARD,11;MEGA,14;GIGA,15;
M?ouroboros -twin stroke of the end-(Homeee VS TangScend)/ouroboros -twin stroke of the end-_CASUAL.xml.rnx;ouroboros -twin stroke of the end-(Homeee VS TangScend)/ouroboros -twin stroke of the end-_NORMAL.xml.rnx;ouroboros -twin stroke of the end-(Homeee VS TangScend)/ouroboros -twin stroke of the end-_HARD.xml.rnx;ouroboros -twin stroke of the end-(Homeee VS TangScend)/ouroboros -twin stroke of the end-_MEGA.xml.rnx;ouroboros -twin stroke of the end-(Homeee VS TangScend)/ouroboros -twin stroke of the end-_GIGA.xml.rnx;
E.
```

## 第三步

打开炸药开打