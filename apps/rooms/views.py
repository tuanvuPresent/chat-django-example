from apps.core.base_model_view_set import BaseModelViewSet
from apps.rooms.serializers import RoomSerializer
from apps.rooms.models import Room


class RoomModelViewSet(BaseModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
