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
* 若出现以下情况请提交Issue，我会修正或更新在README里
   * 搜不到自己确定曾经过审过的谱面
   * 本应正常打开的谱面/正常播放的音源无法打开/播放
* 目前已知未收录谱面：
   * Ignotus Afterburn Giga 2041 By Rezasho, Unranked，2020愚人节谱面
   * εxceζ Giga 15 By γraphitε，Unranked，于6/8 20:09过审
   * {albus} Giga 14 By Graphite，Unranked，于6/8 20:10过审
* 如果你本地保存有以上谱面的数据且想要提取出来上传的话，请将谱面文件和包含对应信息的`__rena_index_2`文件打包发送至trickl4sh220@foxmail.com
   * 当然有能力的话更欢迎fork一下改完merge回来
   * 如果确定自己保存了但实在找不到对应的游戏文件的话发整个`files`文件的压缩包也行，但考虑到文件大小一般不建议这么做

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

### iOS (Sideloadly)

> 原文：[iOS导入方法b站专栏](https://www.bilibili.com/read/cv17026497)

1. 准备好Dynamite的iOS系统安装包`.ipa`文件
2. 在[Sideloadly官网](https://sideloadly.io/)下载并安装sideloadly
3. 在Sideloadly中勾选以下选项后安装ipa
   * Enable UIFileSharing
   * Remove limitation on supported devices
4. 使用imazing、iTunes或爱思助手等软件在应用管理（iTunes的文件共享）里找到你安装的Dynamite程序，`/Documents`目录中的内容即为谱面数据内容，相当于安卓的`/files`目录
5. 每7天需要用Sideloadly重新安装，虽然只要不删掉Dynamite且使用同一个Apple ID即可保留数据，但还是请注意数据备份

### iOS (Filza文件管理器)

> By Jmak

**适用于版本号在 11-13.4.1 / 15-15.1.1 之间的iOS系统**
##### 不依赖电脑

1. 下载FilzaEscaped (https://basvtdevelopments.com/filzaescaped) 
2. 打开浏览器去以下这个网址 - Freebox (https://freebox.co/web/signer/)
3. 在Freebox的网站选择FilzaEscaped的.ipa档案 "Choose File > Browse > Dynamite.ipa > Sign > Wait for it to download > Choose Open on “Open this page in iTunes” > Install"
4. 安装后导航去设定 > 一般 > VPN & Device Management > Apple ID > 信任
5. 在Freebox的网站选择Dynamite的.ipa档案 "Choose File > Browse > Dynamite.ipa > Sign > Wait for it to download > Choose Open on “Open this page in iTunes” > Install"
6. 安装后导航去设定 > 一般 > VPN & Device Management > Apple ID > 信任
7. 开启Filza File Manager，第一次开启可能会闪退，重新开几次就好了
8. 在左边按上Apps manager
9. 关上激活Filza的通知（付费的可以绕过这个步骤）
10. 寻找Dynamite之后移步到Documents
11. 全选所有档案，除了Unity档案夹和`__rena_mark_store_3`之外
12. 完成!
13. 有些应用证书可能会被Apple撤销，如果没法安装的话那就是证书被撤销，撤销的话就要用电脑的方法了

##### 依赖电脑
1. 下载Sideloadly (https://sideloadly.io/) 或者 AltServer (https://altstore.io/)， 和FilzaEscaped (https://basvtdevelopments.com/filzaescaped)
2. 在Sideloadly中安装ipa / 安装AltServer之后选择安装AltStore到设备商
3. (只是AltStore需要做以下第三步骤) 在设备商下载FilzaEscaped和Dynamite的.ipa档并在AltStore上安装 
4. 导航去设定 > 一般 > VPN & Device Management > Apple ID > 信任
5. 跳到上方的第七步骤，跟着做就行
10. 完成!
11. 每7天都要手动用Sideloadly/AltServer重新安装过，只要不要删掉Dynamite而且用的Apple ID是同一个账号就不会流失任何data，但是最好是有备份的准备，预防万一
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