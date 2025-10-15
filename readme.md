# Django Clinic Project

## Steps to build the project

### 2. create project folder

```bash

django-admin startproject erb7 .

```

### 4. run the server

```py

from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include("pages.urls", namespace="pages")),
    path('listings/',include("listings.urls", namespace="listings")),
    path('contacts/',include("contacts.urls", namespace="contacts")),
    path('accounts/',include("accounts.urls", namespace="accounts")),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ERB7 Medical Center Admin Portal"
admin.site.site_title = "ERB7 Medical Center Admin Portal"
admin.site.index_title = "Welcome to ERB7 Medical Center Admin Portal"

```

```html
<html>
    <body>
    </body>
</html>
```
