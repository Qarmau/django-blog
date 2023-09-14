from django.db import models

topics=(
    ('World','World'),
    ('Kenya','Kenya'),
    ('Africa','Africa'),
    ('Technology','Technology'),
    ('Design','Design'),
    ('Culture','Culture'),
    ('Business','Business'),
    ('Politics','Politics'),
    ('Opinion','Opinion'),
    ('Science','Science'),
    ('Health','Health'),
    ('Style','Style'),
    ('Travel','Travel')
    )


class BlogTopic(models.Model):
    blogtopic=models.CharField(max_length=20,choices=topics)
    created=models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.blogtopic.title()

months=(
    ('Jan','Jan'),
    ('Feb','Feb'),
    ('Mar','Mar'),
    ('Apr','Apr'),
    ('May','May'),
    ('Jun','Jun'),
    ('Jul','Jul'),
    ('Aug','Aug'),
    ('Sep','Sep'),
    ('Oct','Oct'),
    ('Nov','Nov'),
    ('Dec','Dec')
)
class Archive(models.Model):
    month=models.CharField(max_length=20,choices=months)
    year=models.IntegerField()


    def __str__(self):
        return str(self.month)+" "+str(self.year)

class BlogPost(models.Model):
    blog_topic=models.ForeignKey(BlogTopic,on_delete=models.CASCADE)
    blog_post=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=255,default='admin')

    def __str__(self):
        return str(self.blog_topic)+' updated'
