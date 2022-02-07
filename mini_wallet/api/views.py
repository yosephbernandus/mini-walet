from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import (JSONParser, MultiPartParser, FormParser)
from rest_framework.views import APIView

from .authentication import TokenAuthentication


class WalletAPIView(APIView):

    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)


class WalletAuthenticationView(WalletAPIView):

    authentication_classes = (TokenAuthentication)
