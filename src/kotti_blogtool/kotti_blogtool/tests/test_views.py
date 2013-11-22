from kotti.resources import get_root

from kotti_blogtool.resources import Blog
from kotti_blogtool.views import BlogView


def test_views(db_session, dummy_request):

    root = get_root()
    content = Blog()
    root['content'] = content

    view = BlogView(root['content'], dummy_request)

    assert view.view() == {}
    assert view.alternative_view() == {}
