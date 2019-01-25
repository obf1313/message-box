from django.shortcuts import get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
import datetime, uuid, json
from .models import User, Question
# Create your views here.


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


@csrf_exempt
def register(request):
    register_user = json.loads(request.body)
    username = register_user['username']
    password = register_user['password']
    user = User(username=username, password=password)
    user.save()
    if user.id:
        data = {'flag': 0, 'id': user.id}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def login(request):
    login_user = json.loads(request.body)
    username = login_user['username']
    password = login_user['password']
    user = get_object_or_404(User, username=username)
    out_user = user.user_vo()
    if user.password == password:
        data = {'flag': 0, 'user': out_user}
    else:
        data = {'flag': 1, 'msg': '用户名或密码错误！'}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def get_user_info(request):
    be_asked_user = json.loads(request.body)
    user_id = be_asked_user['user_id']
    user = get_object_or_404(User, pk=user_id)
    out_user = user.user_vo()
    data = {'flag': 0, 'user': out_user}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def get_question_list(request):
    be_asked_user = json.loads(request.body)
    """
    :search_type
        0: 全部
        1: 待回答
        2: 已回答
        3: 搜索关键词
    """
    search_type = be_asked_user['search_type']
    user_id = be_asked_user['user_id']
    """
    寻常用法： user = User.objects.get(pk=user_id)
     DoesNotExist exception ||  MultipleObjectsReturned
    """
    user = get_object_or_404(User, pk=user_id)
    if search_type == 0:
        """
        user.question_set 可以通过user访问question相关条目对象的列表
        .values('id', 'question_text') 只返回 id 和 question_text 字段
        """
        question_list = list(user.question_set.all().order_by('-pub_date').values())
    elif search_type == 1:
        question_list = list(user.question_set.filter(answer_text__isnull=True).order_by('-pub_date').values())
    elif search_type == 2:
        question_list = list(user.question_set.filter(answer_text__isnull=False).order_by('-pub_date').values())
    elif search_type == 3:
        search_keyword = be_asked_user['keyword']
        question_list = list(user.question_set.filter(question_text__contains=search_keyword).order_by('-pub_date').values())
    data = {'flag': 0, 'questionList': question_list}
    return HttpResponse(json.dumps(data, cls=CJsonEncoder), content_type='application/json')


@csrf_exempt
def ask_question(request):
    data = json.loads(request.body)
    user_id = data['user_id']
    question_text = data['question']
    pub_date = datetime.datetime.now()
    question = Question(question_text=question_text, pub_date=pub_date, user_id=user_id)
    question.save()
    out_question = question.question_vo()
    if question.id:
        data = {'flag': 0, 'question': out_question}
    else:
        data = {'flag': 1, 'msg': 'something trouble'}
    return HttpResponse(json.dumps(data, cls=CJsonEncoder), content_type='application/json')


@csrf_exempt
def answer_question(request):
    data = json.loads(request.body)
    question_id = data['question_id']
    answer_text = data['answer']
    answer_date = datetime.datetime.now()
    question = get_object_or_404(Question, pk=question_id)
    question.answer_text = answer_text
    question.answer_date = answer_date
    question.save()
    out_question = question.question_vo()
    data = {'flag': 0, 'question': out_question}
    return HttpResponse(json.dumps(data, cls=CJsonEncoder), content_type='application/json')