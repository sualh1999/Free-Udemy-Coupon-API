from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
  def send_account_already_exists_mail(self, email):
    return ""
