from django.db import models


class AboutMe(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    lang = models.CharField(max_length=200)
    cv_media = models.FileField(upload_to="my_cv/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"


class Social(models.Model):
    telegram = models.CharField(max_length=120)
    github = models.CharField(max_length=120)
    linkedin = models.CharField(max_length=120)
    instagram = models.CharField(max_length=120)
    facebook = models.CharField(max_length=120)
    twitter = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Social network"

    class Meta:
        verbose_name = "Social network"
        verbose_name_plural = "Social networks"


class Experience(models.Model):
    name = models.CharField(verbose_name="Company name", max_length=120)
    description = models.TextField()
    position = models.CharField(max_length=120)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    company_url = models.CharField(max_length=120, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiments"


class Project(models.Model):
    name = models.CharField(verbose_name="Project name", max_length=120)
    image = models.FileField(upload_to="project_pics/")
    description = models.TextField(verbose_name="About the project")
    position = models.CharField(verbose_name="Programming position", max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    project_url = models.CharField(verbose_name="Project url", max_length=120)
    github = models.CharField(verbose_name="Github url", max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Project: {self.name}"

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    theme = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class BlogImage(models.Model):
    name = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog_pict/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.title

    class Meta:
        verbose_name = "Blog image"
        verbose_name_plural = "Blog images"
