from django.apps import AppConfig


class DrivevillaConfig(AppConfig):
    name = 'DriveVilla'

    def ready(self):
        import DriveVilla.signals
