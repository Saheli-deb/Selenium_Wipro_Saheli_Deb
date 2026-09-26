import csv
from pathlib import Path


class CSVReader:

    @staticmethod
    def read(file_path):
        """
        Read CSV file and return rows as a list of dictionaries.
        Kept as 'read' because existing tests use CSVReader.read().
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"CSV file not found: {file_path}"
            )

        with open(
            path,
            mode="r",
            encoding="utf-8-sig",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            return list(reader)

    @staticmethod
    def read_csv(file_path):
        """
        Alias for read(), provided for reusable CSV handling.
        """

        return CSVReader.read(file_path)