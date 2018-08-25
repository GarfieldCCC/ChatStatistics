import itchat, xlwt, xlrd, datetime
import jieba
jieba.load_userdict("userdict.txt")

from itchat.content import *
from itchat.content import TEXT
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO])
def handle_receive_msg(msg):
    stopwords_path = "stopwords_path"  # 这是停用词文件的路径
    excel_path1 = "excel_path1"  # 这是词频统计文件的路径
    excel_path2 = "excel_path2"  # 这是信息时间分布的路径
    excel_path3 = "excel_path3"  # 这是日期时间分布的路径
    name = "备注"  # 这是你想要统计的用户的备注名
    now = datetime.datetime.now()
    hour = str(int(now.strftime('%H')))
    Date = getDate()

    if itchat.search_friends(userName=msg['FromUserName'])['RemarkName'] == name:

        dictionary2 = getExcelInfo(excel_path3)
        dic2 = getDateDictionary(Date, dictionary2)
        writeToExcel(excel_path3, dic2)

        if msg['Type'] == "Text":
            Dictionary = Text(msg['Content'], stopwords_path)
            dictionary = getExcelInfo(excel_path1)
            dic = getNewDictionary(Dictionary, dictionary)
            writeToExcel(excel_path1, dic)

            dictionary = getExcelInfo(excel_path2)
            dic = getHourDictionary(hour, dictionary)
            writeToExcel(excel_path2, dic)
        else:
            dictionary1 = getExcelInfo(excel_path2)
            dic1 = getHourDictionary(hour, dictionary1)
            writeToExcel(excel_path2, dic1)
            info = "这是一条" + str(msg['Type']) + "消息"
            itchat.send_msg(info, toUserName='filehelper')


def loadStopWords(file_path):
    stopwords = []
    for line in open(file_path, encoding='utf-8'):
        stopwords.append(line.strip())
    return stopwords

def Text(msg, file_path):
    dic = []
    itchat.send_msg(msg, toUserName='filehelper')
    print(msg)
    stopwords = loadStopWords(file_path)
    seg_list = jieba.cut(msg, cut_all=False)
    for item in seg_list:
        if item not in stopwords:
            dic.append(str(item))
    return dic

def getExcelInfo(file_name):
    dictionary = {}
    excel = xlrd.open_workbook(file_name)
    table = excel.sheets()[0]
    sheet_by_name = excel.sheet_by_name(file_name)
    nrows = table.nrows
    for i in range(nrows):
        word = str(sheet_by_name.row_values(i)[0])
        number = int(sheet_by_name.row_values(i)[1])
        dictionary[word] = number
    return dictionary

def getNewDictionary(Dictionary, dictionary):
    # Dictionary是获得的句子, dictionary是Excel的数据
    for word in Dictionary:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    itchat.send_msg(str(Dictionary), toUserName='filehelper')
    return dictionary

def getHourDictionary(Hour, dictionary):
    # Hour是获得的小时信息, dictionary是Excel的数据
    dictionary[Hour] += 1
    return dictionary

def writeToExcel(excel_path, dictionary):
    file = xlwt.Workbook(encoding='utf-8')
    table = file.add_sheet(excel_path)
    row = 0
    for item in dictionary:
        table.write(row, 0, item)
        table.write(row, 1, dictionary[item])
        row += 1
    file.save(excel_path)

def getDate():
    # 获取日期信息
    t = datetime.datetime.now()
    date = str(t.year) + "_" + str(t.month) + "_" + str(t.day)
    return date

def getDateDictionary(Date, dictionary):
    # Date是日期信息, dictionary是Excel的数据
    Dictionary = dictionary
    if Date in Dictionary:
        Dictionary[Date] += 1
    else:
        Dictionary[Date] = 1
    return Dictionary

itchat.auto_login(hotReload=True)
itchat.run()
