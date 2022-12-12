#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Fmx 2
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, GrRangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class fmx_2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fmx 2", catch_exceptions=False)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fmx 2")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fmx_2")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.vol = vol = .15
        self.vco_sens = vco_sens = 34501.8
        self.transw = transw = 250
        self.source_rate = source_rate = 32000
        self.source = source = 0
        self.samp_rate = samp_rate = 128000
        self.mode = mode = 0
        self.level = level = .2
        self.freq = freq = 1500.
        self.bploc = bploc = 1500
        self.bphic = bphic = 15000
        self.audiocomp = audiocomp = 0

        ##################################################
        # Blocks
        ##################################################
        self._bploc_range = Range(0, 10000, 1, 1500, 1)
        self._bploc_win = GrRangeWidget(self._bploc_range, self.set_bploc, "BP Low Cutoff", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_grid_layout.addWidget(self._bploc_win, 3, 1, 1, 4)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._vol_range = Range(.01, .3, .001, .15, 1)
        self._vol_win = GrRangeWidget(self._vol_range, self.set_vol, "Volume", "counter_slider", float, QtCore.Qt.Horizontal, "vol")

        self.top_grid_layout.addWidget(self._vol_win, 0, 12, 1, 3)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(12, 15):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._transw_range = Range(0, 3000, 1, 250, 10)
        self._transw_win = GrRangeWidget(self._transw_range, self.set_transw, "BP Transition Width", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_grid_layout.addWidget(self._transw_win, 3, 8, 1, 4)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(8, 12):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, 'Source')
        self.tabs_widget_1 = Qt.QWidget()
        self.tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_1)
        self.tabs_grid_layout_1 = Qt.QGridLayout()
        self.tabs_layout_1.addLayout(self.tabs_grid_layout_1)
        self.tabs.addTab(self.tabs_widget_1, 'Message')
        self.tabs_widget_2 = Qt.QWidget()
        self.tabs_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_2)
        self.tabs_grid_layout_2 = Qt.QGridLayout()
        self.tabs_layout_2.addLayout(self.tabs_grid_layout_2)
        self.tabs.addTab(self.tabs_widget_2, 'FM DeMod2 (pr. FM Signal)')
        self.tabs_widget_3 = Qt.QWidget()
        self.tabs_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_3)
        self.tabs_grid_layout_3 = Qt.QGridLayout()
        self.tabs_layout_3.addLayout(self.tabs_grid_layout_3)
        self.tabs.addTab(self.tabs_widget_3, 'FM Spectrum')
        self.tabs_widget_4 = Qt.QWidget()
        self.tabs_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_4)
        self.tabs_grid_layout_4 = Qt.QGridLayout()
        self.tabs_layout_4.addLayout(self.tabs_grid_layout_4)
        self.tabs.addTab(self.tabs_widget_4, 'DeMod')
        self.top_layout.addWidget(self.tabs)
        # Create the options list
        self._mode_options = [0, 1]
        # Create the labels list
        self._mode_labels = ['FMSig', 'CalTone']
        # Create the combo box
        # Create the radio buttons
        self._mode_group_box = Qt.QGroupBox("Mode" + ": ")
        self._mode_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._mode_button_group = variable_chooser_button_group()
        self._mode_group_box.setLayout(self._mode_box)
        for i, _label in enumerate(self._mode_labels):
            radio_button = Qt.QRadioButton(_label)
            self._mode_box.addWidget(radio_button)
            self._mode_button_group.addButton(radio_button, i)
        self._mode_callback = lambda i: Qt.QMetaObject.invokeMethod(self._mode_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._mode_options.index(i)))
        self._mode_callback(self.mode)
        self._mode_button_group.buttonClicked[int].connect(
            lambda i: self.set_mode(self._mode_options[i]))
        self.top_grid_layout.addWidget(self._mode_group_box, 0, 30, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(30, 31):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._level_range = Range(0, 1, .001, .2, 1)
        self._level_win = GrRangeWidget(self._level_range, self.set_level, "Level", "counter_slider", float, QtCore.Qt.Horizontal, "level")

        self.top_grid_layout.addWidget(self._level_win, 0, 1, 1, 3)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_range = Range(1., 10000., .001, 1500., 1)
        self._freq_win = GrRangeWidget(self._freq_range, self.set_freq, "Frequency", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_grid_layout.addWidget(self._freq_win, 0, 7, 1, 3)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(7, 10):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._bphic_range = Range(bploc+1, 25000, 1, 15000, 20)
        self._bphic_win = GrRangeWidget(self._bphic_range, self.set_bphic, "BP Hi Cutoff", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_grid_layout.addWidget(self._bphic_win, 3, 13, 1, 4)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(13, 17):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._audiocomp_options = [0, 1, 2]
        # Create the labels list
        self._audiocomp_labels = ['WAV', 'DMed', 'DMed 2']
        # Create the combo box
        # Create the radio buttons
        self._audiocomp_group_box = Qt.QGroupBox("Audio Comparisons" + ": ")
        self._audiocomp_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._audiocomp_button_group = variable_chooser_button_group()
        self._audiocomp_group_box.setLayout(self._audiocomp_box)
        for i, _label in enumerate(self._audiocomp_labels):
            radio_button = Qt.QRadioButton(_label)
            self._audiocomp_box.addWidget(radio_button)
            self._audiocomp_button_group.addButton(radio_button, i)
        self._audiocomp_callback = lambda i: Qt.QMetaObject.invokeMethod(self._audiocomp_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._audiocomp_options.index(i)))
        self._audiocomp_callback(self.audiocomp)
        self._audiocomp_button_group.buttonClicked[int].connect(
            lambda i: self.set_audiocomp(self._audiocomp_options[i]))
        self.top_grid_layout.addWidget(self._audiocomp_group_box, 0, 25, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(25, 26):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._source_options = [0, 1]
        # Create the labels list
        self._source_labels = ['Tone', 'Audio']
        # Create the combo box
        # Create the radio buttons
        self._source_group_box = Qt.QGroupBox("source" + ": ")
        self._source_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._source_button_group = variable_chooser_button_group()
        self._source_group_box.setLayout(self._source_box)
        for i, _label in enumerate(self._source_labels):
            radio_button = Qt.QRadioButton(_label)
            self._source_box.addWidget(radio_button)
            self._source_button_group.addButton(radio_button, i)
        self._source_callback = lambda i: Qt.QMetaObject.invokeMethod(self._source_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._source_options.index(i)))
        self._source_callback(self.source)
        self._source_button_group.buttonClicked[int].connect(
            lambda i: self.set_source(self._source_options[i]))
        self.top_grid_layout.addWidget(self._source_group_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            source_rate, #samp_rate
            'Sample Audio', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.001)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Rendered Audio', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['dark green', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.tabs_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_sink_x_1_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            10000, #fc
            10000, #bw
            'FM Output Spectrum', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_1_0.set_update_time(1.0/.001)
        self._qtgui_sink_x_1_0_win = sip.wrapinstance(self.qtgui_sink_x_1_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_1_0.enable_rf_freq(False)

        self.tabs_layout_3.addWidget(self._qtgui_sink_x_1_0_win)
        self.qtgui_sink_x_1 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_HAMMING, #wintype
            0, #fc
            samp_rate, #bw
            '2nd Demod', #name
            True, #plotfreq
            True, #plotwaterfall
            False, #plottime
            False, #plotconst
            None # parent
        )
        self.qtgui_sink_x_1.set_update_time(1.0/.01)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_1.enable_rf_freq(False)

        self.tabs_layout_2.addWidget(self._qtgui_sink_x_1_win)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_HAMMING, #wintype
            5000, #fc
            10000, #bw
            'FM Demodulated', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            False, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/.01)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(True)

        self.tabs_layout_4.addWidget(self._qtgui_sink_x_0_win)
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source('/Users/nattykorb/Documents/GitHub/Capstone/ASSETS/SHEARS_lps_looped_16-Bit_32kHz.wav', True)
        self.blocks_vco_f_0_1 = blocks.vco_f(samp_rate, vco_sens, 1)
        self.blocks_vco_f_0_0 = blocks.vco_f(samp_rate, vco_sens, 1)
        self.blocks_selector_1 = blocks.selector(gr.sizeof_float*1,audiocomp,0)
        self.blocks_selector_1.set_enabled(True)
        self.blocks_selector_0_0_0 = blocks.selector(gr.sizeof_float*1,mode,0)
        self.blocks_selector_0_0_0.set_enabled(True)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(vol)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff((level*50))
        self.blocks_integrate_xx_0_0 = blocks.integrate_ff(1, 1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(1)
        self.band_pass_filter_0_0 = filter.fir_filter_fcc(
            3,
            firdes.complex_band_pass(
                1,
                samp_rate,
                bploc,
                bphic,
                transw,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fcc(
            3,
            firdes.complex_band_pass(
                1,
                samp_rate,
                bploc,
                bphic,
                transw,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(32000, '', True)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_CONST_WAVE, freq, level, 0, 0)
        self.analog_fm_demod_cf_0_0 = analog.fm_demod_cf(
        	channel_rate=samp_rate,
        	audio_decim=5,
        	deviation=5000,
        	audio_pass=5000,
        	audio_stop=11000,
        	gain=1.0,
        	tau=0.0,
        )
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=samp_rate,
        	audio_decim=5,
        	deviation=5000,
        	audio_pass=5000,
        	audio_stop=11000,
        	gain=1.0,
        	tau=0.0,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_demod_cf_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.analog_fm_demod_cf_0_0, 0), (self.blocks_selector_1, 2))
        self.connect((self.analog_fm_demod_cf_0_0, 0), (self.qtgui_sink_x_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_vco_f_0_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.analog_fm_demod_cf_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_integrate_xx_0_0, 0))
        self.connect((self.blocks_integrate_xx_0_0, 0), (self.blocks_vco_f_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_selector_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_selector_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_selector_0_0_0, 0), (self.qtgui_sink_x_1_0, 0))
        self.connect((self.blocks_selector_1, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_vco_f_0_0, 0), (self.blocks_selector_0_0_0, 1))
        self.connect((self.blocks_vco_f_0_1, 0), (self.blocks_selector_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fmx_2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_vol(self):
        return self.vol

    def set_vol(self, vol):
        self.vol = vol
        self.blocks_multiply_const_vxx_1.set_k(self.vol)

    def get_vco_sens(self):
        return self.vco_sens

    def set_vco_sens(self, vco_sens):
        self.vco_sens = vco_sens

    def get_transw(self):
        return self.transw

    def set_transw(self, transw):
        self.transw = transw
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.bploc, self.bphic, self.transw, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.bploc, self.bphic, self.transw, window.WIN_HAMMING, 6.76))

    def get_source_rate(self):
        return self.source_rate

    def set_source_rate(self, source_rate):
        self.source_rate = source_rate
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.source_rate)

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source
        self._source_callback(self.source)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.bploc, self.bphic, self.transw, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.bploc, self.bphic, self.transw, window.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate)

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode
        self._mode_callback(self.mode)
        self.blocks_selector_0_0_0.set_input_index(self.mode)

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level
        self.analog_sig_source_x_0_0.set_amplitude(self.level)
        self.blocks_multiply_const_vxx_0_0.set_k((self.level*50))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0_0.set_frequency(self.freq)

    def get_bploc(self):
        return self.bploc

    def set_bploc(self, bploc):
        self.bploc = bploc
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.bploc, self.bphic, self.transw, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.bploc, self.bphic, self.transw, window.WIN_HAMMING, 6.76))

    def get_bphic(self):
        return self.bphic

    def set_bphic(self, bphic):
        self.bphic = bphic
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.bploc, self.bphic, self.transw, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.bploc, self.bphic, self.transw, window.WIN_HAMMING, 6.76))

    def get_audiocomp(self):
        return self.audiocomp

    def set_audiocomp(self, audiocomp):
        self.audiocomp = audiocomp
        self._audiocomp_callback(self.audiocomp)
        self.blocks_selector_1.set_input_index(self.audiocomp)




def main(top_block_cls=fmx_2, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print("Error: failed to enable real-time scheduling.")

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
