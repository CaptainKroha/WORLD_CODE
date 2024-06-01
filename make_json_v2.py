import json
import os


class JSONFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {"list": []}
        self.current_item = {"annotations": []}

        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)

    def add_annotation(self, start, end, mark):
        annotation = {
            "start": start,
            "end": end,
            "mark": mark
        }
        self.current_item["annotations"].append(annotation)

    def add_text(self, text):
        self.current_item["text"] = text
        self.data["list"].append(self.current_item)
        self.current_item = {"annotations": []}

    def add_text_from_file(self, r_path):
        with open(r_path, "r", encoding='utf-8') as f:
            text = f.read()
        self.add_text(text)

    def load_from_ndjson(self, path_):
        with open(path_, 'r', encoding='utf-8') as f:
            for line in f:
                json_data = json.loads(line)
                txt_f_path = "./TXTS1/" + json_data['data_row']['external_id']
                for project in json_data["projects"].values():
                    for label in project["labels"]:
                        for obj in label["annotations"]["objects"]:
                            self.add_annotation(obj["location"]["start"], obj["location"]["end"] + 1, obj["name"])
                        self.add_text_from_file(txt_f_path)

    def close_item(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    path = "./JSONS/data.json"
    json_file = JSONFile(path)
    json_file.load_from_ndjson("./JSONS/dataset.ndjson")
    json_file.close_item()
