from django.db import models
import string, random

class ShortURL(models.Model):
    original_url = models.URLField(max_length=2000)  # Some URLs can be long
    short_code = models.CharField(max_length=6, unique=True)
    generated_at = models.DateTimeField(auto_now_add=True)  # Use DateTimeField
    click_count = models.IntegerField(default=0)  # No need for max_length

    def __str__(self):
        return f"{self.short_code} - {self.original_url[:50]}"

    @staticmethod
    def generate_short_code(length=4):
        characters = string.ascii_lowercase + string.digits
        while True:
            code = ''.join(random.choice(characters) for _ in range(length))
            if not ShortURL.objects.filter(short_code=code).exists():
                return code