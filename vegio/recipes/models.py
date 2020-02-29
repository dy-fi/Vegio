from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

import json

# Full recipe info model
class Recipe(models.Model):
    """
    Represents a single recipe
    """
    spoon_id = models.CharField(max_length=300)

    title = models.CharField(max_length=300, help_text="Recipe Title")

    summary = models.TextField(help_text="Recipe Summary")

    image_url = models.CharField(max_length=400)
    
    source_url = models.CharField(max_length=300, help_text="Recipe Url")

    slug = models.CharField(max_length=1000, blank=True, editable=False, help_text="URL to find this recipe")

    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this page was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True,
                                    help_text="The date and time this page was updated. Automatically generated when the model updates.")

    def __str__(self):
        return self.title
                                    
    def set_wines(self, x):
        self.wines = json.dumps(x)
    
    def get_wines(self):
        return json.loads(self.wines)
    
    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-wiki-page). """
        path_components = {'slug': self.slug}
        return reverse('wiki-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Page, self).save(*args, **kwargs)