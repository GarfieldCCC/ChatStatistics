# ChatStatistics
统计微信聊天信息

## 使用配置
- python3

## 准备
- 安装python3(建议直接安装anaconda，它拥有丰富的python第三方库)
- 安装第三方库 jieba 和 itchat
```
# 安装anaconda之后打开命令行窗口，输入下面两个命令: 
pip install jieba
pip install itchat
```

## 代码的功能
- Attention
``` python
def handle_receive_msg(msg):
    stopwords_path = "stopwords_path"			#这是停用词文件的路径
    excel_path1 = "WordCount_path"			#这是词频统计文件的路径
    excel_path2 = "Time_path"			#这是信息时间分布的路径
    excel_path3 = "Date_path"           # 这是日期分布的路径
    name = "备注名"			#这是你想要统计的用户的备注名
    now = datetime.datetime.now()
    hour = str(int(now.strftime('%H')))
    Date = getDate()
```
这段程序中您需要修改的是四个路径(停用词文件的路径, 词频统计文件的路径, 信息时间分布的路径, 日期分布的路径)。
其中信息时间分布的路径, 词频统计文件的路径和日期分布的路径均为.xls文件(Excel文件)。
此外您还需要将name修改为您想要统计的那个用户的备注。

## 注意
**词频统计文件**, **信息时间分布文件**和**日期分布文件**这三个文件需要提前创建好并在其中提前输入好内容。
<BR/>
**词频统计文件**的格式如下：
<BR/>
![image_1c6mlql651pd2gnbgh6a9b115c9.png-1.5kB][1]
<BR/>
**信息时间分布文件**的格式如下：
<BR/>
![image_1c6mltr7dlv21ch81mua91tv5em.png-8.9kB][2]
<BR/>
**日期分布文件**的格式如下：
<BR/>
![image_1c7b3shuu6tu9qvcn21cvghcd9.png-1.4kB][3]
<BR/>

## 使用
Download下来确认一切无误之后直接运行Chat.py即可。

## 效果
**词频**：
<BR/>
![image_1c6mm3evdbn2opg4fk12h21asb13.png-8.2kB][4]
<BR/>
**信息时间分布**：
<BR/>
![image_1c6mm57h21n2n1ku619gvn02127u1g.png-12.3kB][5]
<BR/>
**日期分布文件**：
<BR/>
![image_1c7b3ve0s1nqm18jq1c2arnc1a2lm.png-1.7kB][6]
<BR/>

## 思考
本人认为将信息存入数据库更好，后续将尝试修改。


  [1]: http://static.zybuluo.com/GarfieldMty/f7c125l6xrv1n7qs3jno7w6x/image_1c6mlql651pd2gnbgh6a9b115c9.png
  [2]: http://static.zybuluo.com/GarfieldMty/niwpzijbinvgkt4wqnhngo5b/image_1c6mltr7dlv21ch81mua91tv5em.png
  [3]: http://static.zybuluo.com/GarfieldMty/95o25c5fg1c65lif7nof2lut/image_1c7b3shuu6tu9qvcn21cvghcd9.png
  [4]: http://static.zybuluo.com/GarfieldMty/g0cdohmow1s7yluvmc1daak8/image_1c6mm3evdbn2opg4fk12h21asb13.png
  [5]: http://static.zybuluo.com/GarfieldMty/hh2ajkgmro7eey3jbshggj35/image_1c6mm57h21n2n1ku619gvn02127u1g.png
  [6]: http://static.zybuluo.com/GarfieldMty/a08ng9duo6jipqd7yfge21a5/image_1c7b3ve0s1nqm18jq1c2arnc1a2lm.png