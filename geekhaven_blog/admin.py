from django.contrib import admin
from .models import BlogPost, BlogComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
# passing in SummernoteModelAdmin allows for use of summernote on admin panel
class AdminSearchOption(SummernoteModelAdmin):
    search_options = (
        "blog_heading",
        "url_slug",
        "blog_published_status",
        "creation_date",
    )
    search_by_heading = ["blog_heading"]
    search_filter = ("blog_published_status",)
    prepopulated_fields = {
        # slug field(url creator) is automatically populated using the blog title
        "url_slug": ("blog_heading",)
    }
    summernote_text_fields = (
        # assigns the use of summernote only to the blog_content field
        "blog_content"
    )


admin.site.register(BlogComment)
