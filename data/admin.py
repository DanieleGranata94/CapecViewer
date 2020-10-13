from django.contrib import admin

from .models import ComprehensiveCapecDictionary
from .models import DeprecatedEntries
from .models import DetailedAbstractions
from .models import DomainsOfAttack
from .models import MechanismsOfAttack
from .models import MetaAbstractions
from .models import MobileDevicePatterns
from .models import StandardAbstractions

admin.site.register(ComprehensiveCapecDictionary)
admin.site.register(DeprecatedEntries)
admin.site.register(DetailedAbstractions)
admin.site.register(DomainsOfAttack)
admin.site.register(MechanismsOfAttack)
admin.site.register(MetaAbstractions)
admin.site.register(MobileDevicePatterns)
admin.site.register(StandardAbstractions)