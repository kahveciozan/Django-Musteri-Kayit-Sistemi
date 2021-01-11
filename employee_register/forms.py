from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','gsm','tc')

    def clean(self):
        # -----------------------------------
        tc = self.cleaned_data.get('tc')
        tc_value = str(tc)
        if not ControlClass.tcControl(tc_value):
            raise forms.ValidationError('TC Kimlik No Yanlış! Kontrol Ediniz')


        # ------------------------------------
        fullname = self.cleaned_data.get('fullname')
        fullname_value = str(fullname)
        if not ControlClass.fullnameControl(fullname_value):
            raise forms.ValidationError('Hatalı İsim Girdiniz Lütfen Kontrol Ediniz')
        #---------------------------------------
        gsm = self.cleaned_data.get('gsm')
        gsm_value = str(gsm)
        if not ControlClass.gsmControl(gsm_value):
            raise forms.ValidationError('Hatalı Telofon Numarası Girdiniz Lütfen Kontrol Ediniz')

        # --------------------------------------
        return super(EmployeeForm, self).clean()


class ControlClass():
    # -- Turkish Identity Number Control --
    def tcControl(tc_value):
            # 11 hanelidir.
            if not len(tc_value) == 11:
                return False
            # Sadece rakamlardan olusur.
            if not tc_value.isdigit():
                return False
            # Ilk hanesi 0 olamaz.
            if int(tc_value[0]) == 0:
                return False
            digits = [int(d) for d in str(tc_value)]
            # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
            # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
            if not sum(digits[:10]) % 10 == digits[10]:
                return False
            # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı
            # çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize
            # 10. haneyi verir.
            if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
                return False
            return True

    # ----- Fullname Control -----
    def fullnameControl(fullname_value):
        for c in fullname_value:
            if c.isspace()==False:
                    if c.isalpha()==False:
                        return False
        return True

    # ----- Phone Number Control  ------
    def gsmControl(gsm):
        # 10 hanelidir.
        if not len(gsm) == 10:
            return False
        # Sıfır ile baslamamali
        if  int(gsm[0]) == 0 :
            raise forms.ValidationError('Telofon Numarasının başına Sıfır Koymayınız')
            return False
        # ilk hane 5 olmali
        if not int(gsm[0]) == 5:
            return False
        return True