from rest_framework.routers import SimpleRouter

from .views import (
    PersonTypeViewSet,
    PersonMediaTypeViewSet,
    PersonMediaViewSet,
    AddUpdateViewSet,
    PersonAuditViewSet,
    PersonViewSet
    )

router = SimpleRouter()

router.register('vinculo', PersonTypeViewSet,)
router.register('tipomidia', PersonMediaTypeViewSet)
router.register('midia', PersonMediaViewSet)
router.register('status', AddUpdateViewSet)
router.register('editar', PersonAuditViewSet)
router.register('nome', PersonViewSet)
