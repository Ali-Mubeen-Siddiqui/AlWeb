from django.contrib.sitemaps import Sitemap

class StaticSitemapView(Sitemap):
    def items(self):
        return [
            '/',                # Home path
            
            '/home',
            '/contact',         # Contact path
            '/book-us',         # Book Us path
            '/gallery',         # Gallery path
            '/reviews',         # Reviews path
            '/add-review',      # Add Review path
            '/privacy-policy'   # Privacy Policy path
        ]
    
    def location(self, item):
        return item
