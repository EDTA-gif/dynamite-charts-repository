Dynamite Backup Project
===

> Translated by Jmak

## Charts Included
* All ranked and unranked charts that were approved by June 10, 2022 before Dynamite servers were terminated
* Filenames, file structures and `__rena_index_2` are rearranged
* The data retains the in-game encryption and can only be imported into Dynamite to play
* GitHub is only used for file statistic and revision purposes. After all the charts are completed, a faster download approach for Mainland China network will be provided.

## List of Songs
* Most of the subfolders in the Charts folder are named according to the format of `<song title>(<charter>)`. For songs that has more than one version, it will be renamed as `<song title>_<ranked status>(<charter>)`
* As there are too many charts, GitHub will only show the first 1,000 subfolders, so please navigate to `rena_index_list` and use `Ctrl+F` to search for track names in the file's source code
* If you encounter one of the following cases, please submit an Issue and I will fix it or update it in the README
   * Cannot find a chart that you are sure that has passed the review
   * A track's chart file or music file doesn't play properly 
* Missing chart sets：
   * Ignotus Afterburn Giga 2041 By Rezasho, Unranked，2020 April Fools Chart
   * εxceζ Giga 15 By γraphitε，Unranked，Approved as Unranked in 20:09 June 8, 2022
   * {albus} Giga 14 By Graphite，Unranked，Approved as Unranked in 20:10 June 8, 2022
* If you have saved the chart data mentioned above locally and want to extract it and upload it, please package the chart files and the `__rena_index_2` file containing the corresponding information and send it to trickl4sh220@foxmail.com
   * If you have the ability to fork and make changes within GitHub, I can merge it afterwards (preferrable)
   * If you are sure that you have saved it but you cannot find the corresponding game file, you can send the entire files as a compressed package, but considering the file size, it is not recommended to do so

## Importing Method

> To import custom chart to dynamite, see [this](./Custom_Import_Tutorial_EN.md)

### Android

> Original Post in Bilibili：[Link](https://www.bilibili.com/read/cv17021429)

1. Back up local data
2. Empty all files with the .rnx suffix in `Android > data > tech.dynami.dynamite > files`
   * The game can only indentify files listed in the `index` file that's going to be overwrite in the following steps, so you can remove your local data to save space.
3. Put all the files in the Charts folder into this directory, and overwrite the local corresponding files with the `__rena_index_2` file in the folder
4. You can now play in offline mode

> For Android systems with version 12 or higher, if your file manager cannot access `Android/data`, please consider using tools such as Magisk to root

### iOS (Sideloadly)

> Original Post in Bilibili：[Link](https://www.bilibili.com/read/cv17026497)

1. Prepare the `.ipa` Dynamite file to install 
2. Download Sideloadly from their [official website](https://sideloadly.io/)
3. Install ipa after checking the following options in Sideloadly
   * Enable UIFileSharing
   * Remove limitation on supported devices
4. Use software such as imazing, iTunes or i4 Assistant (爱思助手) to find the Dynamite program you installed in the application management through iTunes File Sharing, within the `/Documents` directory is the content of the chart data, equivalent to Android `/files`
5. You will have to re-sign the application every 7 days with Sideloadly. As long as you do not delete the Dynamite app and use the same Apple ID to sign with Sideloadly, you will not lose any data, but it's always best to backup data.

### iOS (Filza file explorer)

> By [Jmak](https://docs.google.com/document/d/1-1ydDVTnuJO2g49b-9FFa9vXiAFRLGUEK4ullHnD2fU)

**Suitable for iOS 11-13.4.1 / 15-15.1.1 only**

##### Without computer
1. Download FilzaEscaped from this website (https://basvtdevelopments.com/filzaescaped) 
2. Go to Freebox (https://freebox.co/web/signer/)
3. Choose the .ipa file for FilzaEscaped in Freebox by tapping Choose File > Browse > Dynamite.ipa > Sign > Wait for it to download > Choose Open on “Open this page in iTunes” > Install
4. Navigate to Settings > General > VPN & Device Management > Apple ID > Trust
5. Choose the .ipa Dynamite file in Freebox by tapping Choose File > Browse > Dynamite.ipa > Sign > Wait for it to download > Choose Open on “Open this page in iTunes” > Install
6. After installation, navigate to Settings > General > VPN & Device Management > Apple ID > Trust
7. Open Filza File Manager. The first time you launch it, the app may crash. Just reopen it a few times and you should get access
8. Click on Apps manager on the left sidebar
9. Close off the activate notification (Paid users can ignore this step)
10. Search for the app Dynamite and navigate to the Documents folder
11. Select all the files except for`__rena_mark_store_3`and the Unity folder
12. Finished!
13. Apple may revoke some app certificates. If you cannot install the apps, Apple has revoked them, leaving you with the computer method. Make sure you have a backup of your chart files just in case.

##### With computer
1. Download Sideloadly (https://sideloadly.io/) or AltServer (https://altstore.io/), and FilzaEscaped(https://basvtdevelopments.com/filzaescaped)
2. Install ipa in Sideloadly / Install AltServer and select install AltStore to your device
3. (Only AltStore users are required to do Step 3) Download FilzaEscaped and Dynamite .ipa file from your device and use AltStore to install
4. Navigate to Settings > General > VPN & Device Management > Apple ID > Trust
5. Jump to step 7 as above, just follow the instructions
10. Finished!
11. You will have to resign the application every 7 days with Sideloadly/AltServer. As long as you do not delete the Dynamite app and use the same Apple ID to sign with, you will not lose any data, but it's always best to backup data.

### iOS (Jailbreak)

> By [Jmak](https://docs.google.com/document/d/1-1ydDVTnuJO2g49b-9FFa9vXiAFRLGUEK4ullHnD2fU)

1. Do not delete the Dynamite app downloaded from TestFlight, the following method will allow expired apps to be used normally
2. Add the following source (http://cydia.kiiimo.org) or (https://repo.hackyouriphone.org) and install Anti-Revoke 2 with Cydia/Sileo (Zebra or others also work)
3. Make sure you have installed Filza File Manager from Cydia/Sileo or other jailbreak stores, free or paid version does not matter
4. Click on Apps manager on the left sidebar
5. Close off the activate notification (Paid users can ignore this step)
6. Search for the app Dynamite and navigate to the Documents folder
7. Select all the files except for `__rena_mark_store_3` and the Unity folder
8. Finished!

## Links to other Dynamite related documents

[R value tier list for dynamite ranked charts](https://www.bilibili.com/read/cv16981243)

[Formula for R value calculation according to your performance](https://www.bilibili.com/read/cv17024921)

## Special Thanks
* i0nTempest
* Errno
* Jmak