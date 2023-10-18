from django.utils import timezone

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            #print(user.timezone)
            timezone.activate(user.timezone)
        else:
            timezone.deactivate()  # Use the default timezone for anonymous users
        response = self.get_response(request)
        return response
