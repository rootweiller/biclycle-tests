from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView)
from bicycle.models import Bicycle
from bicycle.serializers import BicycleSerializers


class BicycleView(ListCreateAPIView):
    """
    class for add and list bicycle
    """
    model = Bicycle
    queryset = model.objects.all()
    serializer_class = BicycleSerializers

    def get_queryset(self):
        """
        List all elements in DB
        :return:
        """
        queryset = self.model.objects.all().order_by('-date_created')
        return queryset

    def filter_queryset(self, queryset):
        """
        Filter for brand or serial with Method GET
        :param queryset:
        :return:
        """
        query = {}
        if self.request.GET.get('brand'):
            query['brand'] = self.request.GET.get('brand')
        if self.request.GET.get('serial'):
            query['serial'] = self.request.GET.get('serial')

        return self.model.objects.filter(**query)


class BicycleUpdateView(UpdateAPIView):
    """
    Update view for bicycle
    """
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializers


class BicycleDestroyView(DestroyAPIView):
    """
    Delete for ID bicycle
    """
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializers
