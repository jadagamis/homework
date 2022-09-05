import statistics
import re

response = input("Enter data: ")
print("\n")

def process_data(data_set: str):
    data_set = re.split(",\s|,", data_set)
    for i in range(0, len(data_set)):
        data_set[i] = int(data_set[i])
    return data_set


class Summary:
    def __init__(self, data_set: list):
        self.data_set = sorted(data_set)
        self.mean = None
        self.mode = None
        self.range = None
        self.first_quartile = None
        self.second_quartile = None
        self.third_quartile = None
        self.iqr = None
        self.outliers = None

    def get_mean(self):
        total = sum(self.data_set)
        mean = total / len(self.data_set)
        self.mean = mean
        return mean

    def get_mode(self):
        mode = statistics.mode(self.data_set)
        self.mode = mode
        return mode

    def get_range(self):
        range = self.data_set[-1] - self.data_set[0]
        self.range = range
        return range

    def get_second_quartile(self):
        median = statistics.median(self.data_set)
        self.second_quartile = median
        return median

    def get_first_quartile(self):
        if len(self.data_set) % 2 != 0:
            median_position = int((len(self.data_set) / 2) + 0.5)
            del self.data_set[median_position]
            half = int(len(self.data_set) / 2)
            updated = self.data_set[:half]
            q1 = statistics.median(updated)
            self.first_quartile = q1
            return q1
        elif len(self.data_set) % 2 == 0:
            half = int(len(self.data_set) / 2)
            q1 = statistics.median(self.data_set[:half])
            self.first_quartile = q1
            return q1

    def get_third_quartile(self):
        if len(self.data_set) % 2 != 0:
            median_position = int((len(self.data_set) / 2) + 0.5)
            del self.data_set[median_position]
            half = int(len(self.data_set) / 2)
            updated = self.data_set[half:]
            q3 = statistics.median(updated)
            self.third_quartile = q3
            return q3
        elif len(self.data_set) % 2 == 0:
            half = int(len(self.data_set) / 2)
            q3 = statistics.median(self.data_set[half:])
            self.third_quartile = q3
            return q3

    def get_interquartile_range(self, q3, q1):
        iqr = q3 - q1
        self.iqr = iqr
        return iqr

    def get_outliers(self):
        outliers = []
        for i in self.data_set:
            if self.first_quartile - (1.5 * self.iqr) > i or i > self.third_quartile + (1.5 * self.iqr):
                outliers.append(i)
        self.outliers = outliers
        return outliers


x = Summary(process_data(response))
x.get_mean()
x.get_mean()
x.get_mode()
x.get_range()
x.get_second_quartile()
x.get_interquartile_range(x.get_third_quartile(), x.get_first_quartile())
x.get_outliers()

# attributes = vars(x)
# for key, value in attributes.items():
#     print(f'{key:20}{value}')
