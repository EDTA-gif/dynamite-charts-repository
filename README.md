Dynamite Backup Project
===

## 收录范围
* 截至2022/6/10 Dynamite关服前已通过Ranked/Unranked审核的所有谱面
* 对文件名，文件结构和`__rena_index_2`文件进行了整理
* 数据保留了游戏内加密，目前只可以导入Dynamite进行游玩
* Github仅做文件统计用途，全部谱面补全后会在发布国内相对方便下载的源

## 曲目一览
* Charts文件夹中的子文件夹大部分是按照`<曲名>(<谱师名>)`的格式命名的，为了区分同一作者提交的同一曲的多个版本也有`<曲名>_<Ranked状态>(<谱师名>)`的命名格式
* 因文件项目过多，Github默认只显示前一千条目录，请在`rena_index_list`文件中善用`Ctrl+F`功能查找歌曲
* 若搜不到自己确定曾经过审过的谱面请提交Issue，我会更新在README里
* 目前已知未收录谱面：
   * Ignotus Afterburn Giga 2041 By Rezasho, Unranked，2022愚人节谱面
   * εxceζ Giga 15 By γraphitε，Unranked，于6/8 20:09过审
   * {albus} Giga 14 By Graphite，Unranked，于6/8 20:10过审
* 如果你本地保存有以上谱面的数据且想要提取出来上传的话，请将谱面文件和包含对应信息的`__rena_index_2`文件打包发送至trickl4sh220@foxmail.com
   * 当然有能力的话更欢迎fork一下改完merge回来
   * 如果确定自己保存了但实在找不到对应的游戏文件的话发整个`files`文件的压缩包也行，但考虑到文件大小一般不建议这么做

## 导入方法

### Android

原文：[安卓导入方法b站专栏](https://www.bilibili.com/read/cv17021429)

1. 对本地数据做好备份
2. 清空`Android > data > tech.dynami.dynamite > files`文件夹内的所有.rnx后缀文件
3. 将Charts文件夹内的所有文件放入该目录中，用文件夹里的`__rena_index_2`文件覆盖掉本地的对应文件
4. 即可离线游玩

> 对于版本大于等于12的安卓系统，如发现默认文件管理器无法打开`Android/data`，请考虑利用Magisk等工具root

### iOS

原文：[iOS导入方法b站专栏](https://www.bilibili.com/read/cv17026497)

1. 准备好Dynamite的iOS系统安装包`.ipa`文件
2. 在[Sideloadly官网](https://sideloadly.io/)下载并安装sideloadly
3. 在Sideloadly中勾选以下选项后安装ipa
   * Enable UIFileSharing
   * Remove limitation on supported devices
4. 使用imazing、iTunes或爱思助手等软件在应用管理（iTunes的文件共享）里找到你安装的Dynamite程序，`/Documents`目录中的内容即为谱面数据内容，相当于安卓的`/files`目录

## 其他Dynamite相关文档的友情链接

[Ranked谱面R值定数表图片版](https://www.bilibili.com/read/cv16981243)

[Ranked谱面R值计算拟合公式](https://www.bilibili.com/read/cv17024921)

## 特别鸣谢
* i0nTempest
* Errno
