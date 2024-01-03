import pandas as pd
from sklearn import preprocessing
from sklearn import svm
from sklearn import model_selection


class Identifier:
    def __init__(self):
        self.svc = svm.SVC()
        self.scaler = preprocessing.StandardScaler()

        self.data = pd.read_csv("Data/spambase.data")

        self.data.columns = [
            "word_freq_make", "word_freq_address", "word_freq_all", "word_freq_3d", "word_freq_our",
            "word_freq_over", "word_freq_remove", "word_freq_internet", "word_freq_order", "word_freq_mail",
            "word_freq_receive", "word_freq_will", "word_freq_people", "word_freq_report", "word_freq_addresses",
            "word_freq_free", "word_freq_business", "word_freq_email", "word_freq_you", "word_freq_credit",
            "word_freq_your", "word_freq_font", "word_freq_000", "word_freq_money", "word_freq_hp", "word_freq_hpl",
            "word_freq_george", "word_freq_650", "word_freq_lab", "word_freq_labs", "word_freq_telnet",
            "word_freq_857", "word_freq_data", "word_freq_415", "word_freq_85", "word_freq_technology",
            "word_freq_1999", "word_freq_parts", "word_freq_pm", "word_freq_direct", "word_freq_cs",
            "word_freq_meeting", "word_freq_original", "word_freq_project", "word_freq_re", "word_freq_edu",
            "word_freq_table", "word_freq_conference", "char_freq_;", "char_freq_(", "char_freq_[", "char_freq_!",
            "char_freq_$", "char_freq_#", "capital_run_length_average", "capital_run_length_longest",
            "capital_run_length_total", "is_spam"]

        self.data = self.data.dropna()

        self.data = self.data[["word_freq_all", "word_freq_our", "word_freq_remove", "word_freq_receive",
                     "word_freq_credit", "word_freq_000", "word_freq_free",
                     "word_freq_email", "word_freq_george", "word_freq_data", "word_freq_415", "word_freq_original",
                     "word_freq_edu", "char_freq_;", "char_freq_!", "capital_run_length_average",
                     "capital_run_length_longest", "capital_run_length_total", "is_spam"]]

    def train(self, x_train, y_train):
        self.svc.fit(x_train, y_train)

    def predict(self, x_list):
        predicted = self.svc.predict(x_list)
        index = predicted[0]
        cls = ["Not Spam!", "Spam"]
        result = cls[index]
        return result

    def getLists(self):
        data = self.getData()
        x = data.drop("is_spam", axis=1)
        y = data["is_spam"]

        x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.1)

        x_train = self.scaler.fit_transform(x_train)
        x_test = self.scaler.transform(x_test)

        return x_train, x_test, y_train, y_test

    def getData(self):
        return self.data

    def evaluate_accuracy(self, x_test, y_test):
        accuracy = self.svc.score(x_test, y_test)
        return accuracy
