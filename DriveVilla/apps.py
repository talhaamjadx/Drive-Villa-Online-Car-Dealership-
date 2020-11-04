from django.apps import AppConfig

class DrivevillaConfig(AppConfig):
    name = 'DriveVilla'
    
    def ready(self):
        print("hello from startup")
        import DriveVilla.signals
        from os import path
        from users.models import CustomUser
        from DriveVilla import tasks
        users = CustomUser.objects.all()
        for user in users:
            print("The File for {} exists = {}".format(user.username, path.exists("model/Model/"+user.username+".hdf5")))
            if(not (path.exists("model/Model/"+ user.username + ".hdf5"))):
                tasks.createUser.delay('hello',user.username)

