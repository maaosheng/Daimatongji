from django.shortcuts import render,HttpResponse,redirect
from fs.models import  *
# Create your views here.
from untitled.settings import *

def index(request):
    if request.method=='GET':
        return render(request,'index.html')


def list_view(request):
    user = request.session.get('user')
    print(user)
    if request.method=='GET':
        if user:
            obj = Userinfo.objects.filter(name=user).all()
            return render(request,'list_view.html',locals())
        else:
            return redirect('/login/')




def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        user_name = request.POST.get('name')
        pwd = request.POST.get('password')
        print(user_name)
        obj = Userinfo.objects.filter(id=1).first()
        print(obj)
        if obj:
            request.session['user'] = user_name
            return render(request,'main.html')
        else:
            return render(request, 'login.html')
from django.core.files.uploadedfile import TemporaryUploadedFile
def jishu(request):
    user = request.session.get('user')
    if request.method=='GET':
        if user:
             return render(request,'jishu.html')
        else:
            return  redirect('/login/')
    else:
        file_obj = request.FILES.get('file')
        #file 的四个对象 read （内容）,size（大小） content_type(查看属性)
        # print(file_obj.name)
        # print(file_obj.read)
        # print(file_obj.content_type)
        c,v = file_obj.name.rsplit('.',maxsplit=1)
        if not v or v!='zip':
            return HttpResponse('请上传正确格式的文件')
        import shutil
        import uuid
        import os
        # print(os.path)
        target_path = os.path.join('files', str(uuid.uuid4()))
        # target_path = os.path.join(MEDIA_PATH,str(uuid.uuid4()))
        # 接收用户上传文件，并解压到指定目录
        shutil._unpack_zipfile(file_obj, target_path)
        # with open(target_path,'wb') as f:
        #     for info in file_obj.chunks():#chunks是生成器 可以一点点的读数据 防止文件过大
        #         f.write(info)
        #     f.close()
        # print(os.walk(target_path))#循环列出该文件夹下所有的文件
        totle_num = 0
        for base_path,floder_path,filter_list in os.walk(target_path):
            for file_name in filter_list:
                file_path = os.path.join(base_path,file_name)
                try:
                    c,v = file_path.rsplit('.',maxsplit=1)
                except:
                    continue
                if not v or v!='py':
                   continue
                with open(file_path,'rb') as f1:
                        num = 0
                        for info in f1:
                            info.strip()
                            if not info:
                                continue
                            if info.startswith(b'#'):#以B开头的注释
                                continue
                            else:
                                num += 1
                totle_num += num
        import datetime
        date = str(datetime.datetime.today().date())
        num = str(totle_num)
        name = request.session.get('user')
        print(name,date,num)
        try:
             Userinfo.objects.update_or_create(name=name,date=date,num=num)
        except:
            return HttpResponse('你今天已经上传过了')

        return HttpResponse('上传成功')



def layout(request):
    if request.method=='GET':
        request.session['user'] = None
        return render(request,'index.html')