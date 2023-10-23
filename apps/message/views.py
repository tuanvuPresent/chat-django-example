from apps.core.base_model_view_set import BaseModelViewSet
from apps.message.models import Message
from apps.message.serializers import MessageSerializer, MessageCreateSerializer
from channels.layers import get_channel_layer


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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.validated_data.get('message')
        room = serializer.validated_data.get('room')
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
