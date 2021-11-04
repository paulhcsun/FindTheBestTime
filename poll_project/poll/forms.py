from django.forms import ModelForm

from .models import Poll


class CreatePollForm(ModelForm):
    # TODO: add a toggle between select multiple answers and YES/NO
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two']

    # def save(self, commit=True):
    #     instance = super(CreatePollForm, self).save(commit=False)
    #     instance.poll_id = self.random_with_n_digits(8)
    #     if commit:
    #         instance.save()
    #     return instance
