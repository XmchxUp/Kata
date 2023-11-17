import re
import datetime
from typing import Any


class ValidationError(Exception):
    pass


class Field:
    def __init__(self, blank=False, default=None):
        self.blank = blank
        self.default = default
        self.value = default

    def validate():
        raise NotImplementedError


class CharField(Field):
    def __init__(self, min_length=0, max_length=None, **kwargs):
        self.min_length = min_length
        self.max_length = max_length
        super().__init__(**kwargs)

    def validate(self, value):
        if value is None:
            return
        if not isinstance(value, str):
            raise ValidationError("Value must be a string.")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError("String is shorter than minimum length.")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError("String is longer than maximum length.")


class IntegerField(Field):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(**kwargs)

    def validate(self, value):
        if value is None:
            return
        if not isinstance(value, int):
            raise ValidationError("Value must be a integer.")
        if self.min_value is not None and value < self.min_value:
            raise ValidationError("Integer is less than minimum value.")
        if self.max_value is not None and value > self.max_value:
            raise ValidationError("Integer is greater than maximum value.")


class BooleanField(Field):
    def validate(self, value):
        if value is not None and not isinstance(value, bool):
            raise ValidationError("Value must be a boolean.")


class DateTimeField(Field):
    def __init__(self, auto_now=False, default=None, **kwargs):
        super().__init__(**kwargs)
        self.auto_now = auto_now
        self._default = default

    def __getattribute__(self, name: str) -> Any:
        if name == "default":
            if self._default is None and self.auto_now is True:
                return datetime.datetime.now()
            else:
                return self._default
        return super().__getattribute__(name)

    def validate(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise ValidationError("Value must be a datetime object.")


class EmailField(CharField):
    def validate(self, value):
        super().validate(value)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError("Value must be a valid email address.")


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {k: v for k, v in attrs.items() if isinstance(v, Field)}
        for field_name in fields:
            del attrs[field_name]
        new_class = super().__new__(cls, name, bases, attrs)
        setattr(new_class, "_fields", fields)
        return new_class


class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field_name, field in self._fields.items():
            value = kwargs.get(
                field_name,
                field.default if not callable(field.default) else field.default(),
            )
            setattr(self, field_name, value)

    def validate(self):
        for field_name, field in self._fields.items():
            value = getattr(self, field_name)
            if value is None and not field.blank:
                raise ValidationError(f"{field_name} is required.")
            if value is not None:
                field.validate(value)

    def validate(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise ValidationError("Value must be a datetime object.")


class EmailField(CharField):
    def validate(self, value):
        super().validate(value)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError("Value must be a valid email address.")


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {k: v for k, v in attrs.items() if isinstance(v, Field)}
        for field_name in fields:
            del attrs[field_name]
        new_class = super().__new__(cls, name, bases, attrs)
        setattr(new_class, "_fields", fields)
        return new_class


class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field_name, field in self._fields.items():
            value = kwargs.get(
                field_name,
                field.default if not callable(field.default) else field.default(),
            )
            setattr(self, field_name, value)

    def validate(self):
        for field_name, field in self._fields.items():
            value = getattr(self, field_name)
            if value is None and not field.blank:
                raise ValidationError(f"{field_name} is required.")
            if value is not None:
                field.validate(value)


class User(Model):
    first_name = CharField(max_length=30, default="Adam")
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)


print(DateTimeField(auto_now=True).default)
print(User(first_name="test").date_joined)
print(User(first_name="test").date_joined)
