# ListDashlet

A dashlet that shows a list

## Properties
- queryset: A predefined queryset, will override model.
- model: Model form which data is coming from.
- fields: list or tuple of fields or properties to show. Default __unicode__
- order_by: Order list by.
- count: number of objects to show. Default 3.
- show_change: Show admin link to the model change_list. Default False.
- show_add: Show admin link to add a new object. Default False.

## Example
```
from responsive_dashboard.dashboard import ListDashlet
class MyDashlet(ListDashlet):
    title = 'My List'
    model = Student
    fields = ('fname', 'lname', 'calculate_gpa',)
    order_by = ('last_logged_in',)
    count = 4
```
