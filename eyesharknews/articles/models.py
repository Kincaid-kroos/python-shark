from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    SPORTS = 'sports'
    ENTERTAINMENT = 'entertainment'
    TECH  = 'tech'
    BUSINESS = 'business'
    POLITICS = 'politics'
    WORLDNEWS = 'worldnews'
    MORE= 'more'
    
class BlogPosts(models.Model): 
    title = models.CharField(max_length=50) 
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.BUSINESS)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.CharField(max_length=150)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    latest = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    hero = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    
    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPosts.objects.all().filter(slug__iexact=original_slug).count()
        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPosts.objects.all().filter(slug__iexact=slug).count()
        self.slug = slug

        # If the post is marked as hero and not already featured, select any hero post to feature
        if self.hero and not self.featured:
            try:
                # Check if there's any hero post currently featured
                featured_hero = BlogPosts.objects.get(hero=True, featured=True)
            except BlogPosts.DoesNotExist:
                featured_hero = None

            # If no hero post is currently featured, mark the current one as featured
            if not featured_hero:
                self.featured = True
            else:
                # If there's another hero post featured, unfeature it
                if self != featured_hero:
                    featured_hero.featured = False
                    featured_hero.save()

        # If the post is marked as latest and not already featured, select any latest post to feature
        if self.latest and not self.featured:
            try:
                # Check if there's any latest post currently featured
                featured_latest = BlogPosts.objects.get(latest=True, featured=True)
            except BlogPosts.DoesNotExist:
                featured_latest = None

            # If no latest post is currently featured, mark the current one as featured
            if not featured_latest:
                self.featured = True
            else:
                # If there's another latest post featured, unfeature it
                if self != featured_latest:
                    featured_latest.featured = False
                    featured_latest.save()

        super(BlogPosts, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
