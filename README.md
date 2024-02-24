
# Theo tài liệu chính thức của Django REST framework, có sáu loại mixin được hỗ trợ, là

ListModelMixin: Cung cấp phương thức list() để trả về một danh sách các đối tượng model.
CreateModelMixin: Cung cấp phương thức create() để tạo một đối tượng model mới.
RetrieveModelMixin: Cung cấp phương thức retrieve() để trả về một đối tượng model cụ thể.
UpdateModelMixin: Cung cấp phương thức update() và partial_update() để cập nhật một đối tượng model hiện có.
DestroyModelMixin: Cung cấp phương thức destroy() để xóa một đối tượng model hiện có.
GenericModelMixin: Cung cấp các thuộc tính queryset và serializer_class để xác định các đối tượng model và serializer cho view

## lookup_field

lookup_field trong django là một thuộc tính của các lớp view dựa trên GenericAPIView, dùng để xác định trường dữ liệu sẽ được sử dụng làm khóa để tìm kiếm một đối tượng model cụ thể. Mặc định, lookup_field là ‘pk’, tức là trường primary key của model. Bạn có thể thay đổi lookup_field bằng một trường khác, miễn là trường đó là duy nhất và có thể truy vấn được. Bạn cũng cần phải khớp lookup_field với tham số tương ứng trong URL conf của view.

## Theo tài liệu của REST framework1, có 11 class permission có sẵn trong REST framework, bao gồm

**AllowAny**: Cho phép truy cập cho tất cả các yêu cầu, không cần xác thực hoặc kiểm tra quyền.
**IsAuthenticated**: Yêu cầu yêu cầu phải được xác thực, nếu không sẽ từ chối truy cập.
**IsAdminUser**: Yêu cầu yêu cầu phải được xác thực và là một người dùng quản trị, nếu không sẽ từ chối truy cập.
**IsAuthenticatedOrReadOnly**: Cho phép truy cập cho các yêu cầu được xác thực, hoặc các yêu cầu chỉ đọc (GET, HEAD, OPTIONS) nếu không được xác thực.
**DjangoModelPermissions**: Sử dụng các quyền của model Django để xác định quyền truy cập. Yêu cầu yêu cầu phải được xác thực, và người dùng phải có quyền thích hợp cho các phương thức GET, POST, PUT, PATCH, DELETE.
**DjangoModelPermissionsOrAnonReadOnly**: Tương tự như DjangoModelPermissions, nhưng cho phép truy cập cho các yêu cầu chỉ đọc nếu không được xác thực.
**DjangoObjectPermissions**: Sử dụng các quyền của object Django để xác định quyền truy cập. Yêu cầu yêu cầu phải được xác thực, và người dùng phải có quyền thích hợp cho các phương thức GET, POST, PUT, PATCH, DELETE trên từng đối tượng riêng lẻ.
**DjangoObjectPermissionsOrAnonReadOnly**: Tương tự như DjangoObjectPermissions, nhưng cho phép truy cập cho các yêu cầu chỉ đọc nếu không được xác thực.
**TokenHasReadWriteScope**: Sử dụng các scope của token OAuth2 để xác định quyền truy cập. Yêu cầu yêu cầu phải được xác thực bằng token, và token phải có scope thích hợp cho các phương thức GET, POST, PUT, PATCH, DELETE.
**TokenHasScope**: Sử dụng các scope của token OAuth2 để xác định quyền truy cập. Yêu cầu yêu cầu phải được xác thực bằng token, và token phải có ít nhất một trong các scope được chỉ định.
**IsOwnerOrReadOnly**: Cho phép truy cập cho người dùng là chủ sở hữu của đối tượng, hoặc các yêu cầu chỉ đọc.

1. Django Model Instance as API Response

2. Django Model Instance to Dictionary

3. Rest Framework View & Response

4. Django Rest Framework Model Serializers

5. Ingest Data with Django Rest Framework Views

6. Django Rest Framework Generics RetrieveAPIView

7. Django Rest Framework CreateAPIView

8. Django Rest Framework ListAPIView & ListCreateAPIView

9. Using Function Based Views For Create Retrieve or List

10. UpdateAPIView & DestroyAPIView

11. Mixins and a Generic API View

12. Session Authentication & Permissions

13. User & Group Permissions with DjangoModelPermissions

14. Custom Permissions

15. Token Authentication

16. Default Django Rest Framework Settings

17. Using Mixins for Permissions

18. ViewSets & Routers
    ViewSets và routes là hai khái niệm quan trọng trong Django REST framework. Chúng cho phép bạn tạo ra các API một cách nhanh chóng và dễ dàng, bằng cách sử dụng các lớp ViewSet để định nghĩa các hành động như list, retrieve, create, update, destroy, và các hành động tùy chỉnh. Sau đó, bạn có thể sử dụng các lớp Router để tự động tạo ra các URL conf cho các ViewSet, dựa trên các quy ước chung. 12

Ví dụ, bạn có thể tạo một ViewSet cho model User như sau:
code
Python

from django.contrib.auth.models import User
from rest_framework import viewsets
from myapp.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    \"\"\"  A viewset for viewing and editing user instances.  \"\"\"
    serializer_class = UserSerializer
    queryset = User.objects.all()
code: