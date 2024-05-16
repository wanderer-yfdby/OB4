# Принцип открытости/закрытости
# class Report():
#    def __init__(self, title, content):
#        self.title = title
#        self.content = content
#
#    def docPrinter(self):
#        print(f"сформирован отчет - {self.title} - {self.content}")

from abc import ABC, abstractmethod


class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass


class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")


class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)


report = Report('Заголовок отчета', 'это текст отчета, его тут много', TextFormatted())
report.docPrinter()

report = Report('Заголовок репортажа', 'это текст поста, срочная новость!', HtmlFormatted())
report.docPrinter()