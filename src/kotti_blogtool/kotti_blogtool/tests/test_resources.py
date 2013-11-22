from kotti.resources import get_root
from kotti.testing import DummyRequest

from kotti_blogtool.resources import Blog


def test_blog(db_session):

    root = get_root()
    content = Blog()
    assert content.type_info.addable(root, DummyRequest()) is True
    root['content'] = content
