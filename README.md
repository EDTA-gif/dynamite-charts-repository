Dynamite Backup Project
===

> [English ver.](./README_EN.md)

## 收录范围
* 截至2022/6/10 Dynamite关服前已通过Ranked/Unranked审核的所有谱面
* 对文件名，文件结构和`__rena_index_2`文件进行了整理
* 数据保留了游戏内加密，目前只可以导入Dynamite进行游玩
* Github仅做文件统计和修正用途，全部谱面补全后会在发布国内相对方便下载的源

## 曲目一览
* Charts文件夹中的子文件夹大部分是按照`<曲名>(<谱师名>)`的格式命名的，为了区分同一作者提交的同一曲的多个版本也有`<曲名>_<Ranked状态>(<谱师名>)`的命名格式
* 因文件项目过多，Github默认只显示前一千条目录，请在`rena_index_list`文件中善用`Ctrl+F`功能查找歌曲
* 若出现以下情况请提交Issue或通过trickl4sh220@foxmail.com联系我，我会修正或更新在README里
   * 搜不到自己确定曾经过审过的谱面
   * 本应正常打开的谱面/正常播放的音源无法打开/播放

## 导入方法

> 导入自定义谱面的方法请参考[这里](./Custom_Import_Tutorial.md)

### Android

> 原文：[安卓导入方法b站专栏](https://www.bilibili.com/read/cv17021429)

1. 对本地数据做好备份
2. 清空`Android > data > tech.dynami.dynamite > files`文件夹内的所有.rnx后缀文件
   * 由于游戏只能根据`index`文件识别数据，更换完`index`文件之后无法再利用本地数据，此步是为了节省空间
3. 将Charts文件夹内的所有文件放入该目录中，用文件夹里的`__rena_index_2`文件覆盖掉本地的对应文件
4. 即可离线游玩

> 对于版本大于等于12的安卓系统，如发现默认文件管理器无法打开`Android/data`，请考虑利用Magisk等工具root

### iOS (Sideloadly/AltStore)

> 参考：
> 
> [iOS导入方法b站专栏](https://www.bilibili.com/read/cv17026497) & 
> [Jmak的Manual](https://docs.google.com/document/d/1-1ydDVTnuJO2g49b-9FFa9vXiAFRLGUEK4ullHnD2fU)

1. 在页面右侧的[Releases](https://github.com/EDTA-gif/dynamite-charts-repository/releases/tag/Game_executable)中下载系统安装包`Dynamite_filesharing.ipa`文件
2. 以下两项二选一完成
   
> * 去[Sideloadly官网](https://sideloadly.io/)下载并将Sideloadly安装到电脑上
> * 将设备连接电脑后利用Sideloadly安装ipa

> * 在[AltStore官网](https://altstore.io/)下载并安装AltServer
> * 将设备连接电脑后利用AltServer在设备上安装AltStore
> * 利用AltStore安装ipa
  
3. 非官方应用安装完后需要在`设置 > 通用 > 设备管理`中信任对应账号
4. 使用iTunes的文件管理或Files找到你安装的Dynamite程序，`/Documents`目录中的内容即为谱面数据内容，相当于安卓的`/files`目录
5. 每7天需要用Sideloadly/Altstore重新安装ipa，虽然只要不删掉Dynamite且安装时使用同一个Apple ID即可保留数据，但还是请注意数据备份

### iOS (越狱)

> By Jmak

1. 请不要删掉在设备的Dynamite，以下这个方法是让TestFlight过期了还可以继续使用
2. 在Cydia/Sileo（Zebra或者其他也行）添加新的Source(http://cydia.kiiimo.org)或者(https://repo.hackyouriphone.org)然后安装Anti-Revoke 2
3. 确保已在Cydia/Sileo（Zebra或者其他也行）安裝Filza File Manager，免费和付费版都可以
4. 在左边按上Apps manager
5. 关上激活Filza的通知（付费的可以绕过这个步骤）
6. 寻找Dynamite之后移步到Documents
7. 全选所有档案，除了Unity档案夹和`__rena_mark_store_3`之外
8. 完成!
## 其他Dynamite相关文档的友情链接

[Ranked谱面R值定数表图片版](https://www.bilibili.com/read/cv16981243)

[Ranked谱面R值计算拟合公式](https://www.bilibili.com/read/cv17024921)

## 特别鸣谢
* i0nTempest
* Errno
* Jmak