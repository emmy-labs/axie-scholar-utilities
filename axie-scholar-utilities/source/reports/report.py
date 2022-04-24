import csv
from abc import ABC
from datetime import datetime

from types import ReportType

class Report:

    def __init__(self, data):
        self.data = data
        self.path = self.get_path()

    def get_path(self) -> string:
        raise NotImplementedError()

    def format_report_name(self):
        return f"{self.type.__str__()}-{datetime.now()}.csv"

    def create(self):
        processed_data = self.process_data()
        self.write_to_file(processed_data)

    def write_to_file(self, processed_data):
        with open(self.format_report_name(), mode='w') as report_file:
            report_writer = csv.writer(report_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for data in processed_data:
                report_writer.writerow(data)

    def process_data(self) -> list:
        raise NotImplementedError()

class PaymentReport(Report):

    def __init__(self, data):
        super().__init__(data)
        self.type = ReportType.PAYMENT

    def get_path(self) -> string:
        return "reports/payments"

    def process_data(self) -> list:
        processed_data = []
        for raw_data in self.data:
           processed_data.append([raw_data[''],])
        return processed_data

class ClaimReport(Report):

    def __init__(self, data):
        super().__init__(data)
        self.type = ReportType.CLAIM

    def get_path(self) -> string:
        return "reports/claims"

    def process_data(self) -> list:
        return []