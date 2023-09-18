from rest_framework.serializers import ModelSerializer

from courses.serializers import PaymentSerializer
from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email']


class UserDetailSerializer(ModelSerializer):
    payments = PaymentSerializer(read_only=True, many=True, source='payment_set')

    class Meta:
        model = User
        fields = ['id', 'email', 'payments']
