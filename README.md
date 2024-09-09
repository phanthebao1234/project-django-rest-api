
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

Python

```c
from django.contrib.auth.models import User
from rest_framework import viewsets
from myapp.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    \"\"\"  A viewset for viewing and editing user instances.  \"\"\"
    serializer_class = UserSerializer
    queryset = User.objects.all()
```

Viewset và mixxin trong Django là hai khái niệm liên quan đến việc tạo ra các API một cách hiệu quả và linh hoạt. 1

Viewset là một lớp dựa trên View, nhưng không cung cấp các phương thức xử lý như .get() hay .post(), mà cung cấp các hành động như .list(), .retrieve(), .create(), .update(), .destroy(), và các hành động tùy chỉnh. Viewset cho phép bạn kết hợp logic cho một tập hợp các view liên quan trong một lớp duy nhất, thay vì phải viết nhiều lớp view riêng biệt cho mỗi hành động. Viewset cũng cho phép bạn sử dụng các Router để tự động tạo ra các URL conf cho các viewset, dựa trên các quy ước chung. 2
Mixxin là một lớp cung cấp các hành động cho các view, nhưng không phải là một view đầy đủ. Mixxin cho phép bạn tái sử dụng code cho các hành động phổ biến, như list, create, update, destroy, và các hành động khác. Bạn có thể kết hợp nhiều mixxin với nhau để tạo ra các view tùy biến, hoặc sử dụng các mixxin có sẵn trong Django REST framework, như ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, và các mixxin khác. 3
Ví dụ, bạn có thể tạo một viewset cho model User bằng cách kế thừa từ ModelViewSet, một lớp viewset có sẵn trong Django REST framework, như sau:

Python

```c
from django.contrib.auth.models import User
from rest_framework import viewsets
from myapp.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    \"\"\"  A viewset for viewing and editing user instances.  \"\"\"
    serializer_class = UserSerializer
    queryset = User.objects.all()
```

Đoạn code trên sẽ cung cấp cho bạn các hành động mặc định cho việc xem và chỉnh sửa các user. Bạn không cần phải viết các lớp view riêng biệt cho mỗi hành động. Sau đó, bạn có thể đăng ký viewset này với một router như sau:

Python

```c
from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls
```

Đoạn code trên sẽ tạo ra các URL conf cho các hành động của UserViewSet, ví dụ:

/users/ : hành động list và create
/users/{pk}/ : hành động retrieve, update, và destroy
/users/{pk}/highlight/ : hành động tùy chỉnh highlight (nếu có)
Nếu bạn muốn tạo một view tùy biệt cho model User, bạn có thể kế thừa từ GenericAPIView và các mixxin thích hợp, như sau:

Python

```c
from django.contrib.auth.models import User
from rest_framework import generics, mixins
from myapp.serializers import UserSerializer

class UserList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    \"\"\"  A view for listing and creating user instances.  \"\"\"
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

Đoạn code trên sẽ cung cấp cho bạn hai hành động list và create cho model User, bằng cách kế thừa từ các mixxin ListModelMixin và CreateModelMixin. Bạn cũng cần phải định nghĩa các phương thức xử lý cho các hành động này, bằng cách gọi các hành động tương ứng từ các mixxin. Sau đó, bạn có thể đăng ký view này với một URL conf như sau:

Python

```c
from django.urls import path
from myapp.views import UserList

