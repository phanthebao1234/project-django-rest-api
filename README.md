
# Theo tài liệu chính thức của Django REST framework, có sáu loại mixin được hỗ trợ, là

ListModelMixin: Cung cấp phương thức list() để trả về một danh sách các đối tượng model.<br> \
CreateModelMixin: Cung cấp phương thức create() để tạo một đối tượng model mới.<br> \
RetrieveModelMixin: Cung cấp phương thức retrieve() để trả về một đối tượng model cụ thể.<br> \
UpdateModelMixin: Cung cấp phương thức update() và partial_update() để cập nhật một đối tượng model hiện có. <br> \
DestroyModelMixin: Cung cấp phương thức destroy() để xóa một đối tượng model hiện có.<br> \
GenericModelMixin: Cung cấp các thuộc tính queryset và serializer_class để xác định các đối tượng model và serializer cho view.
<br><br>
## lookup_field

lookup_field trong django là một thuộc tính của các lớp view dựa trên GenericAPIView, dùng để xác định trường dữ liệu sẽ được sử dụng làm khóa để tìm kiếm một đối tượng model cụ thể. Mặc định, lookup_field là ‘pk’, tức là trường primary key của model. Bạn có thể thay đổi lookup_field bằng một trường khác, miễn là trường đó là duy nhất và có thể truy vấn được. Bạn cũng cần phải khớp lookup_field với tham số tương ứng trong URL conf của view.

## Theo tài liệu của REST framework1, có 11 class permission có sẵn trong REST framework, bao gồm

**AllowAny**: Cho phép truy cập cho tất cả các yêu cầu, không cần xác thực hoặc kiểm tra quyền.<br> \
**IsAuthenticated**: Yêu cầu yêu cầu phải được xác thực, nếu không sẽ từ chối truy cập.<br> \
**IsAdminUser**: Yêu cầu yêu cầu phải được xác thực và là một người dùng quản trị, nếu không sẽ từ chối truy cập.<br> \
**IsAuthenticatedOrReadOnly**: Cho phép truy cập cho các yêu cầu được xác thực, hoặc các yêu cầu chỉ đọc (GET, HEAD, OPTIONS) nếu không được xác thực.<br> \
**DjangoModelPermissions**: Sử dụng các quyền của model Django để xác định quyền truy cập. Yêu cầu yêu cầu phải được xác thực, và người dùng phải có quyền thích hợp cho các phương thức GET, POST, PUT, PATCH, DELETE.<br> \
**DjangoModelPermissionsOrAnonReadOnly**: Tương tự như DjangoModelPermissions, nhưng cho phép truy cập cho các yêu cầu chỉ đọc nếu không được xác thực.<br> \
**DjangoObjectPermissions**: Sử dụng các quyền của object Django để xác định quyền truy cập. Yêu cầu yêu cầu phải được xác thực, và người dùng phải có quyền thích hợp cho các phương thức GET, POST, PUT, PATCH, DELETE trên từng đối tượng riêng lẻ.<br> \
**DjangoObjectPermissionsOrAnonReadOnly**: Tương tự như DjangoObjectPermissions, nhưng cho phép truy cập cho các yêu cầu chỉ đọc nếu không được xác thực.<br> \
**TokenHasReadWriteScope**: Sử dụng các scope của token OAuth2 để xác định quyền truy cập. Yêu cầu yêu cầu phải được xác thực bằng token, và token phải có scope thích hợp cho các phương thức GET, POST, PUT, PATCH, DELETE.<br> \
**TokenHasScope**: Sử dụng các scope của token OAuth2 để xác định quyền truy cập. Yêu cầu yêu cầu phải được xác thực bằng token, và token phải có ít nhất một trong các scope được chỉ định.<br> \
**IsOwnerOrReadOnly**: Cho phép truy cập cho người dùng là chủ sở hữu của đối tượng, hoặc các yêu cầu chỉ đọc.
<br>
<br>
1. <h3><ins>Django Model Instance as API Response</ins></h3>

