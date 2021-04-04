# 单篇文献抓取工具

## 背景

现在虽然有很多文献管理工具，例如Endnotes，但是无疑使用原始的文件夹+pdf的方式更加兼容多平台，这种方式配合坚果云等多设备同步使用非常方便。但是我们平常去浏览器中下载文件，文件名经常是随意的，而且下载的位置经常是放在默认目录下面，事后我们还要对其进行文件夹归档，这次的作业我们就是为了部分解决这个问题。

## 思路

解决的思路分成三步：

1. 从网站上面把pdf文档和配套的ris文档下载下来
2. 利用 ris 文档中的信息修改 pdf 文档的文件名以及ris 文档的名称
3. 根据用户给出的信息将 ris 文件和 pdf 文件移动到合适的文件路径



## 遇到的问题：

1. requests的文档中包含了很多我现在不需要用的内容，初期主要是讲怎么从服务器请求数据，但是我对一般的http数据请求一无所知，应该找一个爬虫的示例来得快些。（[爬虫示例](https://www.jianshu.com/p/da98e3ca8e50)）

2. 使用了如下的代码，但是不知道得到的对象里面存放的是什么东西

   ```python
   r = requests.get('https://api.github.com/events')
   dir(r) # 这个给出了一堆属性但是不知道每个表示什么
   #后面去查了一下开发接口，稍微明白了一点，我们主要爬取到的数据就放在raw, text, content 这三个属性里面，只不过编码方式不一样
   ```

3. 之后分析网站上面的html文档遇到一定困难，主要网站的html文档很长，对于html文档我不是特别清楚

   解决办法：去菜鸟教程上面粗略了解了一下html, css, javascript各自大致的内容后大概对html里面的结构有了一个了解，之后结合浏览器提供的html的调试工具，主要是元素选择器边看边想大概懂了，不过用时比较久

4. 接下来我需要从抓取到的html文档中把pdf文档的 url 和 ris文件的 url 提取出来，需要学习bs4中的过滤器，另外利用元素选择器点击文献下载的按钮可以很快帮我定位 url 在 html 中相关的代码。

5. 遇到一个bug，这个同时运用tag和text进行搜索时，我发现下面例子中第二个文本里面含有Do的tag是不能被检验出来的

   ```python
   html_doc = """
   <html><head><title>The Dormouse's story</title></head>
   
   <p class="story">
   <a>Download citation</a>
   <a>Download citation
   <br>
   </a>
   </p>
   """
   
   from bs4 import BeautifulSoup
   soup = BeautifulSoup(html_doc)
   soup.find_all("a",text=re.compile("Do*"))
   # 输出结果
   #[<a>Download citation</a>]  
   ```

   







