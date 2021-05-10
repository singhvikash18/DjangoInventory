from customer.viewsets import EmplyoeeViewset,ItemGroupViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('emplyoee',EmplyoeeViewset)
router.register('item',ItemGroupViewset)