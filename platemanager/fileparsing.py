from pathlib import Path

FOLDER = "files"

class FileParsing:
    def __init__(self, first: str = "", last: str = "", plate: str = ""):
        self.first = first
        self.last = last
        self.filename = ""
        
        self.set_filename()
        self.filepath = Path(FOLDER) / self.filename
        self.plate = plate

    def clear_file(self):
        open(self.filepath, "w").close()

    def create_files(self):
        if not self.file_exists():
            file = Path(FOLDER) / self.filename
            file.touch()
        else:
            self.clear_file()

    def file_exists(self) -> bool:
        file = Path(self.filepath)
        return file.exists()
    
    def file_has_data(self) -> bool:
        file = Path(self.filepath)
        return file.stat().st_size>0

    def set_filename(self) -> None:
        self.filename = self.last[0].lower() + ".txt"
        return

    def add_to_file(self) -> None:
        with open(self.filepath, "a") as file:
            file.write(f"{self.plate} {self.first} {self.last}\n")

    def check_data_length(self, data: list) -> bool:
        return len(data) == 3

    def is_in_file(self, plate_check: bool) -> bool:

        if self.file_has_data():
            with open(self.filepath, "r") as file:
                for line in file:
                    parts = line.strip().split()
                    if self.check_data_length(parts):
                        if not plate_check:
                            given_nme = parts[1] # checking fname in file
                            last_nme = parts[2] # checking lname in file

                            if last_nme == self.last and given_nme == self.first:
                                return 1
                        else:
                            plate = parts[0] # checking plates in file
                            if plate == self.plate:
                                return 1
                    else:
                        continue 
        return 0