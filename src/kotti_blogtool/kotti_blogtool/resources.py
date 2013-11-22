import datetime
from dateutil.tz import tzutc

from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import types

from kotti.resources import Document
from kotti_blogtool import _


class UTCDateTime(types.TypeDecorator):
    impl = types.DateTime

    def process_bind_param(self, value, engine):
        if value is not None:
            return value.astimezone(tzutc())

    def process_result_value(self, value, engine):
        if value is not None:
            return datetime.datetime(value.year, value.month, value.day,
                                     value.hour, value.minute, value.second,
                                     value.microsecond,
                                     tzinfo=tzutc())


class Blog(Content):
    """My content type"""

    id = Column(
        Integer(),
        ForeignKey('contents.id'),
        primary_key=True
    )

    type_info = Content.type_info.copy(
        name=u'Blog',
        title=_(u'Blog Folder'),
        add_view=u'add_blog',
        addable_to=['Document', ],
        selectable_default_views=[
            ('alternative-view', _(u"Alternative View")),
        ],
    )

    def __init__(self, example_attribute=u"", **kwargs):
        super(Blog, self).__init__(**kwargs)


class BlogEntry(Document):
    id = Column(
        Integer,
        ForeignKey('documents.id'),
        primary_key=True
    )
    date = Column(
        'date',
        UTCDateTime()
    )

    type_info = Document.type_info.copy(
        name=u'Blog entry',
        title=_(u'Blog entry'),
        add_view=u'add_blogentry',
        addable_to=[u'Blog'],
    )

    def __init__(self, date=None, **kwargs):
        super(BlogEntry, self).__init__(**kwargs)
        self.date = date
