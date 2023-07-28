该project仅为狗剩一人服务，仅为抓取港交所懂事变动的数据并生成csv文件（后来发现傻了其实并不需要港股公司列表lol）

如有雷同，不胜荣幸

香港交易所上市公司列表.csv是从：https://zh.wikipedia.org/wiki/%E9%A6%99%E6%B8%AF%E4%BA%A4%E6%98%93%E6%89%80%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B8%E5%88%97%E8%A1%A8
爬取得到

process：
1. 从这里获取全部directors的excel信息：https://www3.hkexnews.hk/reports/dirsearch/?sc_lang=en
2. 直接筛选appointment在1997年到2000年之间的或resignation在1997到2000年之间的（因为有可能appointment列是空的）

...
