import requests
import csv
from lxml import html

#常量
TMDB_BASE_URL="https://www.themoviedb.org/"
TMDB_TOP_URL="https://www.themoviedb.org/movie/top-rated"


#主获取电影详情
def get_movie_info(movie_info_url):
    pass

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




