from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            print('IS LOGGED IN')
            return redirect('UserHomepage')
        else:
            print('NOT LOGGED IN')
            return view_func(request, *args, **kwargs)

    return wrapper_func
