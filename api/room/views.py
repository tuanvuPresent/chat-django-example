from api.core.base_model_view_set import BaseModelViewSet
from api.room.serializers import RoomSerializer
from api.room.models import Room


class RoomModelViewSet(BaseModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
