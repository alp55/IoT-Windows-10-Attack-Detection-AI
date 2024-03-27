import sys,threading
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from arayuz import Ui_Form
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_Form()
        self.ui.setupUi(self) 
        self.ui.baslat.clicked.connect(self.analizet)
        self.dataframe_lock = QtCore.QMutex()  # Veri değişikliklerini senkronize etmek için kilitleme mekanizması

    def analizet(self):
        # Veriyi al
        self.dataframe = pd.read_csv('Iot_Windows_10_random.csv')

        # İkili model için analiz yap
        model_ikili = joblib.load('Iot_model_ikili.pkl')
        dataframe_ikili = self.dataframe.drop("type", axis=1)
        dataframe_ikili = dataframe_ikili.apply(pd.to_numeric, errors='coerce', axis=1)
        correlations = dataframe_ikili.corr()['label']
        columns_to_drop = correlations[correlations.isna()].index
        dataframe_ikili = dataframe_ikili.drop(columns=columns_to_drop, axis=1)
        columns_add = [column for column, correlation in correlations.items() 
                       if 0 < correlation < 0.3052701147994894 
                       or -0.10585134837663442 <= correlation < 0]
        columns_add.append("label")
        dataframe_selected_ikili = dataframe_ikili[columns_add]
        dataframe_ikili = dataframe_selected_ikili.drop(["label"], axis=1).values
        tahmin_ikili = model_ikili.predict(dataframe_ikili)
        tahmin_ikili = pd.DataFrame({"Analiz Türü": tahmin_ikili})
        tahmin_ikili['Analiz Türü'] = tahmin_ikili['Analiz Türü'].map({0: 'Zararsız', 1: 'Zararlı'})
        print("İkili Model Tahminleri:")
        print(tahmin_ikili)

        # Çoklu model için analiz yap
        model_multi = joblib.load('Iot_model_multi.pkl')
        df = self.dataframe
        label_encoder = LabelEncoder()
        df['type_encoded'] = label_encoder.fit_transform(df['type'])
        df = df.drop("type", axis=1)
        df = df.apply(pd.to_numeric, errors='coerce', axis=1)
        correlations = df.corr()['type_encoded']
        columns_to_drop = correlations[correlations.isna()].index
        df = df.drop(columns=columns_to_drop, axis=1)
        columns_add = [column for column, correlation in correlations.items() 
                       if 0 < correlation < 0.14972162479892778 
                       or -0.1645839900029373 <= correlation < 0]
        columns_add.append("type_encoded")
        dataframe_selected_multi = df[columns_add]
        dataframe_selected_multi = dataframe_selected_multi.fillna(0)
        X_multi = dataframe_selected_multi.drop(["type_encoded"], axis=1).values
        tahmin_multi = model_multi.predict(X_multi)
        tahmin_multi = pd.DataFrame({"Atak Türü": tahmin_multi})
        class_names = ['ddos', 'dos', 'injection', 'mitm', 'normal', 'password', 'scanning', 'xss']
        tahmin_multi['Atak Türü'] = tahmin_multi['Atak Türü'].apply(lambda x: class_names[int(x)])
        print("Çoklu Model Tahminleri:")
        print(tahmin_multi)

        # tahmin_multi ve tahmin_ikili veri çerçevelerini birleştirme
        birlesik_tahmin = pd.concat([tahmin_ikili, tahmin_multi], axis=1)
        rastgele_sutunlar = dataframe_selected_multi.sample(n=12, axis=1)
        birlesik_tahmin = pd.concat([rastgele_sutunlar, birlesik_tahmin], axis=1)

        # QTableWidget'i oluştur
        self.ui.veriaktar.setColumnCount(len(birlesik_tahmin.columns))
        self.ui.veriaktar.setHorizontalHeaderLabels(birlesik_tahmin.columns)

        # Verileri QTableWidget'e ekle
        self.update_table(birlesik_tahmin)

    def update_table(self, birlesik_tahmin):
        self.ui.veriaktar.setRowCount(0)  # Mevcut satırları temizle

        def add_row(row):
            row_data = birlesik_tahmin.iloc[row]
            row_position = self.ui.veriaktar.rowCount()
            self.ui.veriaktar.insertRow(row_position)
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.veriaktar.setItem(row_position, col, item)

                # 'Analiz Türü' sütunundaki değere göre satır rengini ayarla
                if row_data["Analiz Türü"] == "Zararlı":
                    item.setBackground(QColor(255, 0, 0))  # Kırmızı
                else:
                    item.setBackground(QColor(0, 255, 0))  # Yeşil

        def add_rows(start_row, end_row):
            for i in range(start_row, end_row):
                add_row(i)
                QtWidgets.QApplication.processEvents()  # GUI'nin donmamasını sağlamak için işlemleri işleyin
                QtCore.QThread.msleep(250)  # 1 saniye bekleyin

        # İş parçacığı oluştur ve başlat
        thread = threading.Thread(target=lambda: add_rows(0, len(birlesik_tahmin)))
        thread.start()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
