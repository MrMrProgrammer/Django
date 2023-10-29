# ===========================================================
# Description : Django admin actions allow you to perform an "action" on an object or a group of objects.
#   An action can be used to modify an object's attributes, delete the object, copy it, and so forth.
#   Actions are primarily utilized for frequently performed "actions" or bulk changes.
#   A perfect example is activating or deactivating a ticket.
#   Suppose we have many tickets we'd like to activate.
#   It would be pretty tedious to click each of them, change their is_active property and save the model.
#   Instead, we can define an action that'll do just that.
#   Define activate_tickets and deactivate_tickets actions and add them to TicketAdmin like so:
#   @admin.action(description="Activate selected tickets")


# app/admin.py

def activate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Deactivate selected tickets")
def deactivate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=False)


class TicketAdmin(admin.ModelAdmin):
    # ...
    actions = [activate_tickets, deactivate_tickets]


# ===========================================================