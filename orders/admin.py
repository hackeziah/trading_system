from django.contrib import admin
from orders.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_display = ('order_code', 'get_stock_holder', 'get_stock_name', 'order_type', 'get_total_amount', 'created_at',)
    list_per_page = 20
    list_filter = ['order_type']
    search_fields = ['order_code', 'stock__symbol']
    readonly_fields = (
        'get_stock_name', 'get_stock_holder', 'get_order_code','get_total_amount', 'created_at', 'updated_at'
    )
    def get_fieldsets(self, request, obj: Order):
        super(OrderAdmin, self).get_fields(request, obj)
        if not obj:
            return (
                ('Order Details', {
                    'fields': ('account','stock', 'order_type', 'quantity', )
                }),
            )
     
        return (
            ('Order Details', {
                'fields': ('get_order_code', 'stock', 'order_type', 
                'quantity',)
            }),
        )
    
    def get_stock_name(self, obj: Order):
        return f'{obj.stock.name}'
    get_stock_name.short_description = "Stock Name"

    def get_stock_holder(self, obj: Order):
        if not obj:
            return 'Not Yet Set'
        return f'{obj.account.get_full_name()}'
    get_stock_holder.short_description = "Stock Holder"

    def get_order_code(self, obj: Order):
        return f'{obj.order_code}'
    get_order_code.short_description = "Order Code"

    def get_total_amount(self, obj: Order):
        if not obj.total_amount:
            return f'0.00'
        return f'{obj.total_amount}'
    get_total_amount.short_description = "Total Amount"
    
