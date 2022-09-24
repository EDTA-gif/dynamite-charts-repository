Dynamite Backup Project
===

> Translated by Jmak

<!-- TOC -->

- [Dynamite Backup Project](#dynamite-backup-project)
  - [Charts Included](#charts-included)
  - [List of Songs](#list-of-songs)
  - [Importing Method](#importing-method)
    - [Android](#android)
    - [iOS (Sideloadly/AltStore)](#ios-sideloadlyaltstore)
    - [iOS (Jailbreak)](#ios-jailbreak)
  - [Links to other Dynamite related documents and tutorial videos](#links-to-other-dynamite-related-documents-and-tutorial-videos)
  - [Special Thanks](#special-thanks)

<!-- /TOC -->

## Charts Included
* All ranked and unranked charts that were approved by June 10, 2022 before Dynamite servers were terminated
* Filenames, file structures and `__rena_index_2` are rearranged
* The data retains the in-game encryption and can only be imported into Dynamite to play
* GitHub is only used for file statistic and revision purposes. After all the charts are completed, a faster download approach for Mainland China network will be provided.

## List of Songs
* Most of the subfolders in the Charts folder are named according to the format of `<song title>(<charter>)`. For songs that has more than one version, it will be renamed as `<song title>_<ranked status>(<charter>)`
* As there are too many charts, GitHub will only show the first 1,000 subfolders, so please navigate to `rena_index_list` and use `Ctrl+F` to search for track names in the file's source code
* If you encounter one of the following cases, please submit an Issue or send an e-mail to trickl4sh220@foxmail.com, I will fix it or update it in the README
   * Cannot find a chart that you are sure that has passed the review
   * A track's chart file or music file doesn't play properly

## Importing Method

> **To import custom chart to dynamite, see [this](./Custom_Import_Tutorial_EN.md)**

### Android

> Original Post in Bilibili：[Link](https://www.bilibili.com/read/cv17021429)

1. Back up local data
2. Empty all files with the .rnx suffix in `Android > data > tech.dynami.dynamite > files`
   * The game can only indentify files listed in the `index` file that's going to be overwrite in the following steps, so you can remove your local data to save space.
3. Put all the files in the Charts folder into this directory, and overwrite the local corresponding files with the `__rena_index_2` file in the folder
4. You can now play in offline mode

> For Android systems with version 11 or higher, if your file manager cannot access `Android/data`, please consider using tools such as Magisk to root

> Google fixed the SAF bug in Android 13, this solution may not work on Android 13 devices, if this happens please use [Shizuku](https://shizuku.rikka.app/)/[Sui](https://github.com/RikkaApps/Sui) or [Magisk](https://github.com/topjohnwu/Magisk)

### iOS (Sideloadly/AltStore)

> References：
> 
> [iOS import method post in Bilibili](https://www.bilibili.com/read/cv17026497) & 
> [Jmak's manual](https://docs.google.com/document/d/1-1ydDVTnuJO2g49b-9FFa9vXiAFRLGUEK4ullHnD2fU)

1. Download the `Dynamite_filesharing.ipa` file in [releases](https://github.com/EDTA-gif/dynamite-charts-repository/releases/tag/Game_executable)
2. Choose one of the following blocks and follow the guide in it
   
> * Download Sideloadly from their [official website](https://sideloadly.io/) and install it on your PC
> * Connect your iOS device to your PC and install the dynamite ipa via Sideloadly (with default Sideloadly settings)

> * Download Altserver from their [official website](https://altstore.io/) and install it on your PC
> * Connect your iOS device to your PC and install AltStore via AltServer
> * Install the Dynamite ipa via AltStore
  
3. You may need to go to `Settings -> General -> Profiles & Device Management` to trust the Apple ID you used to install the apps
4. Now you can use PC software such as imazing, iTunes or i4 Assistant (爱思助手), or the default File application on your iOS device, to manage the data of the Dynamite program. within the `/Documents` directory is the content of the chart data, equivalent to Android `/files`
5. You will have to re-sign the application every 7 days with Sideloadly/AltStore. Though as long as you do not delete the Dynamite app and use the same Apple ID to sign, you will not lose any data, it's still recommended to backup your data regularly.

### iOS (Jailbreak)

> By [Jmak](https://docs.google.com/document/d/1-1ydDVTnuJO2g49b-9FFa9vXiAFRLGUEK4ullHnD2fU)

1. Do not delete the Dynamite app downloaded from TestFlight, the following method will allow expired apps to be used normally
2. Add the following source (http://cydia.kiiimo.org) or (https://repo.hackyouriphone.org) and install Anti-Revoke 2 with Cydia/Sileo (Zebra or others also work)
3. Make sure you have installed Filza File Manager from Cydia/Sileo or other jailbreak stores, free or paid version does not matter
4. Click on Apps manager on the left sidebar
5. Close off the activate notification (Paid users can ignore this step)
6. Search for the app Dynamite and navigate to the Documents folder
7. Delete all the files except for `__rena_mark_store_3` and the Unity folder to save space
8. Finished!

## Links to other Dynamite related documents and tutorial videos

[R value tier list for dynamite ranked charts](https://www.bilibili.com/read/cv16981243)

[Formula for R value calculation according to your performance](https://www.bilibili.com/read/cv17024921)

[Custom chart import methods' demostration (Bilibili video)](https://www.bilibili.com/video/BV13v4y1G7sZ)

[Installing ipa file and importing data (Bilibili video)](https://www.bilibili.com/video/BV1ST411V72Q)

## Special Thanks
* i0nTempest
* Errno
* Jmak
* asasaxd
* eastown
