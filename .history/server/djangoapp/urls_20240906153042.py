# Uncomment the imports before you add the code
<<<<<<< HEAD
# from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# from . import views
=======
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
>>>>>>> fb9fc0d (React login/logout)

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
<<<<<<< HEAD
    # path(route='login', view=views.login_user, name='login'),
=======
    path(route='login', view=views.login_user, name='login'),

    # path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    # path for registration
    path(route='register', view=views.registration, name='register'),
>>>>>>> fb9fc0d (React login/logout)

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
