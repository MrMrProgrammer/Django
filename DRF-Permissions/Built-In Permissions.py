# ===========================================================
# All of built-in drf access level permissions


# AllowAny

# IsAuthenticated

# IsAuthenticatedOrReadOnly

# IsAdminUser

# DjangoModelPermissions

# DjangoModelPermissionsOrAnonReadOnly

# DjangoObjectPermissions ( by extending DjangoModelPermissions )


# ===========================================================
# Set access level permissions for FBVs (function-based views)


from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def ShwCar(request):
    cars = Car.objects.all()
    car_serializer = CarSerializer(cars, many=True)
    return Response(car_serializer.data)


# ===========================================================
# Set access level permissions for CBVs (class-based views)


from rest_framework.permissions import IsAuthenticated

class ShowView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = ((IsAuthenticated,))


# ===========================================================
# Set a default access level for all APIs


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.IsAuthenticated'    # set your access level
    ]
}


# ===========================================================