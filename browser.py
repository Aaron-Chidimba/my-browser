import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

#create a class for my object window
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('http://google.com'))
		self.setCentralWidget(self.browser)
		self.showMaximized()

		#create navbar
		navbar = QToolBar()
		self.addToolBar(navbar)
		#create back btn
		back_btn = QAction('Back', self)
		back_btn.triggered.connect(self.browser.back)
		navbar.addAction(back_btn)

		#create forward btn
		forward_btn = QAction('Forward', self)
		forward_btn.triggered.connect(self.browser.forward)
		navbar.addAction(forward_btn)

		#create refresh/reload btn
		reload_btn = QAction('Reload', self)
		reload_btn.triggered.connect(self.browser.reload)
		navbar.addAction(reload_btn)

		#create home btn and call it
		home_btn = QAction('Home', self)
		home_btn.triggered.connect(self.navigate_home)
		navbar.addAction(home_btn)
		#call home
	def navigate_home(self):
		self.browser.setUrl(QUrl('http://youtube.com'))

		# create Qline edit
		self.url_bar = QlineEdit()
		self.url_bar.returnPressed.connect(self.navigate_to_url)
		navbar.addWidget(self.url_bar)

		#call QLine edit

	def navigate_to_url(self):
		url = self.url_bar.text()
		self.browser.setUrl(QUrl(url))

		#create an update url function
		self.browser.urlChanged.connect(self.update_url)
		#create a call

	def update_url(self, q):
		self.url_bar.setText(q.toString())
		


#create a call class function
app = QApplication(sys.argv)
QApplication.setApplicationName('Thocco Browser')
window = MainWindow()
app.exec_()
