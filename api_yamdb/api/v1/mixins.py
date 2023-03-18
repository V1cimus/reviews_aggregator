from rest_framework import mixins, viewsets


class ListCreateDestroyGeneric(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass
