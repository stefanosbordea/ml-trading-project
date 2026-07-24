from load import data_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def build_radom_forest(param_name,list,accuracy_list_train,accuracy_list_cv):
    for i in list:
        model = RandomForestClassifier(**{param_name: i}, random_state= 55).fit(x_train,y_train)

        predictions_train = model.predict(x_train)
        predictions_cv = model.predict(x_cv)
        accuracy_train = accuracy_score(predictions_train,y_train)
        accuracy_cv = accuracy_score(predictions_cv,y_cv)
        accuracy_list_train.append(accuracy_train)
        accuracy_list_cv.append(accuracy_cv)


def plot_random_forest(label_name,list,accuracy_list_train,accuracy_list_cv):
    plt.title("Train x Validation metrics")
    plt.xlabel(label_name)
    plt.ylabel("accuracy")
    plt.xticks(ticks=range(len(list)),labels=list)
    plt.plot(accuracy_list_train)
    plt.plot(accuracy_list_cv)
    plt.legend(["Train","Validation"])
    plt.show()

x_train,x_cv,x_test,y_train,y_cv,y_test = data_split()

min_samples_split_list = [2,10,30,50,100,200,300,700]
max_depth_list = [2,4,8,16,32,64,None]
n_estimators_list = [10,50,100,500]

splits_accuracy_list_train = []
splits_accuracy_list_cv = []
build_radom_forest("min_samples_split",min_samples_split_list,splits_accuracy_list_train,splits_accuracy_list_cv)
plot_random_forest("min_samples_split",min_samples_split_list,splits_accuracy_list_train,splits_accuracy_list_cv)

depth_accuracy_list_train = []
depth_accuracy_list_cv = []
build_radom_forest("max_depth",max_depth_list,depth_accuracy_list_train,depth_accuracy_list_cv)
plot_random_forest("max_depth",max_depth_list,depth_accuracy_list_train,depth_accuracy_list_cv)

estimators_accuracy_list_train = []
estimators_accuracy_list_cv = []
build_radom_forest("n_estimators",n_estimators_list,estimators_accuracy_list_train,estimators_accuracy_list_cv)
plot_random_forest("n_estimators",n_estimators_list,estimators_accuracy_list_train,estimators_accuracy_list_cv)








