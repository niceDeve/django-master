"""Django Ninja - Fast Django REST framework"""

__version__ = "0.9.7"

from ninja.main import NinjaAPI
from ninja.params import Query, Path, Header, Cookie, Body, Form, File
from ninja.router import Router
from ninja.schema import Schema
from ninja.files import UploadedFile
