#coding=utf-8
from django.views.generic import TemplateView


class HtmlTemplateView(TemplateView):
    """
    静态页地址
    """

    def get_template_names(self):
        template_name = self.kwargs["docs_name"] + ".html"
        return template_name
