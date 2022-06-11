# Import your own chart into dynamite to play

## Step 1
Copy your chart, music, preview music and cover files into `data`(Android)/`Documents`(iOS) folder.

* Can only read audio files in `.mp3` format and image files in `.jpg` format
* Refer to [Main Guide](./README_EN.md) for detailed import methods

## Step 2
Modify the local `__rena_index_2` file to add an entry for your file

Entry Structure：
```
B.<UUID>
Y?<Hidden chart?(0/1)>
R?<Ranked chart?(0/1)>
N?<Song Name>
S?<Music file path>
C?<Cover file path>
P?<Preview music file path>
U?<Charter>
W?<Artist>
I?<Chart info>
H?<Chart difficulty 1>;<Chart difficulty 2>; ...
M?<Chart file 1>;<Chart file 2>; ...
E.
```
* Any random 24-bit UUID will work
* All file paths are relative paths to `data`/`Documents` folder
* For multiple-diffed charts, the file paths correspond to the difficulties in input order
* It's allowed to have custom diff names
* If you don't want the chart to be identified as ranked or hidden, you can just leave out the whole line


Example:
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

## Step 3

Open dynamite and enjoy.