import warnings
from flask.exthook import ExtDeprecationWarning
warnings.simplefilter('ignore', ExtDeprecationWarning)

from flask import Blueprint
from flask_autodoc import Autodoc


doc = Blueprint('doc', __name__)
auto = Autodoc()


@doc.route('/')
def public_doc():
    generate_docs = auto.html(
        groups=['public'], title='API Documentation', template="docs_template.html")
    return generate_docs
