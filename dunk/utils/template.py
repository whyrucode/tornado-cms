# coding: utf8

from jinja2 import Environment, FileSystemLoader, Template


def st(template_file, **kw):
    env = Environment(loader=FileSystemLoader(['./dunk/template','./dunk/static/js']))
    template = env.get_template(template_file)
    return template.render(**kw)
