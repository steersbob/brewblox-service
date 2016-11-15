import logging

from brewpi_service.plugins import BrewPiServicePlugin
from brewpi_service.database import db_session
from brewpi_service.admin import admin, ModelView

__plugin__ = "TimeDevicePlugin"

LOGGER = logging.getLogger(__name__)


class TimeDevicePlugin(BrewPiServicePlugin):
    def setup(self):
        from .models import Clock

    def install(self):
        from .models import Clock
        admin.add_view(ModelView(Clock, db_session))

