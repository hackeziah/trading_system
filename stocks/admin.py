from django.contrib import admin
from stocks.models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_display = ('symbol', 'name', 'price', 'created_at',)
    list_per_page = 20
    search_fields = ('symbol', 'name',)

    def get_fieldsets(self, request, obj=None):
        super(StockAdmin, self).get_fields(request, obj)
        return (
            ('Stock Details', {
                'fields': ('symbol', 'name',  'price',)
            }),
        )
    
    readonly_fields = ('created_at', 'updated_at')
