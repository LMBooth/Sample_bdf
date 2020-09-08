from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import os
import matplotlib
matplotlib.use("module://kivy.garden.matplotlib.backend_kivy")
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas
import matplotlib.pyplot as plt
import mne
from mne.viz._figure import MNEBrowseFigure
from mne.viz.raw import return_params, plot_raw_alt
kv = """
<Test>:
	orientation: 'vertical'
	Button:
		text: "MNE Kivy Test Button"
		size_hint_y: None
		height: 40
		on_press: print("testing")
"""
Builder.load_string(kv)

class Test(BoxLayout):
	def __init__(self, *args, **kwargs):
		super(Test, self).__init__(*args, **kwargs)
		sample_data_folder = mne.datasets.sample.data_path()
		sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',
											'sample_audvis_raw.fif')
		filename = 	'C:\\Users\\Liam\\Documents\\python\\kivy\\current\\Raw_Test_Data.bdf'								
		self.raw = raw = mne.io.read_raw_bdf(filename)
		params = return_params(self.raw)
		self.fig = plt.figure(FigureClass=MNEBrowseFigure, **params)
		canvas = FigureCanvas(self.fig)
		plot_raw_alt(self.raw,  butterfly=False, figs = self.fig)
		self.add_widget(canvas)

class TestApp(App):
	def build(self):
		return Test()
if __name__ == '__main__':
	TestApp().run()