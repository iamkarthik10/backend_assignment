from django.core.management.base import BaseCommand
from backend_test.userlogin.models import User, Activity
import argparse

class Command(BaseCommand):
    help = 'insert user data into database'

    def add_arguments(self, parser):
        parser.add_argument('Name', type=str)
        parser.add_argument('TimeZone', type=str)
        parser.add_argument('StartTime', type=str)
        parser.add_argument('EndTime', type=str)

    def handle(self, *args, **options):
        us =User.objects.filter(Real_Name=options['Name'])
        if len(us)<1:
            Usertable = User()
            Usertable.Real_Name = options['Name']
            Usertable.Timezone = options['TimeZone']
            Usertable.save()

            Activitytable = Activity()
            Activitytable.User_Id = User.objects.filter(Real_Name=options['Name'])[0]
            Activitytable.Start_Time = options['StartTime'] 
            Activitytable.End_Time = options['EndTime']
            Activitytable.save()
        elif len(us)>=1:
            Activitytable = Activity()
            Activitytable.User_Id = User.objects.filter(Real_Name=options['Name'])[0]
            Activitytable.Start_Time = options['StartTime'] 
            Activitytable.End_Time = options['EndTime']
            Activitytable.save()