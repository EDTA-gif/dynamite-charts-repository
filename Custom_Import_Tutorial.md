# 将自己的谱面导入Dynamite中游玩
===

> [English ver.](./Custom_Import_Tutorial_EN.md)

## 第一步

将自己的谱面文件、音乐、预览音频和背景图等放入`data`(Android)/`Documents`(iOS)文件夹
* 只能识别.mp3格式的音频和.jpg格式的图片
* 具体导入方法请参考[主README](./README.md)中的步骤

## 第二步(Step 2)

在__rena_index_file中添加一条谱面信息

文件结构：
```
B.<UUID>
Y?<谱面是否隐藏?(0/1)>
R?<谱面是否为Ranked?(0/1)>
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
* UUID一栏随机生成一个24位的ID即可
* 所有文件路径都是相对于`data`/`Documents`文件夹的相对路径
* 多难度谱面文件和谱面标级按顺序对应
* 难度名可以自定义
* 是否Ranked属性和是否Hidden属性若为否可直接省略该行

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