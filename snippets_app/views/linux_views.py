from flask import Blueprint, render_template
from snippets_app.models import PageComponent, TreeNode
from snippets_app.utils.text_utils import (
    unescape_text, get_id_for_header
)
from snippets_app.utils.web_utils import get_list

bp = Blueprint('linux', __name__, url_prefix='/linux')


@bp.route('/')
def home():
    return get_list(node_name='Home/Linux')
