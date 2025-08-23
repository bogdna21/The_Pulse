from news.forms import NewspaperSearchForm, TopicSearchForm, RedactorSearchForm, EmailVerificationForm, SetNewPasswordForm


def test_newspaper_search_form_valid():
    form = NewspaperSearchForm({"title": "Some title"})
    assert form.is_valid()


def test_topic_search_form_valid():
    form = TopicSearchForm({"name": "Tech"})
    assert form.is_valid()


def test_redactor_search_form_valid():
    form = RedactorSearchForm({"username": "user"})
    assert form.is_valid()


def test_email_verification_form_valid():
    form = EmailVerificationForm({"email": "user@example.com"})
    assert form.is_valid()


def test_set_new_password_form_valid():
    form = SetNewPasswordForm({"new_password1": "12345test", "new_password2": "12345test"})
    assert form.is_valid()