urlpatterns = [
    path('users/', UserList.as_view()),
]
AI-generated code. Review and use carefully. More info on FAQ.
Đoạn code trên sẽ tạo ra một URL conf cho view UserList, là /users/.
```

19. URLs, Reverse, & Serializers

URLs là cách để định nghĩa các đường dẫn cho các view của API, bằng cách sử dụng các biểu thức chính quy (regex) hoặc các router. URLs cho phép bạn ánh xạ các yêu cầu HTTP đến các hàm xử lý tương ứng, và truyền các tham số từ đường dẫn vào các hàm đó. Ví dụ, bạn có thể định nghĩa một URL như sau:
Python

from django.urls import path
from myapp.views import UserList

urlpatterns = [
    path('users/', UserList.as_view()),
]
AI-generated code. Review and use carefully. More info on FAQ.
Đoạn code trên sẽ ánh xạ các yêu cầu GET hoặc POST đến đường dẫn /users/ đến hàm UserList.as_view(), một lớp view dựa trên GenericAPIView. 2

Reverse là một hàm để tạo ra các URL từ tên của các view, bằng cách sử dụng các tham số truyền vào. Reverse cho phép bạn trả về các URL tuyệt đối từ API của bạn, thay vì các URL tương đối, để tăng tính rõ ràng và tiện lợi cho người dùng. Ví dụ, bạn có thể tạo một URL cho view UserDetail như sau:
Python

from rest_framework.reverse import reverse

url = reverse('user-detail', args=[1])

# url = '<http://example.com/users/1/>'

Đoạn code trên sẽ tạo ra một URL tuyệt đối cho view UserDetail với tham số là 1, tức là user có id là 1. Bạn cần truyền vào request như một tham số từ khóa cho hàm reverse, để nó có thể xác định host và port. 3

Serializers là một lớp để chuyển đổi các dữ liệu phức tạp như các model hoặc các queryset thành các dữ liệu đơn giản như các kiểu dữ liệu Python, để có thể hiển thị dưới dạng JSON, XML, hoặc các định dạng khác. Serializers cũng cho phép bạn chuyển đổi các dữ liệu đã phân tích cú pháp từ các yêu cầu HTTP thành các đối tượng phức tạp, sau khi xác thực các dữ liệu đó. Ví dụ, bạn có thể tạo một serializer cho model User như sau:
Python

```c

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
```

Đoạn code trên sẽ tạo ra một serializer dựa trên ModelSerializer, một lớp serializer có sẵn trong Django REST framework, để chuyển đổi các đối tượng User thành các dữ liệu JSON, và ngược lại. Bạn cũng có thể tùy chỉnh các trường, các kiểu dữ liệu, các quy tắc xác thực, và các phương thức tạo và cập nhật cho serializer.

20. Model Serializer Create & Update Methods

Model serializer là một loại serializer cho phép bạn chuyển đổi dữ liệu phức tạp như các queryset và model instance thành các kiểu dữ liệu Python có thể được hiển thị dễ dàng thành JSON, XML hoặc các loại nội dung khác. Model serializer cũng cung cấp chức năng deserialization, cho phép dữ liệu đã được phân tích được chuyển đổi trở lại thành các kiểu dữ liệu phức tạp, sau khi xác thực dữ liệu đầu vào. 1

Để tạo và cập nhật các model instance bằng model serializer, bạn cần thực hiện một hoặc cả hai phương thức .create() và .update(). Phương thức .create() sẽ được gọi khi bạn tạo một serializer mới với dữ liệu đầu vào và gọi phương thức .save(). Phương thức .update() sẽ được gọi khi bạn tạo một serializer với một model instance hiện có và dữ liệu đầu vào và gọi phương thức .save(). 2

Ví dụ, bạn có một model User như sau:

Python

```c
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
```

Bạn có thể tạo một model serializer cho model User như sau:

Python

```c
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Tạo một model instance mới từ dữ liệu đã được xác thực
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Trả về model instance mới
        return user

    def update(self, instance, validated_data):
        # Cập nhật các thuộc tính của model instance hiện có từ dữ liệu đã được xác thực
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        # Lưu và trả về model instance đã được cập nhật
        instance.save()
        return instance
```

Bạn có thể sử dụng model serializer này để tạo và cập nhật các model instance bằng cách gọi phương thức .save() trên serializer. Ví dụ:

Python

```c
Tạo một model instance mới từ dữ liệu đầu vào
data = {'username': 'alice', 'email': 'alice@example.com', 'password': '123456'}
serializer = UserSerializer(data=data)
if serializer.is_valid():
    user = serializer.save()
    print(user.username, user.email, user.password)
# alice alice@example.com 123456

