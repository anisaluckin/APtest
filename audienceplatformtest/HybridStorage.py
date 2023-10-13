from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string

from django.conf import settings


@deconstructible
class HybridPublicStorage(Storage):

    def __init__(self, acl=None, bucket=None, location=None, base_url=None, **settings):
        self.client = get_hybrid_storage_class()()

    def __getstate__(self):
        return self.client.__getstate__

    def __setstate__(self, state):
        self.client.__setstate__(state)

    def _open(self, name, mode='rb'):
        return self.client._open(name=name, mode=mode)

    def _save(self, name, content):
        return self.client._save(name=name, content=content)

    def _save_content(self, obj, content, parameters):
        self.client._save_content(obj=obj, content=content, parameters=parameters)

    def delete(self, name):
        self.client.delete(name)

    def exists(self, name):
        return self.client.exists(name)

    def listdir(self, name):
        return self.client.listdir(name)

    def size(self, name):
        return self.client.size(name)

    def path(self, name):
        return self.client.path(name)

    def get_accessed_time(self, name):
        return self.client.get_accessed_time(name)

    def get_created_time(self, name):
        return self.client.get_created_time(name)

    def get_modified_time(self, name):
        return self.client.get_modified_time(name)

    def modified_time(self, name):
        return self.client.modified_time(name)

    def url(self, name, parameters=None, expire=None):
        return self.client.url(name)

    def get_valid_name(self, name):
        return self.client.get_valid_name(name)

    def get_available_name(self, name, max_length=None):
        return self.client.get_available_name(name, max_length=max_length)


def get_hybrid_storage_class(import_path=None):
    return import_string(import_path or settings.DEFAULT_FILE_STORAGE)

class DefaultHybridStorage(LazyObject):
    def _setup(self):
        self._wrapped = HybridPublicStorage()


default_hybrid_storage = DefaultHybridStorage()
