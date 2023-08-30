from django.shortcuts import render
from datetime import date


all_posts =[
    {
        "slug": "hike_in_the_mountains",
        "image": "mountains.jpg",
        "author": "Mira",
        "date": date(2023,8,5),
        "title": "Hiking",
        "exerpt": "Something about hiking",
        "content": "hvyoirhvorygvouhvyoirhvoryghvyoirhvorygvoutjdchilwehvguwygoweirvoutjdchilwehvguwygoweirtjdchilwehvguwygoweir"
    },
    {
        "slug": "hike_in_the_mountains",
        "image": "mountains.jpg",
        "author": "Mira",
        "date": date(2023,6,5),
        "title": "Hiking",
        "exerpt": "Something about hiking",
        "content": "hvyoirhvorygvouhvyoirhvoryghvyoirhvorygvoutjdchilwehvguwygoweirvoutjdchilwehvguwygoweirtjdchilwehvguwygoweir"
    },
    {
        "slug": "hike_in_the_mountains",
        "image": "mountains.jpg",
        "author": "Mira",
        "date": date(2023,8,2),
        "title": "Hiking",
        "exerpt": "Something about hiking",
        "content": "hvyoirhvorygvouhvyoirhvoryghvyoirhvorygvoutjdchilwehvguwygoweirvoutjdchilwehvguwygoweirtjdchilwehvguwygoweir"
    },
    {
        "slug": "hike_in_the_mountains",
        "image": "mountains.jpg",
        "author": "Mira",
        "date": date(2023,23,5),
        "title": "Hiking",
        "exerpt": "Something about hiking",
        "content": "hvyoirhvorygvouhvyoirhvoryghvyoirhvorygvoutjdchilwehvguwygoweirvoutjdchilwehvguwygoweirtjdchilwehvguwygoweir"
    },
    {
        "slug": "hike_in_the_mountains",
        "image": "mountains.jpg",
        "author": "Mira",
        "date": date(2023,13,5),
        "title": "Hiking",
        "exerpt": "Something about hiking",
        "content": "hvyoirhvorygvouhvyoirhvoryghvyoirhvorygvoutjdchilwehvguwygoweirvoutjdchilwehvguwygoweirtjdchilwehvguwygoweir"
    }

]

def get_date(post):
   return post ['date']

# Create your views here.

def starting_page (request):
    sorted_posts = all_posts.sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render (request, "blog/index.html", {
        "posts": latest_posts
    })


def posts (request):
    return render (request, "blog/posts.html",{
         "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next (post for post in all_posts if post['slug']==slug)
    return render (request, "blog/posts_detail.html", {
        "post": identified_post
    })