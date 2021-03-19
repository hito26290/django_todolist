from django import forms

class AddTask(forms.Form):
    new_task = forms.CharField(max_length=200, help_text='登録したいタスクを入力してください(200文字以内)')