# Cập nhật một model instance hiện có từ dữ liệu đầu vào
user = User.objects.get(username='alice')
data = {'email': 'alice@gmail.com', 'password': '654321'}
serializer = UserSerializer(user, data=data, partial=True)
if serializer.is_valid():
    user = serializer.save()
    print(user.username, user.email, user.password)
```

21. Custom Validation with Serializers

22. Request User Data & Customize View Queryset

23. Related Fields & Foreign Key Serializer trong django rest framework

Bạn đã hỏi về Related Fields & Foreign Key Serializer trong django rest framework. Đây là một chủ đề rất thú vị và quan trọng trong việc xây dựng các API dựa trên mô hình dữ liệu quan hệ. Tôi sẽ cố gắng giải thích cho bạn một cách ngắn gọn và dễ hiểu.

Related Fields là các trường được sử dụng để biểu diễn các mối quan hệ giữa các mô hình trong django rest framework. Chúng có thể áp dụng cho các trường ForeignKey, ManyToManyField và OneToOneField, cũng như các mối quan hệ ngược và tùy chỉnh như GenericForeignKey1.

Foreign Key Serializer là một loại serializer được sử dụng để tuân thủ các quy tắc chuẩn hóa dữ liệu khi có các mối quan hệ nhiều đến nhiều hoặc một đến nhiều giữa các mô hình2. Foreign Key Serializer cho phép bạn lấy giá trị của trường liên quan từ mô hình khác thông qua thuộc tính source3.

Ví dụ, giả sử bạn có hai mô hình sau:

Python

```c
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='items')

    def __unicode__(self):
        return self.name
```

Bạn muốn tạo một serializer cho mô hình Item, và bạn muốn hiển thị tên của category mà item thuộc về. Bạn có thể sử dụng một Related Field như sau:

Python

```c
class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Item
        fields = ('id', 'name', 'category_name')
```

Kết quả sẽ như sau:

JSON

```c
[
    {
        "id": 1,
        "name": "Item 1",
        "category_name": "Cat 1"
    },
    {
        "id": 2,
        "name": "Item 2",
        "category_name": "Cat 1"
    },
    {
        "id": 3,
        "name": "Item 3",
        "category_name": "Cat 2"
    }
]
```

24. Pagination 

Pagination là một tính năng của Django REST framework cho phép bạn chia một tập kết quả lớn thành nhiều trang nhỏ hơn, với các liên kết “Trước/Sau”. Điều này giúp bạn quản lý dữ liệu một cách hiệu quả hơn, cải thiện thời gian tải và trải nghiệm người dùng của ứng dụng của bạn.

Django REST framework hỗ trợ một số phong cách phân trang khác nhau, bao gồm:

PageNumberPagination: Phân trang kết quả bằng số trang. Phong cách này cho phép bạn nhảy đến các trang cụ thể một cách dễ dàng.
LimitOffsetPagination: Phân trang kết quả bằng giới hạn và độ lệch. Phong cách này mô phỏng cách tìm kiếm nhiều bản ghi trong cơ sở dữ liệu. Khách hàng cho máy chủ biết hai điều: Số lượng bản ghi tối đa để trả về cho mỗi trang (limit) và vị trí bắt đầu trong danh sách bản ghi (offset).
CursorPagination: Cung cấp phân trang bằng cách sử dụng con trỏ di chuyển. Phong cách này cung cấp một cách phân trang hiệu quả và nhất quán cho các tập kết quả lớn và động.
Bạn có thể thiết lập phong cách phân trang toàn cục, bằng cách sử dụng các khóa cài đặt DEFAULT_PAGINATION_CLASS và PAGE_SIZE. Ví dụ, để sử dụng phong cách phân trang theo giới hạn/độ lệch, bạn có thể làm như sau:

Python

```c
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
```

Bạn cũng có thể thiết lập phong cách phân trang cho một view riêng lẻ, bằng cách sử dụng thuộc tính pagination_class. Thông thường, bạn sẽ muốn sử dụng cùng một phong cách phân trang cho toàn bộ API của bạn, mặc dù bạn có thể muốn thay đổi một số khía cạnh của phong cách phân trang, như kích thước trang mặc định hoặc tối đa, trên mỗi view.
