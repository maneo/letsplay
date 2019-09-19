from xgboost import XGBClassifier
import pandas as pd
from os import path
import pickle
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


class Model:
    test_size=0.2

    def __init__(self, model, name):
        self.model = model
        self.name = name

    def evaluate_model(self, X_train, y_train, X_test, y_test):
        y_pred_test = self.model.predict(X_test)
        y_pred_train = self.model.predict(X_train)
        test_accuracy = accuracy_score(y_test, y_pred_test)
        train_accuracy = accuracy_score(y_train, y_pred_train)
        print('Training accuracy: {0:.2f}, evaluation accuracy: {1:.2f}'.format(train_accuracy, test_accuracy))

    def fit(self, x_all, y_all):
        x_train, x_test, y_train, y_test = train_test_split(x_all, y_all, test_size=Model.test_size)
        self.model.fit(x_train, y_train)
        self.evaluate_model(x_train, y_train, x_test, y_test)

    def fit_all(self, x_all, y_all):
        self.model.fit(x_all, y_all)

    def save_model(self, path):
        pickle.dump(self.model, open(path + "/ai_model_" + self.name + ".pkl", "wb"))


class LogisticModel(Model):
    def __init__(self):
        super().__init__(LogisticRegression(), "logit")


class XGB(Model):
    def __init__(self):
        super().__init__(XGBClassifier(n_estimators=1000), "xgb")

    def fit(self, x_all, y_all):
        x_train, x_test, y_train, y_test = train_test_split(x_all, y_all, test_size=Model.test_size)
        self.model.fit(x_train, y_train, eval_set = [[x_test, y_test]])
        self.evaluate_model(x_train, y_train, x_test, y_test)


class RandomForest(Model):
    def __init__(self):
        super().__init__(RandomForestClassifier(random_state=1,
                                                n_estimators=1000), "forest")


class MLP(Model):
    def __init__(self):
        super().__init__(MLPClassifier(solver='lbfgs',
                                       alpha=1e-5,
                                       hidden_layer_sizes=(28, 32, 5),
                                       random_state=1), "mlp")


class ModelVariant:
    def __init__(self, working_dir, vector_length, data_file_name):
        self.working_dir = working_dir
        self.vector_length = vector_length
        self.data_file_name = data_file_name

    def get_data_file_with_path(self):
        return path.join(self.working_dir, self.data_file_name)


def rebuild_models(variants):
    for variant in variants:

        features = ["f" + str(i) for i in range(0, variant.vector_length - 1)]
        label = ["action"]

        headers = features + label

        df = pd.read_csv(variant.get_data_file_with_path(),
                         sep=',',
                         header=None,
                         names=headers)

        print("Dataset in {} consists of {} rows (vector length {})".format(variant.working_dir, len(df), variant.vector_length))

        y_train_all = df["action"]
        x_train_all = df.drop(columns="action")

        # models = [RandomForest(), LogisticModel(), MLP(), XGB()]
        models = [MLP(), XGB()]

        for model in models:
            print("{} training started ".format(model.name))
            model.fit(x_train_all, y_train_all)
            model.save_model(variant.working_dir)
            print("model: {} - done ".format(model.name))


# variants = [ModelVariant("4_frames/", 108, "train_human.csv"),
#             ModelVariant("2_frames/", 54, "train_human.csv"),
#             ModelVariant("1_frame/", 27, "train_human.csv")]

variants = [ModelVariant("1_frame/", 27, "train_evo.csv")]

# variants = [ModelVariant("1_frame/", 27, "train_evo.csv")]
#
# variants = [ModelVariant("1_frame/", 27, "train_human.csv")]

rebuild_models(variants)