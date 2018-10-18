from jinja2 import Environment, PackageLoader, select_autoescape

_env = Environment(
    loader=PackageLoader('pacifica.user_mgmt.view', 'templates'),
    autoescape=select_autoescape(['html'])
)

def render(template, **kwargs):
    """ Render a Jinja2 template """
    template = _env.get_template(template + '.html.jinja2')
    return template.render(**kwargs)
