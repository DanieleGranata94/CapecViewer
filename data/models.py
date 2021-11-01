# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import forms



class ComprehensiveCapecDictionary(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=75,db_column='Name', blank=True, null=True)
    abstraction = models.CharField(max_length=10,db_column='Abstraction', blank=True, null=True)
    status = models.CharField(max_length=10,db_column='Status', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    alternateterms = models.TextField(db_column='AlternateTerms', blank=True, null=True)
    likelihoodofattack = models.CharField(max_length=10,db_column='LikelihoodOfAttack', blank=True, null=True)
    typicalseverity = models.CharField(max_length=10,db_column='TypicalSeverity', blank=True, null=True)
    relatedattackpatterns = models.TextField(db_column='RelatedAttackPatterns', blank=True, null=True)
    executionflow = models.TextField(db_column='ExecutionFlow', blank=True, null=True)
    prerequisites = models.TextField(db_column='Prerequisites', blank=True, null=True)
    skillsrequired = models.TextField(db_column='SkillsRequired', blank=True, null=True)
    resourcesrequired = models.TextField(db_column='ResourcesRequired', blank=True, null=True)
    indicators = models.TextField(db_column='Indicators', blank=True, null=True)
    consequences = models.TextField(db_column='Consequences', blank=True, null=True)
    mitigations = models.TextField(db_column='Mitigations', blank=True, null=True)
    exampleinstances = models.TextField(db_column='ExampleInstances', blank=True, null=True)
    relatedweaknesses = models.TextField(db_column='RelatedWeaknesses', blank=True, null=True)
    taxonomymappings = models.TextField(db_column='TaxonomyMappings', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)
        
    def __str__(self):
        return '%s (%s)' % (self.name, str(self.id))
        
    class Meta:
        managed = False
        db_table = 'Comprehensive CAPEC Dictionary'
        verbose_name_plural = 'Comprehensive CAPEC Dictionary'


class DeprecatedEntries(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=200,db_column='Name', blank=True, null=True)
    abstraction = models.CharField(max_length=10,db_column='Abstraction', blank=True, null=True)
    status = models.CharField(max_length=10,db_column='Status', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    alternateterms = models.TextField(db_column='AlternateTerms', blank=True, null=True)
    likelihoodofattack = models.CharField(max_length=10,db_column='LikelihoodOfAttack', blank=True, null=True)
    typicalseverity = models.CharField(max_length=10,db_column='TypicalSeverity', blank=True, null=True)
    relatedattackpatterns = models.TextField(db_column='RelatedAttackPatterns', blank=True, null=True)
    executionflow = models.TextField(db_column='ExecutionFlow', blank=True, null=True)
    prerequisites = models.TextField(db_column='Prerequisites', blank=True, null=True)
    skillsrequired = models.TextField(db_column='SkillsRequired', blank=True, null=True)
    resourcesrequired = models.TextField(db_column='ResourcesRequired', blank=True, null=True)
    indicators = models.TextField(db_column='Indicators', blank=True, null=True)
    consequences = models.TextField(db_column='Consequences', blank=True, null=True)
    mitigations = models.TextField(db_column='Mitigations', blank=True, null=True)
    exampleinstances = models.TextField(db_column='ExampleInstances', blank=True, null=True)
    relatedweaknesses = models.TextField(db_column='RelatedWeaknesses', blank=True, null=True)
    taxonomymappings = models.TextField(db_column='TaxonomyMappings', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)
    
    def __str__(self):
        return '%s (%s)' % (self.name, str(self.id))
        
    class Meta:
        managed = False
        db_table = 'Deprecated Entries'
        verbose_name_plural = 'Deprecated Entries'


class DetailedAbstractions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=200,db_column='Name', blank=True, null=True)
    abstraction = models.CharField(max_length=10,db_column='Abstraction', blank=True, null=True)
    status = models.CharField(max_length=10,db_column='Status', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    alternateterms = models.TextField(db_column='AlternateTerms', blank=True, null=True)
    likelihoodofattack = models.CharField(max_length=10,db_column='LikelihoodOfAttack', blank=True, null=True)
    typicalseverity = models.CharField(max_length=10,db_column='TypicalSeverity', blank=True, null=True)
    relatedattackpatterns = models.TextField(db_column='RelatedAttackPatterns', blank=True, null=True)
    executionflow = models.TextField(db_column='ExecutionFlow', blank=True, null=True)
    prerequisites = models.TextField(db_column='Prerequisites', blank=True, null=True)
    skillsrequired = models.TextField(db_column='SkillsRequired', blank=True, null=True)
    resourcesrequired = models.TextField(db_column='ResourcesRequired', blank=True, null=True)
    indicators = models.TextField(db_column='Indicators', blank=True, null=True)
    consequences = models.TextField(db_column='Consequences', blank=True, null=True)
    mitigations = models.TextField(db_column='Mitigations', blank=True, null=True)
    exampleinstances = models.TextField(db_column='ExampleInstances', blank=True, null=True)
    relatedweaknesses = models.TextField(db_column='RelatedWeaknesses', blank=True, null=True)
    taxonomymappings = models.TextField(db_column='TaxonomyMappings', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)

    def __str__(self):
        return '%s (%s)' % (self.name, str(self.id))
        
    class Meta:
        managed = False
        db_table = 'Detailed Abstractions'
        verbose_name_plural = 'Detailed Abstractions'


class DomainsOfAttack(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=200,db_column='Name', blank=True, null=True)
    abstraction = models.CharField(max_length=10,db_column='Abstraction', blank=True, null=True)
    status = models.CharField(max_length=10,db_column='Status', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    alternateterms = models.TextField(db_column='AlternateTerms', blank=True, null=True)
    likelihoodofattack = models.CharField(max_length=10,db_column='LikelihoodOfAttack', blank=True, null=True)
    typicalseverity = models.CharField(max_length=10,db_column='TypicalSeverity', blank=True, null=True)
    relatedattackpatterns = models.TextField(db_column='RelatedAttackPatterns', blank=True, null=True)
    executionflow = models.TextField(db_column='ExecutionFlow', blank=True, null=True)
    prerequisites = models.TextField(db_column='Prerequisites', blank=True, null=True)
    skillsrequired = models.TextField(db_column='SkillsRequired', blank=True, null=True)
    resourcesrequired = models.TextField(db_column='ResourcesRequired', blank=True, null=True)
    indicators = models.TextField(db_column='Indicators', blank=True, null=True)
    consequences = models.TextField(db_column='Consequences', blank=True, null=True)
    mitigations = models.TextField(db_column='Mitigations', blank=True, null=True)
    exampleinstances = models.TextField(db_column='ExampleInstances', blank=True, null=True)
    relatedweaknesses = models.TextField(db_column='RelatedWeaknesses', blank=True, null=True)
    taxonomymappings = models.TextField(db_column='TaxonomyMappings', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)

    def __str__(self):
        return '%s (%s)' % (self.name, str(self.id))
    
            
    class Meta:
        managed = False
        db_table = 'Domains of Attack'
        verbose_name_plural = 'Domains of Attack'
        
    
    
    

class MechanismsOfAttack(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=200,db_column='Name', blank=True, null=True)
    abstraction = models.CharField(max_length=10,db_column='Abstraction', blank=True, null=True)
    status = models.CharField(max_length=10,db_column='Status', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    alternateterms = models.TextField(db_column='AlternateTerms', blank=True, null=True)
    likelihoodofattack = models.CharField(max_length=10,db_column='LikelihoodOfAttack', blank=True, null=True)
    typicalseverity = models.CharField(max_length=10,db_column='TypicalSeverity', blank=True, null=True)
    relatedattackpatterns = models.TextField(db_column='RelatedAttackPatterns', blank=True, null=True)
    executionflow = models.TextField(db_column='ExecutionFlow', blank=True, null=True)
    prerequisites = models.TextField(db_column='Prerequisites', blank=True, null=True)
    skillsrequired = models.TextField(db_column='SkillsRequired', blank=True, null=True)
    resourcesrequired = models.TextField(db_column='ResourcesRequired', blank=True, null=True)
    indicators = models.TextField(db_column='Indicators', blank=True, null=True)
    consequences = models.TextField(db_column='Consequences', blank=True, null=True)
    mitigations = models.TextField(db_column='Mitigations', blank=True, null=True)
    exampleinstances = models.TextField(db_column='ExampleInstances', blank=True, null=True)
    relatedweaknesses = models.TextField(db_column='RelatedWeaknesses', blank=True, null=True)
    taxonomymappings = models.TextField(db_column='TaxonomyMappings', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)

    def __str__(self):
        return '%s (%s)' % (self.name, str(self.id))
        
    class Meta:
        managed = False
        db_table = 'Mechanisms of Attack'
        verbose_name_plural = 'Mechanisms of Attack'


class MetaAbstractions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=200,db_column='Name', blank=True, null=True)
    abstraction = models.CharField(max_length=10,db_column='Abstraction', blank=True, null=True)
    status = models.CharField(max_length=10,db_column='Status', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    alternateterms = models.TextField(db_column='AlternateTerms', blank=True, null=True)
    likelihoodofattack = models.CharField(max_length=10,db_column='LikelihoodOfAttack', blank=True, null=True)
    typicalseverity = models.CharField(max_length=10,db_column='TypicalSeverity', blank=True, null=True)
    relatedattackpatterns = models.TextField(db_column='RelatedAttackPatterns', blank=True, null=True)
    executionflow = models.TextField(db_column='ExecutionFlow', blank=True, null=True)
    prerequisites = models.TextField(db_column='Prerequisites', blank=True, null=True)
    skillsrequired = models.TextField(db_column='SkillsRequired', blank=True, null=True)
    resourcesrequired = models.TextField(db_column='ResourcesRequired', blank=True, null=True)
    indicators = models.TextField(db_column='Indicators', blank=True, null=True)
    consequences = models.TextField(db_column='Consequences', blank=True, null=True)
    mitigations = models.TextField(db_column='Mitigations', blank=True, null=True)
    exampleinstances = models.TextField(db_column='ExampleInstances', blank=True, null=True)
    relatedweaknesses = models.TextField(db_column='RelatedWeaknesses', blank=True, null=True)
    taxonomymappings = models.TextField(db_column='TaxonomyMappings', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)
    #option = forms.BooleanField(db_column='Option', blank=True, null=True)

    def __str__(self):
        return '%s (%s)' % (self.name, str(self.id))
        
    class Meta:
        managed = False
        db_table = 'Meta Abstractions'
        verbose_name_plural = 'Meta Abstractions'

class form(forms.Form):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=200,db_column='Name', blank=True, null=True)
    abstraction = models.CharField(max_length=10,db_column='Abstraction', blank=True, null=True)
    status = models.CharField(max_length=10,db_column='Status', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    alternateterms = models.TextField(db_column='AlternateTerms', blank=True, null=True)
    likelihoodofattack = models.CharField(max_length=10,db_column='LikelihoodOfAttack', blank=True, null=True)
    typicalseverity = models.CharField(max_length=10,db_column='TypicalSeverity', blank=True, null=True)
    relatedattackpatterns = models.TextField(db_column='RelatedAttackPatterns', blank=True, null=True)
    executionflow = models.TextField(db_column='ExecutionFlow', blank=True, null=True)
    prerequisites = models.TextField(db_column='Prerequisites', blank=True, null=True)
    skillsrequired = models.TextField(db_column='SkillsRequired', blank=True, null=True)
    resourcesrequired = models.TextField(db_column='ResourcesRequired', blank=True, null=True)
    indicators = models.TextField(db_column='Indicators', blank=True, null=True)
    consequences = models.TextField(db_column='Consequences', blank=True, null=True)
    mitigations = models.TextField(db_column='Mitigations', blank=True, null=True)
    exampleinstances = models.TextField(db_column='ExampleInstances', blank=True, null=True)
    relatedweaknesses = models.TextField(db_column='RelatedWeaknesses', blank=True, null=True)
    taxonomymappings = models.TextField(db_column='TaxonomyMappings', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)


class MobileDevicePatterns(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=200,db_column='Name', blank=True, null=True)
    abstraction = models.CharField(max_length=10,db_column='Abstraction', blank=True, null=True)
    status = models.CharField(max_length=10,db_column='Status', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    alternateterms = models.TextField(db_column='AlternateTerms', blank=True, null=True)
    likelihoodofattack = models.CharField(max_length=10,db_column='LikelihoodOfAttack', blank=True, null=True)
    typicalseverity = models.CharField(max_length=10,db_column='TypicalSeverity', blank=True, null=True)
    relatedattackpatterns = models.TextField(db_column='RelatedAttackPatterns', blank=True, null=True)
    executionflow = models.TextField(db_column='ExecutionFlow', blank=True, null=True)
    prerequisites = models.TextField(db_column='Prerequisites', blank=True, null=True)
    skillsrequired = models.TextField(db_column='SkillsRequired', blank=True, null=True)
    resourcesrequired = models.TextField(db_column='ResourcesRequired', blank=True, null=True)
    indicators = models.TextField(db_column='Indicators', blank=True, null=True)
    consequences = models.TextField(db_column='Consequences', blank=True, null=True)
    mitigations = models.TextField(db_column='Mitigations', blank=True, null=True)
    exampleinstances = models.TextField(db_column='ExampleInstances', blank=True, null=True)
    relatedweaknesses = models.TextField(db_column='RelatedWeaknesses', blank=True, null=True)
    taxonomymappings = models.TextField(db_column='TaxonomyMappings', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)

    def __str__(self):
        return '%s (%s)' % (self.name, str(self.id))
        
    class Meta:
        managed = False
        db_table = 'Mobile Device Patterns'
        verbose_name_plural = 'Mobile Device Patterns'


class StandardAbstractions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=200,db_column='Name', blank=True, null=True)
    abstraction = models.CharField(max_length=10,db_column='Abstraction', blank=True, null=True)
    status = models.CharField(max_length=10,db_column='Status', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    alternateterms = models.TextField(db_column='AlternateTerms', blank=True, null=True)
    likelihoodofattack = models.CharField(max_length=10,db_column='LikelihoodOfAttack', blank=True, null=True)
    typicalseverity = models.CharField(max_length=10,db_column='TypicalSeverity', blank=True, null=True)
    relatedattackpatterns = models.TextField(db_column='RelatedAttackPatterns', blank=True, null=True)
    executionflow = models.TextField(db_column='ExecutionFlow', blank=True, null=True)
    prerequisites = models.TextField(db_column='Prerequisites', blank=True, null=True)
    skillsrequired = models.TextField(db_column='SkillsRequired', blank=True, null=True)
    resourcesrequired = models.TextField(db_column='ResourcesRequired', blank=True, null=True)
    indicators = models.TextField(db_column='Indicators', blank=True, null=True)
    consequences = models.TextField(db_column='Consequences', blank=True, null=True)
    mitigations = models.TextField(db_column='Mitigations', blank=True, null=True)
    exampleinstances = models.TextField(db_column='ExampleInstances', blank=True, null=True)
    relatedweaknesses = models.TextField(db_column='RelatedWeaknesses', blank=True, null=True)
    taxonomymappings = models.TextField(db_column='TaxonomyMappings', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)

    def __str__(self):
        return '%s (%s)' % (self.name, str(self.id))
        
    class Meta:
        managed = False
        db_table = 'Standard Abstractions'
        verbose_name_plural = 'Standard Abstractions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
