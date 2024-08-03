# PhoneCard
本程序主要用于统计批量通话结果。可以将包含联系人姓名和电话的excel文档转化成卡片，方便阅读，并且可以统计最后的结果，查看上次通话的历史记录等等。
<p align="center">
  <img src="https://github.com/worldtree43/PhoneCard/blob/main/img/Phonecard_1.png" alt="Phonecard 1" width="200"/>
  <img src="https://github.com/worldtree43/PhoneCard/blob/main/img/Phonecard_2.png" alt="Phonecard 2" width="200"/>
  <img src="https://github.com/worldtree43/PhoneCard/blob/main/img/Phonecard_3.png" alt="Phonecard 3" width="200"/>
  <img src="https://github.com/worldtree43/PhoneCard/blob/main/img/Phonecard_4.png" alt="Phonecard 4" width="200"/>
</p>

****

## 程序结构

```flashcard.py```: 管理联系人联系的流程，包括显示联系人信息、记录联系结果、显示汇总信息以及重新联系失败的联系人

```column_selection.py```: 选择 Excel 文件和指定联系人和电话所在的列，并启动联系人联系流程，显示历史记录

```history_manager.py```: 管理历史记录的加载，保存，获取。

```randphonenum.py```: 测试类 用来生成contacts.xlsx
