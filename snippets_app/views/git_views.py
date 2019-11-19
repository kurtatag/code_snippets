from flask import Blueprint, render_template
from snippets_app.models import PageComponent, TreeNode
from snippets_app.utils.text_utils import (
    unescape_text, get_id_for_header
)
from snippets_app.utils.web_utils import get_list

bp = Blueprint('git', __name__, url_prefix='/git')


@bp.route('/')
def home():
    return get_list(node_name='Home/Git')