Trong Django, để trả về một instance của model dưới dạng API response, bạn thường sử dụng Django REST framework (DRF). Đây là một cách để chuyển đổi dữ liệu phức tạp từ các instance của model Django thành các định dạng dễ sử dụng như JSON, XML, v.v.\
Cài đặt Django REST framework:
``` pip install djangorestframework ``` \
Thêm DRF vào INSTALLED_APPS trong settings.py
```c
INSTALLED_APPS = [
    ...
    'rest_framework',
]

```
Tạo Serializer: Serializer giúp chuyển đổi dữ liệu từ model Django thành các định dạng như JSON.
```c
    from rest_framework import serializers
    from .models import YourModel
    
    class YourModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = YourModel
            fields = '__all__'
```
Tạo View: Sử dụng APIView hoặc @api_view để tạo view trả về dữ liệu đã được serialize.
```c
    from rest_framework.response import Response
    from rest_framework.decorators import api_view
    from .models import YourModel
    from .serializers import YourModelSerializer
    
    @api_view(['GET'])
    def your_model_detail(request, pk):
        try:
            instance = YourModel.objects.get(pk=pk)
        except YourModel.DoesNotExist:
            return Response(status=404)
        
        serializer = YourModelSerializer(instance)
        return Response(serializer.data)
```
Cấu hình URLs: Liên kết view với một URL trong urls.py.
```c
    from django.urls import path
    from .views import your_model_detail
    
    urlpatterns = [
        path('yourmodel/<int:pk>/', your_model_detail, name='your_model_detail'),
    ]
```
Với cấu hình này, bạn có thể lấy một instance của model và trả về nó dưới dạng JSON thông qua một endpoint API.

<br>
<br>
2. <h3><ins>Django Model Instance to Dictionary</ins></h3>

Trong Django, việc chuyển đổi một instance của model thành dictionary có thể hữu ích cho nhiều mục đích như debug, serialization, hoặc gửi dữ liệu đến client. Có một số cách để thực hiện điều này:
Sử dụng model_to_dict từ django.forms.models \
Django cung cấp hàm model_to_dict trong module django.forms.models, giúp chuyển đổi một instance của model thành dictionary. Đây là cách đơn giản và phổ biến nhất:
```c
from django.forms.models import model_to_dict
from .models import YourModel

instance = YourModel.objects.get(pk=1)
data = model_to_dict(instance)
print(data)
```
Sử dụng thuộc tính <strong>__dict__</strong>\
Bạn cũng có thể sử dụng thuộc tính __dict__ của instance, nhưng cách này sẽ bao gồm cả các thuộc tính nội bộ của Django:
```c
instance = YourModel.objects.get(pk=1)
data = instance.__dict__
print(data)
```
Để loại bỏ các thuộc tính nội bộ, bạn có thể lọc lại dictionary:
```c
data = {key: value for key, value in instance.__dict__.items() if not key.startswith('_')}
print(data)
```
Sử dụng phương thức <strong>values()</strong>\
Nếu bạn chỉ cần các giá trị của các trường cụ thể, bạn có thể sử dụng phương thức values():
```c
data = YourModel.objects.filter(pk=1).values().first()
print(data)
```
Lợi ích và hạn chế\
Lợi ích: Dictionaries dễ sử dụng, linh hoạt và hiệu quả trong việc truy cập dữ liệu.\
Hạn chế: Dictionaries không bảo mật và không tối ưu như models, có thể ảnh hưởng đến hiệu suất của ứng dụng123.
<br>
<br>
3. <h3><ins>Rest Framework View & Response</ins></h3>

Trong phát triển ứng dụng với Django REST Framework (DRF), hai khái niệm quan trọng là <strong>View</strong> và <strong>Response</strong>. Đây là những thành phần cốt lõi giúp xây dựng và quản lý các API.\
View trong Django REST Framework. \
<strong>View</strong> là nơi xử lý các yêu cầu HTTP và trả về các phản hồi tương ứng. DRF cung cấp nhiều loại view để bạn có thể dễ dàng xây dựng API:
<strong>Function-Based Views (FBV)</strong>: Sử dụng các hàm để xử lý yêu cầu.
```
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def example_view(request):
    data = {"message": "Hello, world!"}
    return Response(data)
```
<br>
<strong>Class-Based Views (CBV)</strong>: Sử dụng các lớp để xử lý yêu cầu, giúp mã nguồn dễ bảo trì và mở rộng.

```
from rest_framework.views import APIView
from rest_framework.response import Response
class ExampleView(APIView):
    def get(self, request):
        data = {"message": "Hello, world!"}
        return Response(data)
```
<br>
<strong>Generic Views</strong>: DRF cung cấp các generic views để thực hiện các thao tác CRUD một cách tự động.

```
from rest_framework import generics
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelListCreate(generics.ListCreateAPIView):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
```
<br>
<strong>Response trong Django REST Framework</strong><br>
<strong>Response là đối tượng được trả về từ các view để gửi dữ liệu đến client. DRF cung cấp lớp `Response` để dễ dàng tạo các phản hồi HTTP với dữ liệu đã được serialize.</strong>
<br>
Tạo Response: Bạn có thể tạo một response đơn giản bằng cách sử dụng lớp Response

