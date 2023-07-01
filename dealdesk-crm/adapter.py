from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Custom account adapter to disable account signup.

    The adapter extends the DefaultAccountAdapter provided by Django allauth.
    By overriding the `is_open_for_signup` method, account signup functionality
    is disabled, preventing users from registering for the application.

    """

    def is_open_for_signup(self, request):
        return False
