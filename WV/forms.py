from django.forms import ModelForm, fields
from WV.models import Data,Options,Tags,ImageOptions
from Word2Vec import settings
from uuid import uuid4
import os.path
from django  import forms
class EnterOptions(ModelForm):
    class Meta:
        model = Options
        fields = ['size','win','minc','cbow','skipgr']
    def __str__(self):
        return self.as_div()

        # run the parent validation firs
class EnterImageOptionsForm(ModelForm):
    class Meta:
        model = ImageOptions
        fields = ['num_clusters','num_neighbors']
    def __str__(self):
        return self.as_div()

class EnterData(ModelForm):
    class Meta:
        model=Data
        fields = ['Data_title','Data_xls']
    def __str__(self):
        return self.as_div()

    def clean(self):
        def ChangeName(filename):
            ext = filename.split('.')[-1]
            # get filename
            filename = '{}.{}'.format(uuid4().hex, ext)
            return filename
        cleaned_data = self.cleaned_data
        cleaned_data['Data_xls'].name=ChangeName(filename= cleaned_data['Data_xls'].name)
        return cleaned_data
    def is_valid(self):

        valid = super(EnterData, self).is_valid()
        # we're done now if not valid
        if not valid:
            return valid


        extensions = ['.xls', '.xlsx','.xlsm','.csv','.xlt','.xltx']
        filename, file_extension = os.path.splitext(self.cleaned_data['Data_xls'].name)

        if file_extension not in extensions:

            return False

        # run the parent validation first
        else:
            return True



class TagsForm(ModelForm):

    class Meta:
        model=Tags
        fields = ['tg']

    def __str__(self):
        return self.as_div()
    def is_valid(self):

        valid = super(TagsForm, self).is_valid()
        # we're done now if not valid
        if not valid:
            return valid
        punct=['/',";","'",'.','#', ':', '!', '?','%','^','<','>','&',')','(','{','}',']','[','$','@']
        for i in self.cleaned_data['tg']:
            if i in punct:
                return False
        if not self.cleaned_data['tg']:
            return False
        # run the parent validation first
        else:
            return True
#Форма для добавления центроид
class CentroidForm(forms.Form):
    centroids= forms.CharField()
class SimilarWordForm(forms.Form):
    word= forms.CharField()
class MinFrequencyWordForm(forms.Form):
    freq= forms.IntegerField()