```
from rest_framework.response import Response

def example_view(request):
    data = {"message": "Hello, world!"}
    return Response(data)
```
Xử lý lỗi: DRF cũng cung cấp các công cụ để xử lý lỗi và trả về các mã trạng thái HTTP phù hợp. 
```
from rest_framework.exceptions import NotFound

def example_view(request):
    if some_condition_not_met:
        raise NotFound("Resource not found")
    data = {"message": "Hello, world!"}
    return Response(data)

```
<br>
<strong>Lợi ích của việc sử dụng View và Response trong DRF</strong> <br> 
<strong>Tính linh hoạt:</strong> DRF cho phép bạn dễ dàng tùy chỉnh và mở rộng các view và response theo nhu cầu của ứng dụng.<br> 
<strong>Quản lý lỗi tốt:</strong> DRF cung cấp các công cụ mạnh mẽ để xử lý và quản lý lỗi, giúp API của bạn trở nên đáng tin cậy hơn. <br>
<strong>Tích hợp dễ dàng:</strong> DRF tích hợp tốt với các thành phần khác của Django, giúp bạn xây dựng các ứng dụng web một cách hiệu quả. 
<br>
<br>
4.<h3>><ins>Django Rest Framework Model Serializers</ins></h3>

Model Serializers trong Django REST Framework (DRF) là một tính năng mạnh mẽ giúp đơn giản hóa quá trình chuyển đổi (serialize) và khôi phục (deserialize) các đối tượng model của Django sang và từ định dạng JSON. <br> <br> 
<strong>Một số điểm nổi bật của Model Serializers:</strong> <br>  
    &emsp;&bull;&nbsp;Chuyển đổi dữ liệu phức tạp: Model Serializers cho phép chuyển đổi các dữ liệu phức tạp như queryset và các instance của model thành các kiểu dữ liệu Python nguyên thủy, sau đó có thể dễ dàng render thành JSON, XML hoặc các loại nội dung khác. <br> 
    &emsp;&bull;&nbsp;Tự động ánh xạ các trường: Model Serializers tự động ánh xạ các trường của model Django với các trường tương ứng trong serializer, giúp giảm thiểu mã cần viết.<br> 
    &emsp;&bull;&nbsp;Xác thực dữ liệu: Model Serializers cung cấp các phương thức để xác thực dữ liệu trước khi lưu vào cơ sở dữ liệu. <br> 
Ví dụ: 
```c
from rest_framework import serializers
from myapp.models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2', 'field3']

```
Trong ví dụ trên, MyModelSerializer sẽ tự động ánh xạ các trường field1, field2, và field3 từ model MyModel và cung cấp các phương thức để serialize và deserialize dữ liệu. <br> <br> 


5.<h3><ins>Ingest Data with Django Rest Framework Views</ins></h3>

Trong Django REST Framework (DRF), Views là nơi bạn định nghĩa logic xử lý các yêu cầu HTTP. Để ingest (nhập) dữ liệu, bạn thường sử dụng các lớp view như APIView hoặc các view dựa trên generic như CreateAPIView, ListCreateAPIView, v.v <br>

<strong>Sử dụng APIView để Ingest Dữ liệu</strong> <br>

APIView cung cấp nhiều phương thức để xử lý các yêu cầu HTTP như GET, POST, PUT, DELETE. Dưới đây là một ví dụ về cách sử dụng APIView để ingest dữ liệu: <br>
```c
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class MyModelAPIView(APIView):
    def post(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

```
Trong ví dụ này:

POST: Phương thức post nhận dữ liệu từ yêu cầu, kiểm tra tính hợp lệ của dữ liệu bằng serializer, và lưu dữ liệu vào cơ sở dữ liệu nếu hợp lệ. <br>

<strong>Sử dụng Generic Views để Ingest Dữ liệu</strong>

Generic views cung cấp các lớp view có sẵn để xử lý các thao tác CRUD. Dưới đây là ví dụ sử dụng CreateAPIView để ingest dữ liệu: <br>
```c
from rest_framework.generics import CreateAPIView
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class MyModelCreateView(CreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

```
Trong ví dụ này:

CreateAPIView: Tự động xử lý các yêu cầu POST để tạo mới một đối tượng model. <br>

<strong>Ví dụ đầy đủ với URL routing:</strong>
```c
from django.urls import path
from myapp.views import MyModelCreateView

urlpatterns = [
    path('mymodel/', MyModelCreateView.as_view(), name='mymodel-create'),
]
```
Với đoạn mã trên, bạn đã tạo một endpoint /mymodel/ để ingest dữ liệu vào model MyModel.
<br>

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
