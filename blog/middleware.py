from django.contrib.auth.models import Group


class GroupsContextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.user.is_authenticated():
            groups = Group.objects.filter(user=request.user)
            response.groups = groups
        return response
