import requests
import csv
from lxml import html

#常量
TMDB_BASE_URL="https://www.themoviedb.org/"
TMDB_TOP_URL="https://www.themoviedb.org/movie/top-rated"


#主获取电影详情
def get_movie_info(movie_info_url):
    #1.发送请求,获取电影数据
    movie_response=requests.get(movie_info_url,timeout=60)
    movie_doc=html.fromstring(movie_response.text)
    #2.解析数据,获取电影信息
    movie_name=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    movie_year=movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
    movie_release_data=movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[2]/text()')
    movie_type=movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[3]/a/text()')
    movie_time = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[4]/text()')
    movie_score=movie_doc.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    movie_language=movie_doc.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    movie_director=movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
    movie_author=movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
    movie_slogans=movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()')
    movie_introduction=movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')

    #3.返回电影详情-字典
    movie_info={
        "电影名":movie_name[0].strip() if movie_name else '',
        "年份":movie_year[0].strip() if movie_year else '',
        "上映日期":movie_release_data[0].strip() if movie_release_data else '',
        "类型":",".join(movie_type) if movie_type else '',
        "时长":movie_time[0].strip() if movie_time else '',
        "评分":movie_score[0].strip() if movie_score else '',
        "语言":movie_language[0].strip() if movie_language else '',
        "导演":",".join(movie_director) if movie_director else '',
        "作者":",".join(movie_author) if movie_author else '',
        "宣传语":movie_slogans[0].strip() if movie_slogans else '',
        "简介":movie_introduction[0].strip() if movie_introduction else ''
    }
    print(movie_info)
    return movie_info



#保存电影数据
def save_movies(all_movie):
    pass


def main():
    #1.发送请求
    response=requests.get(TMDB_TOP_URL,timeout=60)
    #2.解析数据获取电影列表
    document=html.fromstring(response.text)
    movie_list=document.xpath('//*[@id="page_1"]//div[contains(@class, comp.poster-card)]')

    #3.遍历电影列表,获取电影详情
    all_movie=[]
    for movie in movie_list:
        movie_url = movie.xpath("./div/div/a[@class='flex w-full']/@href")
        if movie_url:
            movie_info_url =  TMDB_BASE_URL +movie_url[0]

            #发送请求,获取电影详情数据
            movie_info=get_movie_info(movie_info_url)
            all_movie.append(movie_info)
    #4.保存数据,保存为csv文件
    save_movies(all_movie)



if __name__=="__main__":

    main()




