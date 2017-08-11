from django.forms import ModelForm,Textarea
from reviews.models import Review,ImageUpload

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comment']
        widgets = {
            'comment':Textarea(attrs={'cols':40,'rows':15})
        }

class ImageUploadForm(ModelForm):
    class Meta:
        model= ImageUpload
        fields = ['name','designation','image']
