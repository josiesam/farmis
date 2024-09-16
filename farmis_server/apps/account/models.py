from django.db import models

# Create your models here.
class GenericProfile(models.Model):
    user = models.OneToOneField('auths.CustomUser', on_delete=models.CASCADE, related_name='generic_profile')
    location = models.CharField(max_length=100, null= True, blank=True)
    
    def __str__(self):
        return f"Generic Profile - {self.user.username}"
    
class FarmerProfile(models.Model):
    user = models.OneToOneField('auths.CustomUser', on_delete=models.CASCADE, related_name='farmer_profile')
    farm_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    crops_grown = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"Farmer Profile - {self.user.username}"
    
class InvestorProfile(models.Model):
    user = models.OneToOneField('auths.CustomUser', on_delete=models.CASCADE, related_name='investor_profile')
    company_name = models.CharField(max_length=100, null=True)
    investment_interests = models.TextField(null=True)
    portfolio_value = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    
    def __str__(self):
        return f"Investor Profile - {self.user.username}"

class ResearcherProfile(models.Model):
    user = models.OneToOneField('auths.CustomUser', on_delete=models.CASCADE, related_name='researcher_profile')
    research_field = models.CharField(max_length=100, null=True)
    organization = models.CharField(max_length=100, null=True)
    published_papers = models.IntegerField(default=0, null=True)
    
    def __str__(self):
        return f"Researcher Profile - {self.user.username}"
    
class ProviderProfile(models.Model):
    user = models.OneToOneField('auths.CustomUser', on_delete=models.CASCADE, related_name='provider_profile')
    research_field = models.CharField(max_length=100, null=True)
    organization = models.CharField(max_length=100, null=True)
    published_papers = models.IntegerField(default=0, null=True)
    
    def __str__(self):
        return f"Provider Profile - {self.user.username}"
    
class NGOProfile(models.Model):
    user = models.OneToOneField('auths.CustomUser', on_delete=models.CASCADE, related_name='ngo_profile')
    organization = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    location = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"NGO Profile - {self.user.username}"
    
class GovProfile(models.Model):
    user = models.OneToOneField('auths.CustomUser', on_delete=models.CASCADE, related_name='gov_profile')
    organization = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return f"Gov Profile - {self.user.username}"
