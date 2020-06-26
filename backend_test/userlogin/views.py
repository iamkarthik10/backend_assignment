from django.shortcuts import render
from django.http import JsonResponse
from userlogin.models import  User, Activity

def get_json(request):
    dic = {}
    dic['ok'] = True
    users = User.objects.all()
    members = []
    members_dit = {}
    for user in users:
        members_dit['id'] = user.id
        members_dit['real_name'] = user.Real_Name
        members_dit['tz'] = user.Timezone
        

        activity = Activity.objects.filter(User_Id=user.id)
        activity_periods = []
        activity_dict={}

        for activity in activity:
            activity_dict['start_time'] = activity.Start_Time
            activity_dict['end_time'] = activity.End_Time
            activity_periods.append(activity_dict)

        members_dit['activity_periods'] = activity_periods
        members.append(members_dit)

    dic['members'] = members
    return JsonResponse(dic)
