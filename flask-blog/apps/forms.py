from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistForm(FlaskForm):
    
    user_name = StringField(
        label = '你的名字',
        validators = [DataRequired(message='用户名不能为空')],
        render_kw = {'id': 'user_name','class': 'form-control',}
    )

    user_pwd = PasswordField(
        label = '你的密码',
        validators = [DataRequired(message='密码不能为空')],
        render_kw = {
            'id': 'user_pwd',
            'class': 'form-control'
        }
    )

    submit = SubmitField(
        label='提交表单', 
        render_kw = {
            'class': 'btn btn-success',
            'value': '注册',
            }
        )


class LoginForm(FlaskForm):

    user_name = StringField(
        label = '你的名字',
        validators = [DataRequired(message='输入不能为空')],
        render_kw = {'id': 'user_name','class': 'form-control'}
    )

    user_pwd = PasswordField(
        label = '你的密码',
        validators = [DataRequired(message='输入不能为空')],
        render_kw = {
            'id': 'user_pwd',
            'class': 'form-control'
        }
    )

    submit = SubmitField(
        label = '提交表单', 
        render_kw = {
            'class': 'btn btn-success',
            'value': '登陆',
            }
        )


class PwdForm(FlaskForm):

    old_pwd = PasswordField(
        label = '旧密码',
        validators = [DataRequired(message='输入不能为空')],
        render_kw = {'id': 'old_pwd', 'class': 'form-control'}
    )

    new_pwd = PasswordField(
        label = '旧密码',
        validators = [DataRequired(message='输入不能为空'), 
                     Length(min=3, max=20, message='长度在3-20之间')],
        render_kw = {'id': 'old_pwd', 'class': 'form-control'}
    )

    submit = SubmitField(
        label = '提交表单',
        render_kw = {'class': 'btn btn-success', 'value': '修改'}
    )

