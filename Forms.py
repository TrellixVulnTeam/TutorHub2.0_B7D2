from wtforms import *
from wtforms.validators import *
from wtforms.fields.html5 import *

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])

    email = StringField('Email', [validators.Length(min=1,
                                                    max=150), validators.DataRequired(), validators.email()])
    username = StringField('Username', [validators.Length(min=8
                                                          ), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=8
                                                            ), validators.DataRequired()])
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=8
                                                          ), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=8
                                                            ), validators.DataRequired()])
    remember = BooleanField('Remember me')

language = ['English', '简体中文', '繁体中文', 'Bahasa Melayu', 'Bahasa Indonesia', 'Tamil']

class PersonalInfoForm(Form):
    first_name = StringField("First Name",[validators.Length(max=150), validators.DataRequired()])
    last_name = StringField([validators.Length(min=1, max=150), validators.DataRequired()])
    description = TextAreaField([validators.Length(min=30,max=600)])
    language = SelectField(validators=[DataRequired()], choices=[(lang, lang) for lang in language])
    proficiency = SelectField('Proficiency', choices=[('Basic', 'Basic'), ('Conversational', 'Conversational'), ('Fluent', 'Fluent'), ('Native','Native/Bilingual')],render_kw={'placeholder':"proficiency"})

def nric_check(form,field):
    if not(field.data[0].isalpha() and field.data[-1].isalpha() and field.data[1:-2].isnumeric()):
        raise ValidationError('NRIC not valid')
class ProfessionalInfoForm(Form):
    occupation = StringField( validators =[DataRequired(), Length(min=5,max=60)])
    fromyear = StringField(validators =[DataRequired(), Length(min=4,max=4)])
    toyear = StringField(validators =[DataRequired(), Length(min=4,max=4)])
    college_country = StringField(validators =[DataRequired(), Length(min=4,max=30)])
    college_name = StringField(validators =[DataRequired(), Length(min=2,max=60)])
    major = StringField(validators =[DataRequired(), Length(min=5,max=60)])
    graduateyear = StringField(validators =[DataRequired(), Length(min=4,max=4)])
    dob = DateField(format='%Y-%m-%d')
    nric = StringField(validators =[DataRequired(), Length(min=9,max=9), nric_check])

class ProfileEditForm(Form):
    username = StringField(validators=[Length(min=1), DataRequired()])
    firstname = StringField(validators=[Length(max=150), DataRequired()])
    lastname = StringField(validators=[Length(max=150), DataRequired()])
    description = TextAreaField()
    language = SelectField(validators=[],choices = [(lang,lang) for lang in language])
    proficiency = SelectField('Proficiency',choices=[('Basic', 'Basic'), ('Conversational', 'Conversational'), ('Fluent', 'Fluent'),('Native', 'Native/Bilingual')], render_kw={'placeholder': "proficiency"})
categorykeys = ['GRAPHICS & DESIGN','DIGITAL MARKETING','WRITING & TRANSLATION','PROGRAMMING & TECH']
categories = {'GRAPHICS & DESIGN':['LOGO DESIGN','BRAND STYLE GUIDES','GAME ART','RESUME DESIGN'],
              'DIGITAL MARKETING':['SOCIAL MEDIA ADVERTISING','SEO','PODCAST MARKETING','SURVEY','WEB TRAFFIC'],
              'WRITING & TRANSLATION':['ARTICLES & BLOG POSTS'],
             'PROGRAMMING & TECH':['WEB PROGRAMMING','E-COMMERCE DEVELOPMENT','MOBILE APPLS','DESKTOP APPLICATIONS','DATABASES','USER TESTING']
              }
subcategoryArr = []
for key,values in categories.items():
    subcategoryArr.extend(values)

class CreateCourseForm(Form):
    course_title = StringField(validators=[DataRequired(), Length(max=80)])
    category = SelectField(validators=[DataRequired()],choices = [(categories,categories) for categories in categorykeys])
    subcategory = SelectField(validators=[DataRequired()], choices = [(subcategory,subcategory) for subcategory in subcategoryArr])
    short_description = StringField(validators=[DataRequired(),Length(max=80)])
    description = TextAreaField(validators=[DataRequired()])


class UpdateSessionForm(Form):
    session_title = StringField(validators=[DataRequired(), Length(max=30)])
    session_description = TextAreaField(validators=[])
    time_approx = IntegerField(validators=[DataRequired()])

class AddPricingForm(Form):
    hourlyrate= IntegerField(validators=[DataRequired()])
    maximumhourspersession = IntegerField(validators=[DataRequired()])
    minimumdays = IntegerField(validators=[DataRequired()])
    maximumdays = IntegerField(validators=[DataRequired()])

for subcategory in subcategoryArr:
    print(subcategory)


class RegisterInstitutionForm(Form):
    institution_name = StringField(validators=[length(min=8, max=150),DataRequired()])
    institution_address = StringField(validators=[length(min=8, max=350),DataRequired()])
    postal_code = StringField(validators=[length(min=6, max=6),DataRequired()])
    institution_email = EmailField(validators=[length(min=8, max=200), DataRequired(), email()])
    website = URLField(validators=[length(min=1, max=150),DataRequired(),url()])
    office_no = TelField(validators=[length(min=1, max=30), DataRequired()])
    admin_firstname = StringField(validators=[length(min=1, max=150),DataRequired()])
    admin_lastname = StringField(validators=[length(min=1, max=150),DataRequired()])
    admin_contact = TelField(validators=[length(min=1, max=30), validators.DataRequired()])
    admin_email = EmailField(validators=[length(min=8, max=200),DataRequired(),email()])

    #smstmst = EmailField(validators=[DataRequired()]) testing ignore this line


class socialmediaform(Form):
    smwebsite = URLField(validators=[length(min=1,max=150), DataRequired(),url()])