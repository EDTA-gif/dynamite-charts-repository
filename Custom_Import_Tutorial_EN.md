# Import your own chart into dynamite to play

## Step 1
Copy your chart, music, preview music and cover files into `data`(Android)/`Documents`(iOS) folder.

* As far as we know, only audio files in `.mp3` format and pictures in `.jpg` or `.png` format can be properly imported, so please convert your files if  they're not in formats that are mentioned above.
* Refer to [Main Guide](./README_EN.md) for detailed import methods

## Step 2
Modify the local `__rena_index_2` file to add an entry for your file

Entry structure：
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
* Any value works in UUID row
  * A random hex string of length 24 is recommended
  * No bug caused by using an repeated/empty uuid has been reported so far. 

* All file paths are relative paths to `data`/`Documents` folder
  * Semicolons (`;`) in path is not allowed, all other symbols will be treated as part of the path.
    For example, if the chart file is named `SECRET;WEAPON_M.xml`, then no matter whether the entry is `M?SECRET;WEAPON_M.xml;` or `M?"SECRET;WEAPON_M.xml";`, the game won't find the chart file. Please delete semicolons in filenames.
  * Slashes `/` cannot be replaced by backslashes `\`

* For multiple-diffed charts, the file paths correspond to the difficulties in input order
  * If there are more files than difficulties, the redundant charts will be ignored.
  * Less files than difficulties will cause bugs to occur.

* It's allowed to have custom difficulty names and levels
  * Any name or level without comma `,` or semicolon `;` is allowed
  * Any input except Causal, Normal, Hard, Mega and Giga (case insensitive) will be regarded as custom difficulty names, and will be displayed in the layout of Tera.

* If you want the chart to be identified as unranked or not hidden, leave out that whole line. Any value given will be regarded as true
  * The value will be regarded as true even with inputs like `R?` or `R?0`


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