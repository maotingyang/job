# Given a list of urls, print out the top 3 frequent filenames.
# ex.
# Given
# urls = [
# "http://www.google.com/a.txt",
# "http://www.google.com.tw/a.txt",
# "http://www.google.com/download/c.jpg",
# "http://www.google.co.jp/a.txt",
# "http://www.google.com/b.txt",
# "https://facebook.com/movie/b.txt",
# "http://yahoo.com/123/000/c.jpg",
# "http://gliacloud.com/haha.png",
# ]
# The program should print out
# a.txt 3
# b.txt 2
# c.jpg 2

#=======================解題==========================


urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

count = {}   #準備一個紀錄文件出現次數的字典
for url in urls:
    the_list = url.split('/')    #把網址用反斜線拆開，取最後一塊字串就是文件名了
    doc = the_list[-1]
    if count.get(doc):
        count[doc] += 1
    else:
        count[doc] = 1

count = sorted(count.items(), key=lambda x:x[1], reverse=True)   #依字典鍵值排序   
print(count)            