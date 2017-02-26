from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QUrlQuery

from LoginFrame import LoginFrame
from Util import MyYaml


class WebChatFrame(LoginFrame):

    url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port)
    url_t = 'http://localhost:3000'

    @staticmethod
    def init(main_widget,my_id = '', oppenent_id = ''):
        WebChatFrame.q_widget = QtWidgets.QWidget()
        WebChatFrame.q_widget.show()
        WebChatFrame.q_widget.setFixedSize(300, 600)
        WebChatFrame.q_widget.move(main_widget.mapToGlobal(QPoint(main_widget.width()+1, -23)));
        horizontalLayout = QtWidgets.QHBoxLayout(WebChatFrame.q_widget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)

        view = QtWebEngineWidgets.QWebEngineView(WebChatFrame.q_widget)
        horizontalLayout.addWidget(view)
        view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.JavascriptEnabled, True)

        url = QUrl(WebChatFrame.url+'/chat')

        urldata = QUrlQuery()
        urldata.addQueryItem('my_id', my_id)
        urldata.addQueryItem('oppenent_id', oppenent_id)
        url.setQuery(urldata)

        view.setUrl(url)
        view.show()
