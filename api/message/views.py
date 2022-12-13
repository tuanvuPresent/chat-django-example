from api.core.base_model_view_set import BaseModelViewSet
from api.message.models import Message
from api.message.serializers import MessageSerializer, MessageCreateSerializer


class MessageModelViewSet(BaseModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().select_related('user')

    serializer_action_classes = {
        'create': MessageCreateSerializer,
        'list': MessageSerializer,
        'retrieve': MessageCreateSerializer,
        'update': MessageCreateSerializer,
        'partial_update': MessageCreateSerializer,
    }
